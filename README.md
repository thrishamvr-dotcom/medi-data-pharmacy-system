# 💊 MEDI DATA — Pharmacy Management System

A Python + MySQL based pharmacy record management system built as a Class XII Computer Science project.  
Developed by **Thrisha M.V, Jiya Rajiv, Malavika P.J** | IES Public School, Chittilappilly, Thrissur

---

## 📌 Project Overview

MEDI DATA is a command-line application that helps pharmacies manage medicine inventory efficiently. It replaces manual record-keeping with a simple, menu-driven interface connected to a MySQL database.

---

## ⚙️ Features

- ➕ **Add** new medicine records (ID, name, count, disease, price, MFG & EXP dates)
- 🔍 **Search** medicines by disease name, medicine ID, or stock count
- ✏️ **Update** medicine price or stock count by ID
- 🗑️ **Delete** medicine records by ID
- 🔁 **Loop menu** — continue operations until user exits

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Frontend  | Python 3.x (CLI)        |
| Backend   | MySQL 8.0               |
| Connector | mysql-connector-python  |

---

## 🗃️ Database Schema

**Table: `medicines`**

| Field     | Type         |
|-----------|--------------|
| M_ID      | INT          |
| M_NAME    | VARCHAR(25)  |
| COUNT     | INT          |
| DISEASE   | VARCHAR(25)  |
| PRICE     | FLOAT        |
| MFG_DATE  | DATE         |
| EXP_DATE  | DATE         |

---

## 🚀 How to Run

### Prerequisites
- Python 3.x
- MySQL Server
- mysql-connector-python (`pip install mysql-connector-python`)

### Setup
```bash
# 1. Clone the repository
git clone https://github.com/thrishamvr-dotcom/medi-data-pharmacy-system.git

# 2. Create the database in MySQL
CREATE DATABASE pharmacy;
USE pharmacy;
CREATE TABLE medicines (
    M_ID INT,
    M_NAME VARCHAR(25),
    COUNT INT,
    DISEASE VARCHAR(25),
    PRICE FLOAT,
    MFG_DATE DATE,
    EXP_DATE DATE
);

# 3. Update credentials in medidata.py
# Change host, user, password to match your MySQL setup

# 4. Run the program
python medidata.py
```

---

## 🔐 Security Note — What I Learned

After completing the Offenso Academy ethical hacking course, I revisited this project and identified a **SQL Injection vulnerability** in the `add()` function.

**Vulnerable code (original):**
```python
q = "insert into medicines(M_ID, M_NAME, ...) values({}, '{}', ...)".format(m, s, ...)
mycursor.execute(q)
```
String formatting directly into SQL queries allows an attacker to inject malicious SQL code.

**Secure fix (parameterized query):**
```python
q = "INSERT INTO medicines (M_ID, M_NAME, COUNT, DISEASE, PRICE, MFG_DATE, EXP_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
mycursor.execute(q, (m, s, l, n, p, md, ed))
```
The `search` functions in the original code already used parameterized queries (`%s`) correctly — showing that consistency in secure coding matters across all functions, not just some.

This real-world discovery from my own project helped me understand **why secure coding practices matter**, not just in theory but in code I personally wrote.

---

## 📸 Sample Output

```
WELCOME TO OUR PROJECT BY JIYA RAJIV, THRISHA MV, MALAVIKA PJ
1. add
2. search
3. update
4. delete
Enter your choice: 2
  1. disease
  2. ID
  3. count
Enter any number: 1
Enter name of disease: fever
(1, 'dolo', 57, 'fever', 22.4, datetime.date(2025, 8, 25), datetime.date(2027, 8, 22))
(2, 'paracetamol', 23, 'fever', 25.5, datetime.date(2024, 10, 22), datetime.date(2024, 10, 21))
```

---

## 📚 What This Project Taught Us

- Connecting Python with MySQL using `mysql.connector`
- Designing relational database schemas
- Writing CRUD operations with SQL
- Input validation and menu-driven program design
- **Post-project:** Identifying and fixing SQL injection vulnerabilities

---

## 👩‍💻 Author

**Thrisha M.V**  
Cybersecurity enthusiast | TryHackMe: [Thrishaahh](https://tryhackme.com/p/Thrishaahh) | Top 40%  
GitHub: [thrishamvr-dotcom](https://github.com/thrishamvr-dotcom)
