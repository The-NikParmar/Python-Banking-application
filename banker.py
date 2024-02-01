import pymysql
# Connect to MySQL database
mydb = pymysql.connect(host="localhost",user="root",password="root",database="banking")
mycursor=mydb.cursor()
from Customers import Customers  # Import the Customers class from the Customers module

# Define the Banker class, inheriting from the Customers class
class Banker(Customers):     # Method to register a new banker
    def register(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Register >>>>>>>>>>>>>>>>>>>>>>>>>")
        admin_name = input("Enter your name :- ")
        admin_password = input("Enter password:-")

        # Insert banker data into the database
        query = "INSERT INTO bankers (admin_name, admin_password) VALUES (%s, %s)"
        values = (admin_name, admin_password)
        mycursor.execute(query, values)
        mydb.commit()

        print(">>>>>>>>>>>>>>>>>> Admin registration done >>>>>>>>>>>>>>>>>")

    def login(self):     # Method to handle banker login
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Login")
        admin_name = input("Enter your name :- ")
        admin_password = input("Enter password:-")

        # Check if the banker exists in the database
        query = "SELECT * FROM bankers WHERE admin_name = %s AND admin_password = %s"
        values = (admin_name, admin_password)
        mycursor.execute(query, values)
        user = mycursor.fetchone()

        if user:
            print(">>>>>>>>>>>>>>>>>>> Admin login Success >>>>>>>>>>>>>>>>>>")
        else:
            print("Error:- Password or Name not match !!!!")

    def update_customers(self):    # Method to update customer details
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Update Customer Details ")
        c_ac_no = input("Enter customer account number: ")
        #  new customer details
        new_name = input("Enter new customer name: ")
        new_address = input("Enter new customer address: ")
        new_mobile_no = input("Enter new customer mobile number: ")

        # Update the customer details in the database
        query = "UPDATE customers SET c_name = %s, c_address = %s, c_mobile_no = %s WHERE c_ac_no = %s"
        values = (new_name, new_address, new_mobile_no, c_ac_no)
        mycursor.execute(query, values)
        mydb.commit()

        print("Customer details updated successfully.")

    def delete_customer(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Delete Customer >>>>>>>>>>>>>>>>>>>>>>>>>")
        c_ac_no = input("Enter customer account number to delete: ")

        # Check if the customer exists
        sql_check_customer = "SELECT * FROM customers WHERE c_ac_no = %s"
        mycursor.execute(sql_check_customer, (c_ac_no,))
        customer = mycursor.fetchone()

        if customer:
            confirmation = input("Are you sure you want to delete this customer? (Y/N): ")
            if confirmation == 'y' or confirmation == 'Y' :
                # Delete the customer from the database
                sql_delete_customer = "DELETE FROM customers WHERE c_ac_no = %s"
                mycursor.execute(sql_delete_customer, (c_ac_no,))
                mydb.commit()
                print("Customer deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print("Customer not found.")

    def view_all_customers(self):       # Method to view all customers
        print(">>>>>>>>>>>>>>>>>>>>>>>>> View All Customers >>>>>>>>>>>>>>>>>>>>>>>>>")
       
        mycursor.execute("SELECT * FROM customers")
        customers = mycursor.fetchall()

        if customers:
            print("Customer Details:")
            for customer in customers:
                print(f"Customer Name: {customer[1]}")
                print(f"Account Number: {customer[2]}")
                print(f"Mobile Number: {customer[3]}")
                print(f"Address: {customer[4]}")
                print(f"Balance: {customer[5]}")
                print("-------------------------------------")
        else:
            print("No customers found.")




