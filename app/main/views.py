# import the main blue print instance
from app.main import main
from flask import request, jsonify, abort
from flask import current_app
import logging
import mariadb
import sys


@main.route('/hello', methods=['GET'])
def hello():
    return 'Hello World'


@main.route('/databases', methods=['GET'])
def databases():
    print("databases route")
    # Connect to MariaDB Platform
    # try:
    conn = mariadb.connect(
        user="cc_user",
        password="password",
        host="mariadb",
        port=3306

    )
    # except mariadb.Error as e:
    #     print(f"Error connecting to MariaDB Platform: {e}")
    #     sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    cur.execute(
        "SHOW DATABASES;",
    )

    for row in cur:
        print(row)

    return "databases"