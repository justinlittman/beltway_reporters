import csv


def load_limit_user_ids():
    limit_user_ids = set()
    for lookup_filepath in (
            '../jupyter/lookups/periodical_press_lookup.csv',
            '../jupyter/lookups/senate_press_lookup.csv',
            '../jupyter/lookups/radio_and_television_lookup.csv'):
        limit_user_ids.update(load_seed_list(lookup_filepath))
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
    limit_user_ids = load_limit_user_ids()
    filter_agents('agent_Agent-2017-07-09.csv', 'agent_Agent-2017-07-09-filtered.tsv', limit_user_ids)

    # From Nodeset: Agent > Editor click Nodes > Clean Nodeset > Export Blank Change List
    # Wait for change list. For some reason, it take a long time to export.
    # Run this on change list
    # From Data Management > Change List Manager click Load > Change List and then
