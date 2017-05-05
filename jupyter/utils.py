import json
import gzip
import logging
import glob
import pandas as pd

logger = logging.getLogger()


def tweet_load_iter(limit=None, tweet_transform_func=None):
    # Load tweets from gzipped, line-oriented JSON files, possibly transforming with provided function
    # and limiting by number of tweets.
    # Returns an iterator.
    count = 0
    for filepath in glob.glob('tweets/*.json.gz'):
        logging.info('Loading from %s', filepath)
        with gzip.open(filepath) as file:
            for line in file:
                count += 1
                if count % 50000 == 0:
                    logging.debug('Loaded %s', count)
                tweet = json.loads(line)
                if tweet_transform_func:
                    tweet_transform_ret = tweet_transform_func(tweet)
                    if isinstance(tweet_transform_ret, list):
                        for tweet in tweet_transform_ret:
                            yield tweet
                    elif tweet_transform_ret is not None:
                        yield tweet_transform_ret
                else:
                    yield tweet
                if count == limit:
                    return


def tweet_type(tweet):
    # Determine the type of a tweet
    if tweet.get('in_reply_to_status_id'):
        return 'reply'
    if 'retweeted_status' in tweet:
        return 'retweet'
    if 'quoted_status' in tweet:
        return 'quote'
    return 'original'


def seed_iter(seed_file_map):
    for filepath, type in seed_file_map.items():
        with open(filepath) as file:
            for line in file:
                screen_name, user_id = line.split(',')
                yield {'screen_name': screen_name, 'user_id': user_id[:-1], 'type': type}


def load_screen_name_lookup_df():
    seed_file_map = {
        'lookups/newspaper_reporters_lookup.csv': 'reporters',
        'lookups/periodical_reporters_lookup.csv': 'reporters',
        'lookups/tv_and_radio_reporters_lookup.csv': 'reporters',
        'lookups/administration_officials_lookup.csv': 'politicians',
        'lookups/press_galleries_lookup.csv': 'media',
        'lookups/news_outlets_lookup.csv': 'media',
        'lookups/cabinet_lookup.csv': 'politicians',
        'lookups/representatives_lookup.csv': 'politicians',
        'lookups/senators_lookup.csv': 'politicians',
        'lookups/federal_agencies_lookup.csv': 'government',
    }
    df = pd.DataFrame(seed_iter(seed_file_map))
    df['screen_name_lower'] = df.screen_name.apply(str.lower)
    return df.drop_duplicates(subset='screen_name_lower').set_index(['user_id'])
