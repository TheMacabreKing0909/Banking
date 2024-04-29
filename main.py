import mysql.connector



connection = mysql.connector.connect(user = 'username', database = 'Local2', password = 'password')


cursor = connection.cursor()
connection.close()

def check_balance(account_number):
  """
  This function checks the balance of the given account number.
  """
  cursor.execute(f"SELECT balance FROM accounts WHERE account_number = {account_number}")
  balance = cursor.fetchone()[0]
  print(f"Your account balance is ${balance:.2f}")

def deposit(account_number, amount):
  """
  This function deposits the given amount into the given account number.
  """
  cursor.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE account_number = {account_number}")
  connection.commit()
  print(f"You have deposited ${amount:.2f} into your account.")

def withdraw(account_number, amount):
  """
  This function withdraws the given amount from the given account number.
  """
  cursor.execute(f"SELECT balance FROM accounts WHERE account_number = {account_number}")
  balance = cursor.fetchone()[0]
  if amount > balance:
      print("Insufficient funds.")
  else:
      cursor.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account_number = {account_number}")
      connection.commit()
      print(f"You have withdrawn ${amount:.2f} from your account.")

# Main Banking System

print("Welcome to the Banking System!")
# Create a new account
while True:
  print ('Hello User')
  print ('Are you a new or current user?')
  w = input()
  if w == 'new':
    print('Please create a new account')
    print('Please enter your name')
    name = input()
    print('Please enter your age')
    age = input()
    print('Please enter your address')
    address = input()
    print('Please enter your phone number')
    phone = input()
    print('Please enter your email address')
    email = input()
    print('Please enter your password')
    password = input()
    print('Please enter your account number')
    account_number = input()
    print('Please enter your initial deposit')
    initial_deposit = input()
    cursor.execute(f"INSERT INTO accounts (name, age, address, phone, email, password, account_number, initial_deposit) VALUES ('{name}', {age}, '{address}', '{phone}', '{email}', '{password}', {account_number}, {initial_deposit}")
    connection.commit()
    print('Account created successfully!')
# Already have an account in backing system
  elif w == 'current':
      print('Enter your name:')
      x = input()
  print('Hello ' + x)
  print('Please enter you account pin')
  y = input()
  print('You are now logged in ' + x)
  print('How may I help you today ' + x)
  print('1: Check Balance'
        '2: Deposit'
        '3: Withdraw'
        '4: Sign Out')
  z = input()
  if z == '1':
      print("You've selected Check Balance")
  elif z == '2':
      print("You've selected Deposit")
  elif z == '3':
      print("You've selected Withdraw")
  elif z == '4':
      print("Thank you for using our bank's services, have a good  day.")
      break
  elif z == '':
      print("Invalid input. Please try again.")