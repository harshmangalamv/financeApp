# Harsh Mangalam Verma

import sqlite3
import database as db
# connect to database
conn = sqlite3.connect('table.db')

# c for cursor
c = conn.cursor()
db.createTable()

# db.current_balance()
# exit()
flag = 1
while flag == 1:
    date = "0"
    date = input("Please enter the date in dd-mm-yyyy format:\t")
    income = 0 
    flag1 = input("Please enter y if your account got credited today\t")
    if flag1.upper() == 'Y':
        income = input("Enter the credited money value\t")
    exp_groc = 0; exp_rent = 0; exp_health=0; exp_others=0

    flag1 = input("Please enter y if you bought groceries today\t")
    if flag1.upper() == 'Y':
        exp_groc = input("Enter the amount spent on groceries\t")

    flag1 = input("Please enter y if you paid rent today\t")
    if flag1.upper() == 'Y':
        exp_rent = input("Enter the rent paid\t")
        
    flag1 = input("Please enter y if you spent money on health today\t")
    if flag1.upper() == 'Y':
        exp_health = input("Enter the spent money on health\t")

    flag1 = input("Please enter y if spent money on other things\t")
    if flag1.upper() == 'Y':
        exp_others = input("Enter the spen money\t")
    
    if date != "0":
        db.add_record(date, income, exp_groc, exp_rent, exp_health, exp_others)

    flag1 = input("Do you wish to add more data:[y/n]?\t")
    print(flag1.upper())
    if flag1.upper() != 'Y':
        flag = int(0)
        
flag = 1
expense_type = ["expense_groceries", "expense_rent", "expense_health", "expense_others"]
mOrY = ["month", "year"]
while flag == 1:
    time_val = int(0); year_val = int(0)
    print(time_val)
    expense_category = int(input("Input the option number corressponding to expense type:\n 1. Groceries\t 2. Rent\t 3. Health\t 4. Others\t 5. All\n"))
    year_val = input("Input the year:\t")
    time = int(input("Choose category: 1. Monthly\t 2. Yearly\t"))

    if time == 1:
        time_val = input("Input the month (viz 01 for Jan, 02 for Feb):\t")
    else:
        time_val = year_val

    if expense_category != 5:
        db.expense_detail_specific_element(expense_type[expense_category-1], f"{mOrY[time-1]}", f"{time_val}", f"{year_val}")
    else:
        # for gives detail of expenses on all kinds of expenes
        db.expense_detail(f"{mOrY[time-1]}", f"{time_val}", f"{year_val}")

    flag1 = input("Do you wish to repeat for other data:[y/n]?\t")
    if flag1.upper() == 'N':
        flag = int(0)

flag_bal = 0
flag_bal = int(input("Want to know the current balance? 1.Yes\t 2.No\t"))
if flag_bal == 1:
    db.current_balance()