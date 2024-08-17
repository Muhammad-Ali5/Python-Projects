ATM Simulation Program
This Python program simulates a simple ATM (Automated Teller Machine) system where a user can check their balance, withdraw money, or deposit money. The transactions are logged into a file named atm.txt.

Features
Check Balance: Displays the current account balance.
Withdraw Money: Allows the user to withdraw money if they have sufficient funds.
Deposit Money: Allows the user to deposit money into their account.
User Information: Records the user's name in the transaction log.
How to Use
Run the Program: Execute the script to start the ATM simulation.

Password Authentication: The program requires a password to access the ATM functions. The default password is 1234.

Choose an Operation:

Press 1 to check your balance.
Press 2 to withdraw money.
Press 3 to deposit money.
Transaction Logging: All transactions and operations are logged into the atm.txt file.

Code Overview
c_balance = 30000: The initial balance in the account is set to 30,000.
password = 1234: The default password to access the ATM functions.
checkBalance(): Displays and logs the current balance.
widthrawBalance(): Handles money withdrawal and logs the transaction.
depositeBalance(): Handles money deposit and logs the transaction.
user_information(): Records the user's name in the log.
main(): The main function that drives the ATM operations.
Log File
All user interactions and transactions are stored in atm.txt with details like balance checks, withdrawals, deposits, and user names.

Example Usage
markdown
Copy code
==Welcome To Khyber Bank==
Enter your password : 1234
=================================
=> Press 1. Check Balance     ...
=> Press 2. Widthraw Balance  ...
=> Press 3. Deposite Balance  ...
=================================
==> Enter Your Choice : 1
Your current Balance is : 30000
Notes
Ensure the password is kept secure.
The program currently uses a global variable for balance, which is not ideal for production-level code but sufficient for this simulation.
The file atm.txt will be created or appended to in the same directory as the script.
