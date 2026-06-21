import mysql.connector as med

# Database connection
mydb = med.connect(
    host='localhost',
    user='root',
    password='ies',
    database='pharmacy'
)
mycursor = mydb.cursor()


def add():
    no = int(input("How many medicines to add?: "))
    for i in range(no):
        m = int(input("Enter medicine ID: "))
        s = input("Enter medicine name: ")
        l = int(input("Enter count: "))
        n = input("Enter disease name: ")
        p = float(input("Enter price: "))
        md = input("Enter manufacturing date (YYYY-MM-DD): ")
        ed = input("Enter expiry date (YYYY-MM-DD): ")

        # SECURE: Using parameterized query to prevent SQL Injection
        q = "INSERT INTO medicines (M_ID, M_NAME, COUNT, DISEASE, PRICE, MFG_DATE, EXP_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(q, (m, s, l, n, p, md, ed))
        mydb.commit()
        print("Medicine record added successfully.")


def search1():
    di = input("Enter name of disease: ")
    w = "SELECT * FROM medicines WHERE DISEASE = %s"
    mycursor.execute(w, (di,))
    fe = mycursor.fetchall()
    if fe:
        for i in fe:
            print(i)
    else:
        print("No records found.")


def search2():
    di = int(input("Enter medicine ID: "))
    w = "SELECT * FROM medicines WHERE M_ID = %s"
    mycursor.execute(w, (di,))
    fe = mycursor.fetchall()
    if fe:
        for i in fe:
            print(i)
    else:
        print("No records found.")


def search3():
    di = int(input("Enter count: "))
    w = "SELECT * FROM medicines WHERE COUNT = %s"
    mycursor.execute(w, (di,))
    fe = mycursor.fetchall()
    if fe:
        for i in fe:
            print(i)
    else:
        print("No records found.")


def update1():
    pr = float(input("Enter new price: "))
    di = int(input("Enter M_ID: "))
    w = "UPDATE medicines SET PRICE = %s WHERE M_ID = %s"
    mycursor.execute(w, (pr, di))
    mydb.commit()
    print("Price updated successfully.")


def update2():
    pr = int(input("Enter new count: "))
    di = int(input("Enter M_ID: "))
    w = "UPDATE medicines SET COUNT = %s WHERE M_ID = %s"
    mycursor.execute(w, (pr, di))
    mydb.commit()
    print("Count updated successfully.")


def delete():
    id1 = int(input("Enter the medicine ID to delete: "))
    w = "DELETE FROM medicines WHERE M_ID = %s"
    mycursor.execute(w, (id1,))
    mydb.commit()
    print("Record deleted successfully.")


# Main menu
print("WELCOME TO MEDI DATA - PHARMACY MANAGEMENT SYSTEM")
print("Developed by: Jiya Rajiv, Thrisha M.V, Malavika P.J")
print("-" * 50)

c = 'yes'
while c == 'yes':
    print("\n1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        print("Search by:")
        print("  1. Disease")
        print("  2. Medicine ID")
        print("  3. Count")
        schoice = int(input("Enter your choice: "))
        if schoice == 1:
            search1()
        elif schoice == 2:
            search2()
        else:
            search3()

    elif choice == 3:
        print("Update:")
        print("  1. Price")
        print("  2. Count")
        uchoice = int(input("Enter your choice: "))
        if uchoice == 1:
            update1()
        else:
            update2()

    elif choice == 4:
        delete()

    else:
        print("Invalid input. Please enter 1-4.")

    c = input("\nDo you want to continue? (yes/no): ").strip().lower()

print("Thank you for using MEDI DATA!")
