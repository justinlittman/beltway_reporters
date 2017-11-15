import csv
import argparse

def load_limit_user_ids(seed_list_filepaths):
    limit_user_ids = set()
    for seed_list_filepath in seed_list_filepaths:
        limit_user_ids.update(load_seed_list(seed_list_filepath))
    return limit_user_ids


def load_seed_list(filepath):
    """
    For reading a list of user ids from a seed list downloaded from SFM.
    """
    user_ids = []
    # Encoding handles the BOM
    with open(filepath, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # user id to screen name
            user_ids.append(row['Uid'])
    return user_ids


def filter_agents(input_filepath, output_filepath, limit_user_ids):
    with open(input_filepath) as input_csvfile, open(output_filepath, 'w') as output_csvfile:
        reader = csv.DictReader(input_csvfile)
        writer = csv.DictWriter(output_csvfile, fieldnames=reader.fieldnames, delimiter='\t')
        writer.writeheader()
        for row in reader:
            if row['Current Node Name'] not in limit_user_ids:
                row['Action'] = 'delete'
            writer.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('agent_input_file')
    parser.add_argument('agent_output_file')
    parser.add_argument('seed_list_files', nargs='+')
    args = parser.parse_args()

    limit_user_ids = load_limit_user_ids(args.seed_list_files)
    assert args.agent_output_file.endswith('.tsv')
    filter_agents(args.agent_input_file, args.agent_output_file, limit_user_ids)
