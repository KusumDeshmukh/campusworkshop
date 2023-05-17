"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="postgres://betsol:luNjdoi2fwMyIxpXS4wn1ayELfCTRVoH@dpg-chi83q5269vf5qbdueh0-a.oregon-postgres.render.com/todo_qow3",
        database="todo_qow3",
        user="betsol",
        password="luNjdoi2fwMyIxpXS4wn1ayELfCTRVoH")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
