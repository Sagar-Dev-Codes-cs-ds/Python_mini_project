from operations import get_all_expenses, add_expense_db, delete_expense_db,amount_sum_expense_db, show_graph_day, show_graph_month
from expense import Expense

def add_expense():
    name=input("Enter name : ")
    amount=float(input("Enter amount : "))
    category=input("Enter category : ")
    description=input("Enter description : ")

    expense=Expense(name,amount,category,description)
    add_expense_db(expense)

def view_expense():
    data=get_all_expenses()
    if not data:
        print("No expenses found.")
    for i in data:
        print(f"{"-"*30}\n{i['id']}. {i['date']}\nname : {i['name']}\nCategory : {i['category']}\nDescription : {i['description']}\nAmount : {i['amount']}")

def delete_expenses():
    id=int(input("Enter the id of the expense : "))
    delete_expense_db(id)
def amount_sum_expense():
    print("Total amount : ",amount_sum_expense_db())

def show_analytics():
    ch=int(input(" For monthly analysis press '1' , for day wise analysis press '2' "))
    if ch==1 :
        show_graph_month()
    elif ch==2 :
        show_graph_day()
    else:
        print("Invalid input")

def main():
    while True:
        print("-"*30,"\nPersonel expense tracker\n","-"*30,"\n1. Add Expenses\n2. View Expenses\n3.Sum of expenses\n4.Delete expense\n5. Exit from program\n6. Show analysis")
        choice=input("Enter your choice 1 2 3 4 5 6 : ")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expense()
        elif choice=="3":
            amount_sum_expense()
        elif choice=="4":
            delete_expenses()
        elif choice=="5":
            break
        elif choice=="6":
            show_analytics()
        else:
            print("Invalid input!\n Please try again")
if __name__=="__main__":
    main()
