import sqlite3
import time
import requests
import colored
from colored import *

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
    print(f"""
{Fore.cyan_1} ██████╗ ██████╗ ███████╗███╗   ██╗      ██╗   ██╗███████╗███████╗██████╗       ██████╗ ██████╗{Style.reset}
{Fore.cyan_1}██╔═══██╗██╔══██╗██╔════╝████╗  ██║      ██║   ██║██╔════╝██╔════╝██╔══██╗      ██╔══██╗██╔══██╗{Style.reset}
{Fore.cyan_1}██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗██║   ██║███████╗█████╗  ██████╔╝█████╗██║  ██║██████╔╝{Style.reset}
{Fore.cyan_1}██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║╚════╝██║   ██║╚════██║██╔══╝  ██╔══██╗╚════╝██║  ██║██╔══██╗{Style.reset}
{Fore.cyan_1}╚██████╔╝██║     ███████╗██║ ╚████║      ╚██████╔╝███████║███████╗██║  ██║      ██████╔╝██████╔╝{Style.reset}
{Fore.cyan_1} ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝       ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝{Style.reset}                                             
            {Fore.grey_27}  ▄{Fore.white}                                                             {Fore.grey_27}▄{Style.reset}   
            {Fore.grey_27}▄█▀{Fore.white} ▄█████ ▄████▄ ██████ ██████ ██     ██ ▄████▄ █████▄  ██████ {Fore.grey_27}▀█▄{Style.reset} 
            {Fore.grey_27}██{Fore.white}  ▀▀▀▄▄▄ ██  ██ ██▄▄     ██   ██ ▄█▄ ██ ██▄▄██ ██▄▄██▄ ██▄▄    {Fore.grey_27}██{Style.reset} 
            {Fore.grey_27}▀█▄{Fore.white} █████▀ ▀████▀ ██       ██    ▀██▀██▀  ██  ██ ██   ██ ██▄▄▄▄ {Fore.grey_27}▄█▀{Style.reset} 
            {Fore.grey_27}  ▀{Fore.white}                                                             {Fore.grey_27}▀{Style.reset}    
                            {Fore.yellow}       _  _   __ ___  _         _{Style.reset}  
                            {Fore.yellow} \  / |_ |_) (_   |  / \ |\ |    ){Style.reset} 
                            {Fore.yellow}  \/  |_ | \ __) _|_ \_/ | \|   /_{Style.reset}    
{Fore.cyan_1}                         
                                                    
░█▀▀░█▀█░█▄█░█▄█░█▀█░█▀█░█▀▄░░░█░░░▀█▀░█▀▀░▀█▀░░░░
░█░░░█░█░█░█░█░█░█▀█░█░█░█░█░░░█░░░░█░░▀▀█░░█░░░▀░
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░░▀░░░▀░{Style.reset}

{Fore.black}{Back.cyan_1}{Style.italic}Notes:{Style.reset}
    {Fore.black}{Back.white}LOAD{Style.reset} — Download Public Database (If you have local notes, they may not be saved!).
    {Fore.black}{Back.white}VIEW{Style.reset} — View all notes.
    {Fore.black}{Back.white}ADD{Style.reset} — Add local note.
    {Fore.black}{Back.white}DELETE{Style.reset} — Delete note from your device.
    {Fore.black}{Back.white}PUBLISH{Style.reset} — Publish your note in Public Database.{Style.reset}
{Fore.black}{Back.cyan_1}{Style.italic}Search:{Style.reset}
    {Fore.black}{Back.white}SEARCH_USERNAME{Style.reset} — Search by Username (first value in note).
    {Fore.black}{Back.white}SEARCH_FIRSTNAME{Style.reset} — Search by First Name.
    {Fore.black}{Back.white}SEARCH_LASTNAME{Style.reset} — Search by Last Name.
    {Fore.black}{Back.white}SEARCH_MIDDLENAME{Style.reset} — Search by Middle Name.
    {Fore.black}{Back.white}SEARCH_AGE{Style.reset} — Search by Age.
    {Fore.black}{Back.white}SEARCH_ACCOUNT{Style.reset} — Search by Username in other Social Networks.
    {Fore.black}{Back.white}SEARCH_PHONENUMBER{Style.reset} — Search by Phone Number.{Style.reset}
{Fore.black}{Back.cyan_1}{Style.italic}Other:{Style.reset}
    {Fore.black}{Back.white}GITHUB{Style.reset} — Program's repository on GitHub.
    {Fore.black}{Back.white}SOCIALS{Style.reset} — Program's channels/groups in Social Networks.{Style.reset}
    {Fore.black}{Back.white}CREDITS{Style.reset} — Authors of Program.
          """)
    choice = input(f"{Fore.black}{Back.white}INPUT COMMAND:{Style.reset} ")
    return choice

