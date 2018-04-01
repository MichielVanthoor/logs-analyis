# Log Analysis Project

import psycopg2
from datetime import datetime


def execute_sql(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()

    return results


def question1():
    print("1. What are the most popular three articles of all time?")
    results = execute_sql("SELECT articles.title, COUNT(log.id) as views \
            FROM log, articles \
            WHERE log.path LIKE '%' || articles.slug \
            AND log.status = '200 OK' AND log.method = 'GET' \
            GROUP BY articles.title \
            ORDER BY views DESC \
            LIMIT 3; \
            ")

    for row in results:
        print("\"{}\" - {} views".format(row[0], row[1]))

    print


def question2():
    print("2. Who are the most popular article authors of all time?")
    results = execute_sql("SELECT authors.name, COUNT(log.id) as views \
            FROM log,articles,authors \
            WHERE log.path LIKE '%' || articles.slug \
            AND articles.author = authors.id \
            GROUP BY authors.name \
            ORDER BY views DESC;  \
            ")
    for row in results:
        print("{} - {} views".format(row[0], row[1]))

    print


def question3():
    print("3. On which days did more than 1% of requests lead to errors?")
    results = execute_sql("SELECT date, errors*100.0/total as rate \
            FROM ( \
                SELECT time::date as date, COUNT(status) as total, \
                SUM(case when status='404 NOT FOUND' \
                then 1 else 0 end) as errors \
                FROM log \
                GROUP BY date) l \
            WHERE errors*100.0/total > 1;  \
            ")

    for row in results:
        print("{} - {}% errors".format(row[0].strftime("%b %d, %Y"),
              round(row[1], 2)))

print("#####")
print("Welcome to our Log Analysis!")
print("#####")
question1()
question2()
question3()
