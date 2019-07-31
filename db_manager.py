import sqlite3
import os
import pprint

RESOURCE_PATH = "resources"
DB_NAME = "bottle_tag.db"
try:
    if not os.path.exists(RESOURCE_PATH):
        os.makedirs(RESOURCE_PATH)
except OSError:
    pass
CON = sqlite3.connect(os.path.join(RESOURCE_PATH, DB_NAME))


def save(tb_name, image_name, tag):
    create_stmt = f"CREATE TABLE  IF NOT EXISTS {tb_name} (image_name text PRIMARY KEY ON CONFLICT REPLACE , tag text)"
    CON.execute(create_stmt)
    insert_stmt = f"replace INTO {tb_name} (image_name, tag) VALUES(?, ?) "
    CON.execute(insert_stmt, (image_name, tag))

    CON.commit()


def get_all(tb_name):
    results = []
    for row in CON.execute(f"SELECT * FROM {tb_name} order by image_name"):
        results.append(row)
    return results


def get_all_tables():
    results = []
    for row in CON.execute(f"SELECT name FROM sqlite_master WHERE type='table'"):
        results.append(row[0])
    return results

