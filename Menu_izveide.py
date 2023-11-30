import mysql.connector
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SchoolMySQL55!",
    database="contact"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS darbinieki (
        name char(30) primary key,
        address char(100),
        mobile char(15),
        email char(30)
    );
""")

def intro():
    print("=" * 80)
    print("{:^80s}".format("DARBINIEKU"))
    print("{:^80s}".format(""))
    print("{:^80s}".format("PROJEKTS"))
    print("{:^80s}".format("Autori: Rainers Grigors, Ričards Tarvids, ? Kurtiša"))
    print("=" * 80)
    print()
    time.sleep(2)

def main():
    intro()
    while True:
        print("\nMAIN MENU ")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. EXIT")
        print()
        ch = int(input("Izvēlies opciju (1-6): "))
        print()
        if ch == 1:
            print("piemērs:ADD NEW RECORD")
            ()
        elif ch == 2:
            print("piemērs:SEARCH RECORD BY NAME")
            name = input("Enter name: ")
            search(name)
        elif ch == 3:
            print("piemērs:DISPLAY ALL RECORDS")
            display_all()
        elif ch == 4:
            print("piemērs:DELETE RECORD")
            name = input("Enter name: ")
            delete_record(name)
        elif ch == 5:
            print("piemērs:MODIFY RECORD")
            name = input("Enter name: ")
            modify_record(name)
        elif ch == 6:
            print("piemērs:Thanks for using Contact Book")
            db.close()
            break
        else:
            print("Invalid choice")


main()
   