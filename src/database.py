import sqlite3
from datetime import datetime
from pathlib import Path
from tkinter import messagebox



def getDbPath():
    appdata = Path.home() / "AppData" / "Local" / "TradingNotes"
    appdata.mkdir(parents=True, exist_ok=True)
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
                CHECK(type IN ("interday", "swing")),
                CHECK(accountType IN ("live", "paper", "eval"))
            );
        """)


def getNow():
    return datetime.now().isoformat(sep=" ", timespec="seconds")


def insertToDb(
    entryTime, exitTime, structure, type1, bias,
    risk, result, emotions, takeaways, accountType,
    riskToRR
):

    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Trades (
                entryTime, exitTime, marketStructure, type, bais,
                risk, result, emotions, takeaways, accountType, rewardRatio
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
            entryTime, exitTime, structure, type1.lower(), bias,
            risk, result.lower(), emotions, takeaways, accountType.lower(), riskToRR
        ))
        conn.commit()
        messagebox.showinfo("Success", "Trade added")
    except sqlite3.Error as e:
        messagebox.showerror("Insert to Database Error", str(e))
    finally:
        conn.close()
