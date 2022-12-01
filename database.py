import sqlite3
import re

expense_type = ["expense_groceries", "expense_rent", "expense_health", "expense_others"]
month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# this function creates table in database
def createTable():
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    c.execute(
        """
            CREATE TABLE IF NOT EXISTS detail(
            date VARCHAR(10),
            income INTEGER,
            expense_groceries INTEGER,
            expense_rent INTEGER,
            expense_health INTEGER,
            expense_others INTEGER
            )
        """
    )

    conn.commit()
    conn.close()

    print("Table is created successfully!")

# this function adds records (row-wise) in table
def add_record(date, income, expense_groceries, expense_rent, expense_health, expense_others):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    c.execute(
        f"INSERT INTO detail VALUES (?, ?, ?, ?, ?, ?)", (date, income, expense_groceries, expense_rent, expense_health, expense_others)
    )
    
    conn.commit()
    conn.close()

    print("The record is added successfully!")

# this function is a feature that gives details of expenses of a particular type 
def expense_detail_specific_element(grocery, time, time_value, year):
    conn = sqlite3.connect('table.db')
    c = conn.cursor() 

    expense = 0

    if time == 'month':
        c.execute(f"SELECT {grocery}, date FROM detail")
        for value in c:
            if value[1][3:5] == time_value and value[1][6:10]==year:        # value[0] is expence for particular expense_type
                                                                            # value[1] is corresponding date string
                expense += value[0]
    elif time == 'year':
        c.execute(f"SELECT {grocery}, date FROM detail")
        for value in c:
            if value[1][6:10] == time_value:
                expense += value[0]
  
    if time == 'month':
        print(f"Total expense on {grocery} for {time_value} month is: ", expense, ".")
    else:
        print(f"Total expense on {grocery} for {time_value} year is: ", expense, ".")  

    return expense

# this feature would result in details of expenses of a given year or a particular month of a year
# time -> [year or month], time_value -> [year value or month number ie 01 for January], year_value -> [year in case when query is for month]
def expense_detail(time, time_value, year_val):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    expense = 0

    if time == 'month':
        for exp in expense_type:
            expense += expense_detail_specific_element(exp, time, time_value, year_val) # call to expense_detail_specific_element function \
                                                                                        # for every kind of expense
    
    else:
        for month in month_list:
            # print("currently at ", month)
            for exp in expense_type:
                expense += expense_detail_specific_element(exp, "month", month, year_val)   # for every month, expense_detail_specific_element 
                                                                                            # is called expense category wise
    
    if time == "month":
        print(f"Total expense of {time_value} month is: ", expense, ".")
    else:
        print(f"Total expense in year {time_value} is: ", expense, ".")

# this describes the current balance
def current_balance():
    balance = 0
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    c.execute(
        "SELECT income FROM detail"
    )
    for val in c:
        balance += val[0]

    for exp in expense_type:
        c.execute(
            f"SELECT {exp} FROM detail"
        )
        for val in c:
            balance -= val[0]
        
    print("Current balance is: ", balance, ".")