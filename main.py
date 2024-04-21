

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

# Main Banking System Loop
while True:
print ('Hello User')
print ('Are you a new or current user?')
w = input()
if w == 'new':
    print('Please create a new account')

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
    print("Thank you for using our bank's services, have a good day.")
    break
elif z == '':
    print("That is not an option, please type either 1, 2, 3, or 4.")