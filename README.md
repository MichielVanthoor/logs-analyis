# Logs Analysis

This Python script uses psycopg2 to query a mock PostgreSQL database for a fictional news website. 
This script answers following questions using PostgreSQL queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


Requirements:
* Python 3, PostgreSQL, psycopg2

Steps to launch the analysis:
* Download and unzip [newsdta.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), this file contains the database of the fictional news website
* Import the schema and data from the database in your PostgreSQL environment
* Run **logs_analysis.py** to launch the analysis(eg. `python logs_analysis.py`)

Enjoy!
