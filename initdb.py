import sqlite3

import os


def init_db():
    db = sqlite3.connect(
        os.path.join('F:\pythonproject\flaskdemo', 'sqlite'),
        detect_types=sqlite3.PARSE_DECLTYPES
    )

    with open('sql/schema.sql', 'r') as f:
        db.executescript(f.read().decode('utf8'))

    db.close()