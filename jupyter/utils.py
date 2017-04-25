import json
import gzip
import logging
import pandas as pd

logger = logging.getLogger()


def tweet_iter(filepaths, limit=None, tweet_transform_func=None):
    # Load tweets from gzipped, line-oriented JSON files, possibly transforming with provided function
    # and limiting by number of tweets.
    # Returns an iterator.
    for filepath in filepaths:
        with gzip.open(filepath) as file:
            for count, line in enumerate(file):
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
                if count + 1 == limit:
                    break


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
        'newspaper_reporters.csv': 'reporters',
        'periodical_reporters.csv': 'reporters',
        'administration_officials.csv': 'politicians',
        'news_outlets.csv': 'media',
        'media.csv': 'media',
        'cabinet.csv': 'politicians',
        'representatives.csv': 'politicians',
        'senators.csv': 'politicians',
        'federal_agencies.csv': 'government',
    }
    df = pd.DataFrame(seed_iter(seed_file_map))
    df['screen_name_lower'] = df.screen_name.apply(str.lower)
    return df.drop_duplicates(subset='screen_name_lower').set_index(['user_id'])
