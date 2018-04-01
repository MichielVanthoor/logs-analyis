#!/usr/bin/env python3

import psycopg2
from datetime import datetime


def execute_sql(query):
    """Connect to the news database, execute query and return results."""

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()

    return results


def query_and_print_q1():
    """Execute the query for question 1 and print the results."""

    print("1. What are the most popular three articles of all time?")
    results = execute_sql("SELECT articles.title, COUNT(log.id) as views \
            FROM log, articles \
            WHERE log.path = '/article/' || articles.slug \
            AND log.status = '200 OK' AND log.method = 'GET' \
            GROUP BY articles.title \
            ORDER BY views DESC \
            LIMIT 3; \
            ")

    for row in results:
        print("\"{}\" - {} views".format(row[0], row[1]))

    print


def query_and_print_q2():
    """Execute the query for question 2 and print the results."""

    print("2. Who are the most popular article authors of all time?")
    results = execute_sql("SELECT authors.name, COUNT(log.id) as views \
            FROM log,articles,authors \
            WHERE log.path = '/article/' || articles.slug \
            AND articles.author = authors.id \
            GROUP BY authors.name \
            ORDER BY views DESC;  \
            ")
    for row in results:
        print("{} - {} views".format(row[0], row[1]))

    print


def query_and_print_q3():
    """Execute the query for question 3 and print the results."""
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
        print('{0:%B %d, %Y} - {1:.2f}% errors'.format(row[0], row[1]))

    print


def main():
    print("#####")
    print("Welcome to our Log Analysis!")
    print("#####")
    query_and_print_q1()
    query_and_print_q2()
    query_and_print_q3()


if __name__ == '__main__':
    main()
