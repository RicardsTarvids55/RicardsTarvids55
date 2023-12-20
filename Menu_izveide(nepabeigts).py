import mysql.connector
import time, math

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SchoolMySQL55!",
    database="uznemums"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS darbinieki (
        id INT AUTO_INCREMENT PRIMARY KEY,
        vārds VARCHAR(255), 
        uzvārds VARCHAR(255), 
        vecums CHAR(3), 
        pilsēta VARCHAR(255),
        adrese VARCHAR(255),
        telefona_numurs CHAR(8)
    );
""")

def intro():
    print("=" * 80)
    print("{:^80s}".format("DARBINIEKU"))
    print("{:^80s}".format("INFORMĀCIJAS"))
    print("{:^80s}".format("PROJEKTS"))
    print("{:^80s}".format("Autori: Rainers Grigors, Ričards Tarvids, Elīna Kurtiša"))
    print("=" * 80)
    print()
    time.sleep(2)

def create_record():
    vards = input("Ierakstiet vārdu: ")
    uzvards = input("Ierakstiet uzvārdu: ")
    vecums = input("Ierakstiet vecumu: ")
    pilseta = input("Ierakstiet pilsētas nosaukumu: ")
    adrese = input("Ierakstiet adresi: ")
    telefona_numurs = input("Ierakstiet telefona numuru: ")
    sql = "INSERT INTO darbinieki(vārds, uzvārds, vecums, pilsēta, adrese, telefona_numurs) VALUES (%s,%s,%s,%s,%s,%s)"
    record = (vards, uzvards, vecums, pilseta, adrese, telefona_numurs,)
    cursor.execute(sql, record)
    db.commit()
    print("Ieraksts veiksmīgi ierakstīts\n")

def search(vards_uzvards):
    vards, uzvards = vards_uzvards.split()
    sql = "SELECT * FROM darbinieki WHERE vārds = %s AND uzvārds = %s"
    value = (vards, uzvards)
    cursor.execute(sql, value)
    result = cursor.fetchall()
    if result:
        for row in result:
            print('ID:', row[0])
            print('Vārds:', row[1])
            print('Uzvārds:', row[2])
            print('Vecums:', row[3])
            print('Pilsēta:', row[4])
            print('Adrese:', row[5])
            print('Telefona numurs:', row[6])
            print()
    else:
        print("Nav atrasts neviens ieraksts.")
    cursor.close()
    db.close()


def delete_record(vards, uzvards):
    try:
        sql_delete = "DELETE FROM darbinieki WHERE vārds  = %s AND uzvārds = %s"
        value = (vards, uzvards)
        cursor.execute(sql_delete, value)
        db.commit()

        if cursor.rowcount == 0:
            print ("Ieraksts nav atrasts")
        else:
            print ("Ieraksts veiksmīgi dzēsts")

            cursor.execute("SET @count = 0;")
            cursor.execute("UPDATE darbinieki SET id = @count:= @count +1;")
            cursor.execute("ALTER TABLE darbinieki AUTO_INCREMENT = 1;")
    except Exception as e:
        print(f"ERROR: {e}")

def modify_record(vards, uzvards):
    sql = "SELECT * FROM darbinieki WHERE vārds = %s AND uzvārds = %s"
    value = (vards, uzvards)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("Šāda ieraksts nepastāv")
    else:
        while True:
            print("\nPress the option you want to edit: ")
            print("1. Vārds")
            print("2. Uzvārds")
            print("3. Vecums")
            print("4. Pilsēta")
            print("5. Adrese")
            print("6. Telefona numurs")
            print("7. Atpakaļ")
            print()
            ch = int(input("Izvēlies opciju (1-7): "))
            if ch == 1:
                jauns_vards = input("Ierakstiet jauno vārdu: ")
                sql = "UPDATE darbinieki SET vārds = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauns_vards, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
                vards = jauns_vards
            elif ch == 2:
                jauns_uzvards = input("Ierakstiet jauno uzvārdu: ")
                sql = "UPDATE darbinieki SET uzvārds = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauns_uzvards, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
                uzvards = jauns_uzvards
            elif ch == 3:
                jauns_vecums = input("Ierakstiet jauno vecumu : ")
                sql = "UPDATE darbinieki SET vecums = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauns_vecums, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 4:
                jauna_pilseta = input("Ierakstiet jauno pilsētu: ")
                sql = "UPDATE darbinieki SET pilsēta = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauna_pilseta, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 5:
                jauna_adrese = input("Ierakstiet jaunu adresi: ")
                sql = "UPDATE darbinieki SET adrese = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauna_adrese, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 6:
                jauns_numurs = input("Ierakstiet jauno telefona numuru : ")
                sql = "UPDATE darbinieki SET telefona_numurs = %s WHERE vārds = %s AND uzvārds = %s"
                values = (jauns_numurs, vards, uzvards)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Ieraksts veiksmīgi atjaunināts")
            elif ch == 7:
                break
            else:
                print("Nederīga izvēle !!!\n")

def main():
        intro()
        while True:
            print("\nMAIN MENU ")
            print("1. PIEVIENOT DARBINIEKU")
            print("2. MEKLĒT DARBINIEKU")
            print("3. IZDZĒST DARBINIEKU")
            print("4. MODIFICĒT IERAKSTU")
            print("5. APRĒĶINA ALGAS")
            print("6. Iziet")
            print()
            ch = int(input("Select Your Option (1-6): "))
            print()
            if ch == 1:
                print("PIEVIENOT DARBINIEKU")
                create_record()
            elif ch == 2:
                print("MEKLĒT DARBINIEKU")
                vards_uzvards = input("Ierakstiet vārdu un uzvārdu (atdalot ar atstarpi): ")
                search(vards_uzvards)
                return_to_menu = input("Nospiedier ENTER lai atgrieztos uz izvēlni...")
                if not return_to_menu:
                    continue
            elif ch == 3:
                print("IZDZĒST DARBINIEKU")
                vards_uzvards = input("Ierakstiet vārdu un uzvārdu (atdalot ar atstarpi):")
                delete_record(*vards_uzvards.split())
                print("Nospiediet ENTER lai atgrieztos uz izvēlni...")
                input()
            elif ch == 4: 
                print("Modificēt ierakstu")
                vards_uzvards = input("Ierakstiet vārdu un uzvārdu (atdalot ar atstarpi):")
                modify_record(*vards_uzvards.split())
            elif ch == 5:
                print("APRĒĶINA ALGAS")
                x = float(input("Ievadi stundas likmi "))
                y = float(input("Ievadi nostrādātās darba stundas "))
                z = x*y #aprēķina bruto algu
                soc=10.5/100*z #aprēķina sociālo nodokli
                b = int(input("Ievadiet apgādājamo(bērnu) skaitu "))
                atv = b*250 #atvieglojums par apgādājamo
                apl = z-soc-atv-82.14 #Ar iedzīvotāju ienākuma nodokli apliekamā summa
                ien = 20/100*apl #no 20%
                neto = z-soc-ien
                g = round(neto, 2)
                print("Jūsu bruto alga ir", z, "€" )
                print("Jūsu neto alga ir", g, "€" )
            elif ch == 6:
                print("Iziet")
                db.close()
                break
            else:
                print("Nederīga izvēle")
main()