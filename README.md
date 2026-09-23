# Mini Banking System

## Project Overview

Mini Banking System is a command-line based banking application developed using Python. It allows users to create an account,  log in using a PIN, manage their balance, do transactions, and view their account information.

The project shows the use of Python programming concepts such as functions, conditional statements, loops, exception handling, file handling, JSON data storage, hashing, and modular programming.

## Features

- Create a bank account
- Generate and valid an 8-digit account number
- Set a 4-digit PIN
- Securely store PINs using SHA-256 hashing
- User login and authentication
- Check account balance
- Depositing money
- Withdrawing money
- Transfering money between different accounts
- View transaction histor of user
- View account details
- Logout from the banking system
- Store account information using JSON storage
- Input validation and error correction

## Technologies Used

- Programming Language: Python 3
- Data Storage: JSON
- Library used are: os, json, hashlib
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub

## Project Structure

```
minibankingsystem/
│
├── main.py
├── account.py
├── authentication.py
├── banking.py
├── storage.py
├── validation.py
├── accounts.json
├── README.md
└── statement.md
```

### Description of Modules

- **main.py** – Controls the main menu and connects the different modules.
- **account.py** – deals with account creation and information.
- **authentication.py** – deals user login and PIN verification.
- **banking.py** – deals with balance checking, deposits, withdrawals, transfers, transaction history, and account details.
- **storage.py** – Loads and saves account data using JSON storage.
- **validation.py** – Performs input validation for account numbers, PINs, and transaction amounts.
- **accounts.json** – Stores account informations and transactions data.

## Installation and Setup

**Step 1: Install Python**

Install Python 3 on your computer.

**Step 2: Download the Project**

download this GitHub repository to your computer.

**Step 3: Open the Project**

Open the project folder in Visual Studio Code .

**Step 4: Run the Program**

Open the terminal inside the project folder and run:

python main.py

## How to Use

When the program starts, the main menu provides three options:

1. **Create Account**
2. **Login**
3. **Exit**

After logging in successfully, the user can:

1. **Check Balance**
2. **Deposit Money**
3. **Withdraw Money**
4. **Transfer Money**
5. **View Transaction History**
6. **View Account Details**
7. **Logout**

## Testing

The project can be tested by performing the following operations:

- Create a new account with valid details.
- Try creating an account with an invalid account number.
- Try creating a duplicate account number.
- Try entering an invalid PIN.
- Log in using correct and incorrect credentials.
- Deposit a valid amount.
- Try depositing an invalid amount.
- Withdraw a valid amount.
- Try withdrawing more money than the available balance.
- Transfer money to another existing account.
- Try transferring money to the same account.
- Try transferring money to a non-existing account.
- Check transaction history after transactions.
- Check that account data remains available after restarting the program.

## Data Storage

The project uses a JSON file named "accounts.json" to store account information.

Sensitive PINs are not stored as plain text. The PIN entered during account creation is converted into a SHA-256 hash before being stored.

## Error Handling

The system handles common invalid inputs such as:

- Invalid account numbers
- Invalid PINs
- Invalid transaction amounts
- Non-numeric transaction input
- Insufficient account balance
- Duplicate account numbers
- Non-existing receiver accounts
- Transfers to the same account
- Invalid menu choices

## Future Enhancements

### Possible future improvements include:

- Adding an admin module
- Adding interest calculation
- Generating downloadable transaction statements
- Adding stronger authentication methods
- Adding a graphical user interface
- Moving from JSON storage to a database
