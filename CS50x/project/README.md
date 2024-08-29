# CS50 Bank
[Video Demo](https://youtu.be/uNv2XJx0K2o)


## Description
This bank website that allow users to deposit, withdraw, and transfer money to other accounts on the same website, and view their transaction record.



## Usage
### Register

Register an account in our bank by filling your name, username, and password.
The password must be at least 8 letters, including minimum one uppercase, lowercase and number.

![Register](static/register.JPG)

### Login
Login by inputting the corresponding username and password.

![Login](static/login.JPG)

### Error
If user failed to enter the correct username or password, or if user encounter other errors, an apology page will be returned as followed.

![Apology](static/apology.JPG)

### Account overview
The account overview shows the user their bank account number, current cash balance and their transaction history. Users can also see the bank account of the giver and receiver so that they know more about the details of transfer.

![Account Overview](static/overview.JPG)

### Deposit
Users can deposit any amount of money into your account under the deposit page.

![Deposit](static/deposit.JPG)

### Withdraw
Users can withdraw money from their account under the withdraw page, using either the dragbar to a direct input. The dragbar gives a clearer representation on how much money they can withdraw.

![Withdraw](static/withdraw.JPG)

### Transfer
Users can transfer a certain amount of money to other users using the transferee's bank account.

![Transfer](static/transfer.JPG)

After entering the bank account and the amount, the user will be directed to a confirmation page showing given some masked information of the receiver, this allows the user to confirm whether they are transferring to the right person.

![Confirm](static/confirm.JPG)


## Problem encountered
1. Setting up a well-designed database in SQLite to present the account summary
2. Synchronizing the scrolling bar in the withdrawl page with the input box
3. Positioning the html elements in the corresponding position
4. Masking user's info in the transfer confirmation page

## New skills
1. Joining tables in SQLite using made up aliases
2. Tried to use some simple algorithm to calculate the number of letters needed to mask in the user's name to protect the privacy


## Languages
1. Python
2. Javascript
3. HTML
4. CSS
5. SQLite
6. Frameworks: Bootstrap, Flask


## Possible improvements
The website can provide some investment service like buying stock or insurance, or allows the deposit of different currency, making the deposit and withdrawl function more "useful" as the account balance could be used in elsewhere other than transferal.

A export function can also be implemented to allow users export the transaction history as a pdf file, similar to the bank statement in real life.

With the implementation of stock or foreign currency, we can then design a pie chart to present to the user their account summary, for example 70% of their account total is cash that can be withdrawed immediately, while 30% are stock, or other charts representing the respecting currency in their account.

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
