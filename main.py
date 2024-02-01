from banker import Banker

#=========================================Banker  Menu ====================================================================
bank = '''
         >>>>>>>>>>>>>>>>>>>>>>>>> Banker Menu >>>>>>>>>>>>>>>>>>>>>>>>>
            1. Register
            2. Login
            3. Update Customer
            4. View All Customers
            5. Delete Customer
            6. Exit
'''

#=========================================Customer  Menu ====================================================================
customer = '''
        >>>>>>>>>>>>>>>>>>>>>>>>> Customer Menu >>>>>>>>>>>>>>>>>>>>>>>>>
            1. Register
            2. Login
            3. Withdraw Amount
            4. Deposit amount
            5. view balance
            6. Exit
'''

#=========================================User type  Menu ====================================================================
menu = '''
        >>>>>>>>Select Usertype >>>>>>>>>>
                       1.Banker
                       2.Customer
'''
print(menu)
b1 = Banker()


choice = input("Enter your choice: ")

if choice == '1':
        while True:
            print(bank)
            choice2 = input("Enter your Choice: ")

            if choice2 == '1':
                b1.register()
            elif choice2 == '2':
                b1.login()
            elif choice2 == '3':
                b1.update_customers()
            elif choice2 == '4':
                b1.view_all_customers()
            elif choice2 == '5':
                b1.delete_customer()
            elif choice2 == '6':
                exit()
            else:
                print("Invalid choice. Please try again.")
                
            conti = input("Do you want to continue? (Y/N): ")
            if conti != 'y':
                break
            else:
                exit()
            
elif choice == '2':
        while True:
            print(customer)
            choice3 = input("Enter your choice: ")

            if choice3 == '1':
                b1.customer_register()
            elif choice3 == '2':
                b1.customer_login()
            elif choice3 == '3':
                b1.customer_withdraw()
            elif choice3 == '4':
                b1.customer_deposit()
            elif choice3 == '5':
                b1._Customers__customer_view_balance()
            elif choice3 == '6':
                exit()
            else:
                print("Invalid choice. Please try again.")
                
            conti = input("Do you want to continue? (Y/N): ")
            if conti != 'y':
                break
            else:
                exit()

else:
        print("Invalid selection. Please select 1 or 2.")