def LOAD():
    open("OPEN-USER-DB.db", "wb").write(requests.get("https://raw.githubusercontent.com/RudolfusPlay/OPEN-USER-DB/main/OPEN-USER-DB.db").content)
    print(f"{Fore.white}{Back.green}SUCCESFUL{Style.reset}")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def VIEW():
    cursor.execute("SELECT * FROM Main")
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def ADD():
    input(f"{Fore.white}{Back.yellow}WARNING:{Style.reset} if your Username matches another user in the Database, your note will not be saved. Press ENTER to continue. ")
    newusername = input(f"Unique Username for {Fore.cyan_1}OPEN-USER-DB{Style.reset}: ")
    newfirstname = input(f"Your First Name: ")
    newlastname = input(f"Your Last Name: ")
    newmiddlename = input(f"Your Middle Name (if you have): ")
    newage = input(f"Your Age: ")
    newaccount = input(f"Your Account in other Social Network for communication ([social network name] - [your username there]): ")
    newphonenumber = input(f"Your Phone Number (not necessary): ")

    cursor.execute("""INSERT INTO Main(username, firstname, lastname, middlename, age, account, phonenumber)
        VALUES(?, ?, ?, ?, ?, ?, ?)""", (newusername, newfirstname, newlastname, newmiddlename, newage, newaccount, newphonenumber))
    db.commit()
    print(f"{Fore.white}{Back.green}SUCCESFUL{Style.reset}")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def DELETE():
    delete = input(f"Input Username (first value in note): ")
    cursor.execute("DELETE FROM Main WHERE username = ?", [delete])
    db.commit()
    print(f"{Fore.white}{Back.green}SUCCESFUL{Style.reset}")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")


def PUBLISH():
    print(f"{Fore.cyan_1}Soon...{Style.reset}")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_USERNAME():
    search = input(f"Input Username: ")
    cursor.execute("SELECT * FROM Main WHERE username = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_FIRSTNAME():
    search = input(f"Input First Name: ")
    cursor.execute("SELECT * FROM Main WHERE firstname = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_LASTNAME():
    search = input(f"Input Last Name: ")
    cursor.execute("SELECT * FROM Main WHERE lastname = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_MIDDLENAME():
    search = input(f"Input Middle Name: ")
    cursor.execute("SELECT * FROM Main WHERE middlename = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_AGE():
    search = input(f"Input Age: ")
    cursor.execute("SELECT * FROM Main WHERE age = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_ACCOUNT():
    search = input(f"Input Account ([social network name] - [username there]): ")
    cursor.execute("SELECT * FROM Main WHERE account = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SEARCH_PHONENUMBER():
    search = input(f"Input Last Name: ")
    cursor.execute("SELECT * FROM Main WHERE phonenumber = ?", [search])
    for all in cursor.fetchall():
        print(all)
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def GITHUB():
    print(f"Program's repository on GitHub — {Fore.light_blue}https://github.com/RudolfusPlay/OPEN-USER-DB{Style.reset}")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def SOCIALS():
    print(f"""Telegram — {Fore.light_blue}https://t.me/OPEN_USER_DB{Style.reset}
Discord — {Fore.light_blue}https://discord.gg/GPt6PfQhBm{Style.reset}""")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

def CREDITS():
    print(f"""Creator — RudolfusPlay (РудольфусПлей)""")
    input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")   

def main():
    choice = None
    while True:
        choice = display_menu()
        if choice == "LOAD":
            LOAD()
        elif choice == "VIEW":
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
        elif choice == "GITHUB":
            GITHUB()
        elif choice == "SOCIALS":
            SOCIALS()
        elif choice == "CREDITS":
            CREDITS()
        else:
            print(f"{Fore.white}{Back.red}INCORRECT COMMAND{Style.reset}")
            input(f"Press {Fore.black}{Back.white}ENTER{Style.reset} to open menu. ")

main()
db.close()
