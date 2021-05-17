import sqlite3



def create_database():
    connectDB = sqlite3.connect('revenue_table.db')
    cursorDB = connectDB.cursor()
    cursorDB.execute(f"""CREATE TABLE IF NOT EXISTS object (
            name text,
            amount INTEGER,
            currency text,
            kind text,
            description text,
            category text,
            date text
        )""")

    connectDB.commit()
    connectDB.close()




def add_to_database(name, amount, currency, kind, description, date):
    category = ''
    
    connectDB = sqlite3.connect('revenue_table.db')
    cursorDB = connectDB.cursor()
    cursorDB.execute("INSERT INTO object VALUES (?,?,?,?,?,?,?)", (name, amount, currency, kind, description, category, date))
    connectDB.commit()
    connectDB.close() 

def delete_from_database(row_id):
    connectDB = sqlite3.connect('revenue_table.db')
    cursorDB = connectDB.cursor()
    #cursorDB.execute("SELECT rowid, * FROM object")
    #data = cursorUser.fetchall()
    cursorDB.execute(f"DELETE FROM object WHERE rowid = {row_id}")
    connectDB.commit()
    connectDB.close()




def update_from_database(row_id, name, amount, currency, kind, description, date):
    connectDB = sqlite3.connect('revenue_table.db')
    cursorDB = connectDB.cursor()  
    
    cursorDB.execute(f"""
    UPDATE object
    SET name = '{name}',
        amount = '{amount}',
        currency = '{currency}',
        kind = '{kind}',
        description = '{description}',
        date = '{date}'
    WHERE rowid = {row_id};
    """) 
    connectDB.commit()
    connectDB.close()



def load_database():
    connectDB = sqlite3.connect('revenue_table.db')
    cousorDB = connectDB.cursor()
    cousorDB.execute("SELECT rowid, * FROM object")
    data = cousorDB.fetchall()
    revenue_list = []
    for revenue in data:
        object = {
            'id': revenue[0],
            'name': revenue[1],
            'amount': revenue[2],
            'currency': revenue[3],
            'kind': revenue[4],
            'description': revenue[5],
            'category': revenue[6],
            'date': revenue[7]
        }
        revenue_list.append(object)
    return revenue_list



def balance_counter(revenue_list):
    balance = 0
    income = 0
    outcome = 0
    for revenue in revenue_list:
        if revenue['kind'] == 'income':
            try:
                income = income+revenue['amount']
                balance = balance+revenue['amount']
            except:
                income = income+0
                balance = balance+0
        elif revenue['kind'] == 'outcome':
            try:
                outcome = outcome+revenue['amount']
                balance = balance-revenue['amount']
            except:
                income = income+0
                balance = balance-0
    balance_info = {
        'balance': balance,
        'income': income,
        'outcome': outcome
    }
    return balance_info


def sort_through_date(revenue_list):
    final_revenue_list =  sorted(revenue_list, key=lambda k: k['date'], reverse=True) 
    return final_revenue_list
