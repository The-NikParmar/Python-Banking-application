# Connect to MySQL database
import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="root",database="banking")
mycursor=mydb.cursor()

class Customers:
    def customer_register(self):  # Method to register a new customer
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Register Customer>>>>>>>>>>>>>>>>>>>>>>")
        c_name = input("Enter customer name: ")
        c_ac_no = input("Enter account number: ")
        c_mobile_no = input("Enter mobile number: ")
        c_address = input("Enter address: ")
        c_balance = int(input("Enter initial balance: "))
        c_password = input("Enter your password")

        # Insert customer data into the database
        sql_insert_customer = "INSERT INTO customers (c_name, c_ac_no, c_mobile_no, c_address, c_balance, c_password)VALUES (%s, %s, %s, %s, %s, %s)"
        values = (c_name, c_ac_no, c_mobile_no, c_address, c_balance,c_password)
        mycursor.execute(sql_insert_customer, values)
        mydb.commit()

        print("Customer registration successful.")

    def customer_login(self):    # Method to handle customer login
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Customer Login >>>>>>>>>>>>>>>>>>>>>>>>>")
        c_ac_no = input("Enter account number: ")
        c_password = input("Enter password: ")

        # Check if the customer exists in the database
        sql_check_customer = "SELECT * FROM customers WHERE c_ac_no = %s AND c_password = %s"
        mycursor.execute(sql_check_customer, (c_ac_no, c_password))
        customer = mycursor.fetchone()

        if customer:
            print("Customer login successful.")
            
        else:
            print("Invalid account number or password.")

    def customer_withdraw(self):  # Method to handle customer withdrawal

        print(">>>>>>>>>>>>>>>>>>>>>>>>> Customer Withdrawal >>>>>>>>>>>>>>>>>>>>>>>>>")
        c_ac_no = input("Enter customer account number: ")
        withdraw_amount = int(input("Enter amount to withdraw: "))

        # Check if the customer exists in the database
        sql_check_customer = "SELECT * FROM customers WHERE c_ac_no = %s"
        mycursor.execute(sql_check_customer, (c_ac_no,))
        customer = mycursor.fetchone()

        if customer:
            c_balance = customer[5]  
            if c_balance >= withdraw_amount:
                new_balance = c_balance - withdraw_amount

                # Update customer's balance in the database
                sql_update_balance = "UPDATE customers SET c_balance = %s WHERE c_ac_no = %s"
                mycursor.execute(sql_update_balance, (new_balance, c_ac_no))
                mydb.commit()
                print(f"Withdrawal of {withdraw_amount} successful. New balance: {new_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Customer not found.")

    def customer_deposit(self):    # Method to handle customer deposit
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Customer Deposit >>>>>>>>>>>>>>>>>>>>>>>>>")
        c_ac_no = input("Enter customer account number: ")
        deposit_amount = int(input("Enter amount to deposit: "))

        # Check if the customer exists in the database
        sql_check_customer = "SELECT * FROM customers WHERE c_ac_no = %s"
        mycursor.execute(sql_check_customer, (c_ac_no,))
        customer = mycursor.fetchone()

        if customer:
            c_balance = customer[5]  
            new_balance = c_balance + deposit_amount
            # Update customer's balance in the database
            sql_update_balance = "UPDATE customers SET c_balance = %s WHERE c_ac_no = %s"
            mycursor.execute(sql_update_balance, (new_balance, c_ac_no))
            mydb.commit()
            print(f"Deposit of {deposit_amount} successful. New balance: {new_balance}")
        else:
            print("Customer not found.")

    def __customer_view_balance(self):   # Method to view customer balance (private method)
        print(">>>>>>>>>>>>>>>>>>>>>>>>> View Customer Balance >>>>>>>>>>>>>>>>>>>>>>>>>")
        c_ac_no = input("Enter customer account number: ")

        sql_check_customer = "SELECT * FROM customers WHERE c_ac_no = %s"
        mycursor.execute(sql_check_customer, (c_ac_no,))
        customer = mycursor.fetchone()

        if customer:
            c_balance = customer[5]
            print(f"Customer balance: {c_balance}")
        else:
            print("Customer not found.")

