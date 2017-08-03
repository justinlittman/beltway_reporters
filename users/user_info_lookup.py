import csv
from twarc import Twarc
import json

t = Twarc()


# From a CSV containing names, organizations, screen names, position, gender, race,
# create a lookup CSV containing screen names, user_ids, name, organization, position
# gender, user_created_at, follower_counts, following_counts, tweet_count, verified, protected

def csv_iter(filepaths):
    for filepath in filepaths:
        with open(filepath, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                handle = clean_cell(row['Handle'])
                if handle and row['Color (y/p/w)'].lower() == 'w':
                    yield {
                        'screen_name': handle.lower().lstrip('@'),
                        'name': clean_cell(row['Name']),
                        'organization': clean_cell(row['Organization']),
                        'position': clean_cell(row['Position']),
                        'gender': clean_cell(row['Gender']),
                    }


def write_csv(user_map):
    with open('user_info_lookup.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL,
                                fieldnames=['screen_name', 'user_id', 'name', 'organization', 'position', 'gender',
                                            'followers_count', 'following_count', 'tweet_count',
                                            'user_created_at', 'verified', 'protected'])
        writer.writerows(user_map.values())


def clean_cell(cell):
    if cell and cell != '-':
        return cell.strip()
    return None


if __name__ == '__main__':
    user_map = {}
    for user in csv_iter(['Senate_Press_Galleries.csv', 'Senate_Periodical_Galleries.csv', 'Radio_and_Television.csv']):
        user_map[user['screen_name']] = user

    for user_json in t.user_lookup(screen_names=user_map.keys()):
        user = user_map.get(user_json['screen_name'].lower())
        if user:
            user['user_id'] = user_json['id_str']
            user['followers_count'] = user_json['followers_count']
            user['following_count'] = user_json['friends_count']
            user['tweet_count'] = user_json['statuses_count']
            user['user_created_at'] = user_json['created_at']
            user['verified'] = user_json['verified']
            user['protected'] = user_json['protected']

    # Remove entries without match
    screen_names = list(user_map.keys())
    for screen_name in screen_names:
        if 'user_id' not in user_map[screen_name]:
            del user_map[screen_name]

    write_csv(user_map)