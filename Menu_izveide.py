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
    print("{:^80s}".format("INFORMĀCIJA"))
    print("{:^80s}".format("PROJEKTS"))
    print("{:^80s}".format("Autori: Rainers Grigors, Ričards Tarvids, Elīna Kurtiša"))
    print("=" * 80)
    print()
    time.sleep(2)

def main_menu():
    intro()
    while True:
        print("\nMAIN MENU ")
        print("1. Pievienot darbinieku")
        print("2. Meklēt darbiniekus")
        print("3. Izdzēst darbinieku")
        print("4. Aprēķina algas")
        print("5. Darba laiks")
        print("6. Iziet")
        print()
        time.sleep(2)

def create_record():
    vards = input("Ierakstiet vārdu: ")
    adrese = input("Ierakstiet adresi: ")
    nummurs = input("Ierakstiet telefona nummuru: ")
    email = input("Ierakstiet email: ")
    sql = "INSERT INTO darbinieki(vards, adrese, telefona nummurs, email) VALUES (%s,%s,%s,%s)"
    record = (vards, adrese, nummurs, email)
    cursor.execute(sql, record)
    db.commit()
    print("Record Entered Successfully\n")

def search(vards):
    sql = "SELECT * FROM book WHERE name = %s"
    value = (vards,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("Šāda ieraksta nav")
    else:
        print('Vārds:', record[0])
        print('Adrese:', record[1])
        print('Telefona nummurs:', record[2])
        print('E-mail:', record[3])


def delete_record(vards):
    sql = "DELETE FROM darbinieki WHERE name = %s"
    value = (vards,)
    cursor.execute(sql, value)
    db.commit()
    if cursor.rowcount == 0:
        print("Ieraksts nav atrasts")
    else:
        print("Ieraksts veiksmīgi dzēsts")

def modify_record(vards):
    sql = "SELECT * FROM book WHERE name = %s"
    value = (vards,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("No such record exists")
    else:
        while True:
            print("\nPress the option you want to edit: ")
            print("1. Vārds")
            print("2. Adrese")
            print("3. Telefona nummurs")
            print("4. Atpakaļ")
            print()
            ch = int(input("Izvēlies opciju (1-4): "))
            if ch == 1:
                jauns_vards = input("Ierakstiet jauno vārdu: ")
                sql = "UPDATE darbinieki SET vards = %s WHERE vards = %s"
                values = (jauns_vards, vards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 2:
                jauna_adrese = input("Ierakstiet jaunu adresi: ")
                sql = "UPDATE darbinieki SET adrese = %s WHERE vards = %s"
                values = (jauna_adrese, vards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 3:
                jauns_nummurs = input("Ierakstiet jauno telefona nummuru : ")
                sql = "UPDATE darbinieki SET nummurs = %s WHERE vards = %s"
                values = (jauns_nummurs, vards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 4:
                break
            else:
                print("Nederīga izvēle !!!\n")


        ch = int(input("Izvēlies opciju (1-7): "))
        print()
        if ch == 1:
            print("PIEVIENOT DARBINIEKU")
            create_record()
        elif ch == 2:
            print("MEKLĒT DARBINIEKU")
            name = input("Enter name: ")
            search(name)
        elif ch == 3:
            print("IZDZĒST DARBINIEKU")
            delete_record()
        elif ch == 4: 
            print("Modificēt ierakstu")
            name = input("Enter name: ")
            modify_record(name)
        elif ch == 5:
            print("APRĒĶINA ALGAS")
            name = input("Enter name: ")
            _record(name)
        elif ch == 6:
            print("DARBA LAIKS")
            name = input("Enter name: ")
            _reord(name)
        elif ch == 7:
            print("Iziet")
            db.close()
            break
        else:
            print("Invalid choice")

main_menu()
   