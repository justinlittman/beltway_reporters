import csv
import os


def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        type_map = {}
        reader = csv.reader(csvfile)
        # Skip header
        next(reader)
        for row in reader:
            user_id = row[0]
            screen_name = row[1]
            type = row[4].lower() if row[4] != '-' else 'other'
            if type:
                if type not in type_map:
                    type_map[type] = []
                type_map[type].append((screen_name, user_id))

    return type_map


def write_lookup_csv(filepath, rows):
    print('Writing {} to {}'.format(len(rows), filepath))
    # This will append new users
    user_ids = read_lookup_csv(filepath)
    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        for row in rows:
            if row[1] not in user_ids:
                writer.writerow(row)


def read_lookup_csv(filepath):
    user_ids = []
    if os.path.exists(filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
            for row in reader:
                user_ids.append(row[1])
    return user_ids

if __name__ == '__main__':
    m_type_map = read_csv('unknown_mentions.csv')
    for m_type, m_users in m_type_map.items():
        write_lookup_csv('coded_{}_lookup.csv'.format(m_type.replace(' ', '_')), m_users)