import fileinput
from twarc import Twarc
import os

t = Twarc()


def get_followings(user_ids):
    existing_followed_user_ids = set()
    new_followed_user_ids = set()
    if os.path.exists('followed.csv'):
        with open('followed.csv') as followed_file:
            for line in followed_file:
                existing_followed_user_ids.add(user_id_from_line(line))
        print('Loaded {} existing followed users'.format(len(existing_followed_user_ids)))
    with open('follower_to_followed.csv', 'w') as follower_to_followed_file:
        for count, user_id in enumerate(user_ids):
            print('Getting following for {} ({})'.format(user_id, count + 1))
            for followed_user_id in t.friend_ids(user_id):
                follower_to_followed_file.write('{},{}\n'.format(user_id, followed_user_id))
                if followed_user_id not in existing_followed_user_ids:
                    new_followed_user_ids.add(followed_user_id)
    print('Found {} new followed users'.format(len(new_followed_user_ids)))
    with open('followed.csv', 'a') as followed_file:
        count = 0
        for count, user in enumerate(t.user_lookup(user_ids=new_followed_user_ids)):
            screen_name = user['screen_name']
            user_id = user['id_str']
            if user_id in new_followed_user_ids:
                print('Screen name for {} is {} ({} of {})'.format(user_id, screen_name, count + 1,
                                                                   len(new_followed_user_ids)))
                followed_file.write('{},{}\n'.format(screen_name, user_id))
        print('Added {} new followed users'.format(count + 1 if count else 0))


def user_id_from_line(line):
    return line[:-1].split(',')[1]


if __name__ == '__main__':
    # Given one or more files with screen_name,user_id per line.
    get_followings(user_id_from_line(line) for line in fileinput.input())
