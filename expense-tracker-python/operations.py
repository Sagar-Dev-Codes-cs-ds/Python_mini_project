from db import get_connection
import matplotlib.pyplot as plt
def add_expense_db(expense):
    conn=get_connection()
    cursor=conn.cursor()
    query="""INSERT INTO expenses (name,amount,category,description,date) VALUES (%s,%s,%s,%s,%s)"""
    values=(expense.name,expense.amount,expense.category,expense.description,expense.date)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
def get_all_expenses():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM expenses")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def delete_expense_db(id):
    conn=get_connection()
    cursor=conn.cursor()
    query="""DELETE FROM expenses WHERE id=%s"""
    try:
        cursor.execute(query,(id,))
        conn.commit()
        if cursor.rowcount==0:
            print("ID not found")
        else:
            print("Expense deleted")
    except Exception as e:
        print("Database error: ",e)
    finally:        
        cursor.close()
        conn.close()

def amount_sum_expense_db():
    conn=get_connection()
    cursor=conn.cursor()
    query="""SELECT SUM(amount) FROM expenses"""
    try:
        cursor.execute(query)
        result=cursor.fetchone()
        total=result[0] if result[0] is not None else 0
        return total
    except Exception as e:
        print("Database error: ",e)
        return 0
    finally:
        cursor.close()
        conn.close()

def show_graph_day():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT date , SUM(amount) AS monthly_amount FROM expenses GROUP BY date";
    cursor.execute(query)
    data=cursor.fetchall()
    date=[]
    amount=[]
    for i in data:
        date.append(i[0])
        amount.append(i[1])
    plt.plot(date,amount)
    plt.title("Total expenses per day")
    plt.xlabel("date")
    plt.ylabel("Amount")
    plt.show()
    cursor.close()
    conn.close()
def show_graph_month():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT MONTH(date) as month, sum(amount) AS monthly_amount FROM expenses GROUP BY MONTH(date)";
    cursor.execute(query)
    data=cursor.fetchall()
    months={
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    date=[]
    amount=[]
    for i in data:
        date.append(months[i[0]])
        amount.append(i[1])
    plt.plot(date,amount)
    plt.title("Total expenses per month")
    plt.xlabel("Months")
    plt.ylabel("Amount")
    plt.show()
    cursor.close()
    conn.close()
