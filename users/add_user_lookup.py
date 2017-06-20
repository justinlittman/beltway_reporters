from twarc import Twarc
import csv
import argparse

t = Twarc()


def read_csv(filepath):
    rows = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        field_names = next(reader)
        for row in reader:
            rows.append(row)

    return field_names, rows


def write_csv(filepath, field_names, rows):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        writer.writerows(rows)


def description_field(row, field_names):
    if len(field_names) != len(row):
        return None
    return row[-1]


def user_lookup(user_ids):
    user_description_map = {}
    for user in t.user_lookup(user_ids=user_ids):
        user_description_map[user['id_str']] = user['description']
    return user_description_map


def process(filename):
    field_names, rows = read_csv(filename)
    if field_names[-1] != 'description':
        field_names.append('description')

    for group_count, group in enumerate([rows[i:i + 100] for i in range(0, len(rows), 100)]):
        user_ids = []
        for row in group:
            if not description_field(row, field_names):
                user_ids.append(row[0])
        print('Looking up {} users in group {}'.format(len(user_ids), group_count + 1))
        if user_ids:
            user_description_map = user_lookup(user_ids)
            for row in group:
                if row[0] in user_ids:
                    if user_description_map.get(row[0]):
                        row.append(user_description_map[row[0]])
                    else:
                        row.append('-')
    write_csv(filename, field_names, rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args()
    process(args.filename)


