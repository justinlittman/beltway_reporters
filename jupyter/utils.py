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


def load_tweet_df(tweet_transform_func, columns, limit=None, dedupe=True):
    tweet_df = pd.DataFrame(tweet_load_iter(tweet_transform_func=tweet_transform_func, limit=limit),
                        columns=columns)
    if dedupe:
        tweet_df.drop_duplicates(['tweet_id'], keep='last', inplace=True)

    return tweet_df


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


def load_user_type_lookup_df():
    seed_file_map = {
        'lookups/newspaper_reporters_lookup.csv': 'journalists',
        'lookups/periodical_reporters_lookup.csv': 'journalists',
        'lookups/tv_and_radio_reporters_lookup.csv': 'journalists',
        'lookups/administration_officials_lookup.csv': 'politicians',
        'lookups/press_galleries_lookup.csv': 'media',
        'lookups/news_outlets_lookup.csv': 'media',
        'lookups/cabinet_lookup.csv': 'politicians',
        'lookups/representatives_lookup.csv': 'politicians',
        'lookups/senators_lookup.csv': 'politicians',
        'lookups/federal_agencies_lookup.csv': 'government',
        'lookups/coded_academic_institution_lookup.csv': 'academic',
        'lookups/coded_academic_lookup.csv': 'academic',
        'lookups/coded_business_person_lookup.csv': 'business',
        'lookups/coded_company_lookup.csv': 'business',
        'lookups/coded_entertainment_lookup.csv': 'cultural',
        'lookups/coded_foreign_government_lookup.csv': 'foreign_political',
        'lookups/coded_foreign_politician_lookup.csv': 'foreign_political',
        'lookups/coded_gov_official_lookup.csv': 'government',
        'lookups/coded_government_lookup.csv': 'government',
        'lookups/coded_media_lookup.csv': 'media',
        'lookups/coded_ngo_lookup.csv': 'ngo',
        'lookups/coded_ngo_staff_lookup.csv': 'ngo',
        'lookups/coded_non-federal_government_lookup.csv': 'government',
        'lookups/coded_other_lookup.csv': 'other',
        'lookups/coded_political_org_lookup.csv': 'other_political',
        'lookups/coded_political_staff_lookup.csv': 'other_political',
        'lookups/coded_politician_lookup.csv': 'politicians',
        'lookups/coded_public_figure_lookup.csv': 'cultural',
        'lookups/coded_pundit_lookup.csv': 'pundit',
        'lookups/coded_reporter_lookup.csv': 'journalists',
        'lookups/coded_sports_lookup.csv': 'cultural'
    }
    df = pd.DataFrame(seed_iter(seed_file_map))
    df['screen_name_lower'] = df.screen_name.apply(str.lower)
    return df.drop_duplicates(subset='screen_name_lower').set_index(['user_id'])
