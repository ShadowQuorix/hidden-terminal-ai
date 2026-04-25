import sqlite3

DB = "targets.db"


def init():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS targets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        status TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_target(target):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO targets (target, status, result) VALUES (?, ?, ?)",
        (target, "pending", "")
    )

    conn.commit()
    conn.close()


def get_targets():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT id, target, status, result FROM targets")
    rows = c.fetchall()

    conn.close()
    return rows


def update_status(target_id, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "UPDATE targets SET status=? WHERE id=?",
        (status, target_id)
    )

    conn.commit()
    conn.close()


def save_result(target_id, result):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "UPDATE targets SET status=?, result=? WHERE id=?",
        ("done", result, target_id)
    )

    conn.commit()
    conn.close()