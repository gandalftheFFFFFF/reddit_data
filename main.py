__author__ = 'niels'

import json
import psycopg2
import praw

with open('secrets.json') as f:
    """ Method to get username and password from secrets.json """
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    return secrets[setting]

try:
    conn = psycopg2.connect("dbname='reddit_test' user='test_user' host='localhost' password='{}'".format(get_secret('DATABASE_PASSWORD')))
except:
    print('Unable to log in')

r = praw.Reddit(user_agent='Test script by /u/niels_learns_python')

submissions = r.get_subreddit('news').get_top_from_day(limit=25)

cur = conn.cursor()



for s in submissions:
    cur.execute(
        """
        SELECT * from data WHERE title=%(title)s
        """, {'title': s.title}
    )
    if cur.rowcount > 0:
        cur.execute(
            """
            UPDATE data SET score=%(new_score)s WHERE title=%(title)s
            """, {'new_score': s.score, 'title': s.title}
        )
    else:
        cur.execute(
            """
            INSERT INTO data VALUES (%(title)s, %(score)s)
            """, {'title': s.title, 'score': s.score}
        )

conn.commit()
cur.close()
cur.close()