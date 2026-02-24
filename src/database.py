import sqlite3
from datetime import datetime
from pathlib import Path
from tkinter import messagebox
from platformdirs import user_data_dir


def getDbPath():
    app_name = "TradingNotes"

    appdata = Path(user_data_dir(appname=app_name, appauthor=False))
    appdata.mkdir(parents=True, exist_ok=True)
    #messagebox.showinfo("Path", f"{appdata}")
    return appdata / "TradingNotes.db"

def connect():
    return sqlite3.connect(getDbPath())


def initDb():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Trades (
                tradeID INTEGER PRIMARY KEY AUTOINCREMENT,
                entryTime TEXT NOT NULL,
                exitTime TEXT NOT NULL,
                marketStructure TEXT NOT NULL,
                type TEXT NOT NULL,
                bais TEXT NOT NULL,
                risk REAL NOT NULL,
                result TEXT NOT NULL,
                emotions TEXT NOT NULL,
                takeaways TEXT NOT NULL,
                accountType TEXT NOT NULL,
                rewardRatio REAL NOT NULL,

                CHECK(result IN ("win", "loss", "be")),
                CHECK(type IN ("inter-day", "swing")),
                CHECK(accountType IN ("live", "paper", "eval"))
            );
        """)


def getNow():
    return datetime.now().isoformat(sep=" ", timespec="seconds")


def insertToDb(data):

    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Trades (
                entryTime, exitTime, marketStructure, type, bais,
                risk, result, emotions, takeaways, accountType, rewardRatio
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
            data["entryDate"], data["exitDate"], data["marketStructure"], data["type"].lower(), 
            data["bias"], data["risk"], data["result"].lower(), data["emotions"],
            data["takeaways"], data["accountType"].lower(), data["rewardRatio"] 
        ))
        conn.commit()
        messagebox.showinfo("Success", "Trade added")
    except sqlite3.Error as e:
        messagebox.showerror("Insert to Database Error", str(e))
    finally:
        conn.close()


def executeSelectQuery(query):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(query)

        rows = cur.fetchall()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", "Failed to fetch all data from database")
        return None

    finally:
        if conn:
            conn.close()

    return rows

class trade:
    def __init__(
        self, id, entryDate, exitDate, marketStrucutre,
        type, bias, risk, result, emotions, takeaways, 
        accountType, rewardRatio,
    ):
        self.id = id
        self.entryDate = entryDate
        self.exitDate = exitDate
        self.marketStructure = marketStrucutre
        self.type = type
        self.bias = bias
        self.risk = risk
        self.result = result
        self.emotions = emotions
        self.takeaways = takeaways
        self.accountType = accountType
        self.rewardRatio = rewardRatio



def readIntoClasses(rows):
    assert rows is not None, "Rows is None"
    trades = []
    for row in rows:
        assert len(row) == 12, f"Unexpected row length {len(row)}"
        trades.append(trade(
            row[0], row[1], row[2], row[3],
            row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11]
        ))
    return trades











