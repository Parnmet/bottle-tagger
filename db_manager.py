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


def get_all_path(path):
    dir_name = []
    p, d = os.path.split(path)
    while p != "" and d != "":
        dir_name.append(d)
        p, d = os.path.split(p)
    dir_name.reverse()
    return dir_name


def save(path, tag):
    full_path = get_all_path(path)
    tb_name = f"{full_path[-3]}_{full_path[-2]}"
    create_stmt = f"CREATE TABLE  IF NOT EXISTS {tb_name} (image_name text PRIMARY KEY ON CONFLICT REPLACE , tag text)"
    CON.execute(create_stmt)
    insert_stmt = f"replace INTO {tb_name} (image_name, tag) VALUES(?, ?) "
    CON.execute(insert_stmt, (full_path[-1], tag))

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


if __name__ == "__main__":
    print(get_all(get_all_tables()[0]))
