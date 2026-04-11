import sqlite3

with sqlite3.connect("OPEN-USER-DB.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Main(
               username text PRIMARY KEY,
               firstname text NOT NULL,
               lastname text NOT NULL,
               middlename text,
               age text NOT NULL,
               account text NOT NULL,
               phonenumber text);
               """)

def display_menu():
    print("""
 ██████╗ ██████╗ ███████╗███╗   ██╗      ██╗   ██╗███████╗███████╗██████╗       ██████╗ ██████╗ 
██╔═══██╗██╔══██╗██╔════╝████╗  ██║      ██║   ██║██╔════╝██╔════╝██╔══██╗      ██╔══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗██║   ██║███████╗█████╗  ██████╔╝█████╗██║  ██║██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║╚════╝██║   ██║╚════██║██╔══╝  ██╔══██╗╚════╝██║  ██║██╔══██╗
╚██████╔╝██║     ███████╗██║ ╚████║      ╚██████╔╝███████║███████╗██║  ██║      ██████╔╝██████╔╝
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝       ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝                                                  
              ▄                                                             ▄   
            ▄█▀ ▄█████ ▄████▄ ██████ ██████ ██     ██ ▄████▄ █████▄  ██████ ▀█▄ 
            ██  ▀▀▀▄▄▄ ██  ██ ██▄▄     ██   ██ ▄█▄ ██ ██▄▄██ ██▄▄██▄ ██▄▄    ██ 
            ▀█▄ █████▀ ▀████▀ ██       ██    ▀██▀██▀  ██  ██ ██   ██ ██▄▄▄▄ ▄█▀ 
              ▀                                                             ▀     

█▀▀ █▀█ █▀▄▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄   █░░ █ █▀ ▀█▀ ▀
█▄▄ █▄█ █░▀░█ █░▀░█ █▀█ █░▀█ █▄▀   █▄▄ █ ▄█ ░█░ ▄

Note:
    VIEW — View all notes.
    ADD — Add local note.
    DELETE — Delete note from your device.
    PUBLISH — Publish your note in Public Database.
Search:
    SEARCH_USERNAME — Search by Username (first value in note).
    SEARCH_FIRSTNAME — Search by First Name.
    SEARCH_LASTNAME — Search by Last Name.
    SEARCH_MIDDLENAME — Search by Middle Name.
    SEARCH_AGE — Search by Age.
    SEARCH_ACCOUNT — Search by Username in other Social Networks.
    SEARCH_PHONENUMBER — Search by Phone Number.
          """)
    choice = input("INPUT COMMAND: ")
    return choice

def VIEW():
    cursor.execute("SELECT * FROM Main")
    for all in cursor.fetchall():
        print(all)

def ADD():
    newusername = input("Unique username for OPEN-USER-DB: ")
    newfirstname = input("Your First Name: ")
    newlastname = input("Your Last Name: ")
    newmiddlename = input("Your Middle Name (if you have): ")
    newage = input("Your Age: ")
    newaccount = input("Your account in other social network for communication ([social network name] - [your username there]): ")
    newphonenumber = input("Your Phone Number (not necessary): ")

    cursor.execute("""INSERT INTO Main(username, firstname, lastname, middlename, age, account, phonenumber)
        VALUES(?, ?, ?, ?, ?, ?, ?)""", (newusername, newfirstname, newlastname, newmiddlename, newage, newaccount, newphonenumber))
    db.commit()

def DELETE():
    id = input("Введите ID для удаления: ")
    cursor.execute("DELETE FROM Names WHERE id = ?", [id])
    db.commit()

def PUBLISH():
    print("Soon...")

def SEARCH_USERNAME():
    search = input("Input Username: ")
    cursor.execute("SELECT * FROM Main WHERE username = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_FIRSTNAME():
    search = input("Input First Name: ")
    cursor.execute("SELECT * FROM Main WHERE firstname = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_LASTNAME():
    search = input("Input Last Name: ")
    cursor.execute("SELECT * FROM Main WHERE lastname = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_MIDDLENAME():
    search = input("Input Middle Name: ")
    cursor.execute("SELECT * FROM Main WHERE middlename = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_AGE():
    search = input("Input Age: ")
    cursor.execute("SELECT * FROM Main WHERE age = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_ACCOUNT():
    search = input("Input Account ([social network name] - [username there]): ")
    cursor.execute("SELECT * FROM Main WHERE account = ?", [search])
    for all in cursor.fetchall():
        print(all)

def SEARCH_PHONENUMBER():
    search = input("Input Last Name: ")
    cursor.execute("SELECT * FROM Main WHERE phonenumber = ?", [search])
    for all in cursor.fetchall():
        print(all)

def main():
    choice = None
    while True:
        choice = display_menu()
        if choice == "VIEW":
            VIEW()
        elif choice == "ADD":
            ADD()
        elif choice == "DELETE":
            DELETE()
        elif choice == "PUBLISH":
            PUBLISH()
        elif choice == "SEARCH_USERNAME":
            SEARCH_USERNAME()
        elif choice == "SEARCH_FIRSTNAME":
            SEARCH_FIRSTNAME()
        elif choice == "SEARCH_LASTNAME":
            SEARCH_LASTNAME()
        elif choice == "SEARCH_MIDDLENAME":
            SEARCH_MIDDLENAME()
        elif choice == "SEARCH_AGE":
            SEARCH_AGE()
        elif choice == "SEARCH_ACCOUNT":
            SEARCH_ACCOUNT()
        elif choice == "SEARCH_PHONENUMBER":
            SEARCH_PHONENUMBER()
        else:
            print("INCORRECT COMMAND")

main()
db.close()
