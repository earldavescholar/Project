import variables

def bank():
  buy = 'a'
  while buy == 'a':
    print("\nBank Balance:", variables.balance)
    print("\na. Deposit")
    print("b. Withdraw")
    print("c. Back")
    while True:
      bankInput = input()
      if bankInput.lower() == 'a':
          deposit = int(input("Enter Amount to Deposit: "))
          if deposit <= variables.gold:
              variables.balance = deposit + variables.balance
              variables.gold -= deposit
              print("You've just deposited", deposit, "gold")
              break
          else:
              print("Not enough money!")
      elif bankInput.lower() == 'b':
        withdraw = int(input("Enter Amount to Withdraw: "))
        if withdraw <= variables.balance:
          variables.gold += withdraw
          variables.balance -= withdraw
          print("You've just withdrawed", withdraw, "gold")
          break
      elif bankInput.lower() == 'c':
        buy = 'b'
        break
      else:
        print("Not in the Choices! Try again!")
        
      x = False