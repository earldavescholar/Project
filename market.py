import variables
from island import island

def marketx():
  buy = 'a'
  print("\n█▀▄▀█ ▄▀█ █▀█ █▄▀ █▀▀ ▀█▀\n█░▀░█ █▀█ █▀▄ █░█ ██▄ ░█░\n")
  print("Fish    -", variables.fishMarketPrice, "gold")
  print("Meat    -", variables.meatMarketPrice, "gold")
  print("Rum     -", variables.rumMarketPrice, "gold")
  print("Leather -", variables.leatherMarketPrice, "gold")
  print("Tobacco -", variables.tobaccoMarketPrice, "gold")
  print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  while buy == 'a':
    print("\na. Buy")
    print("b. Sell")
    print("c. Back")
    while True:
      marketInput = input()
      if marketInput == "a":
        buy_menu()
        break
      elif marketInput == "b":
        sell_inventory()
        break
      elif marketInput == "c":
        buy = 'b'
        break
      else:
        print("Not in the Choices. Try Again!\n")
        
def buy_menu():
        print("a. Buy Fish")
        print("b. Buy Meat")
        print("c. Buy Rum")
        print("d. Buy Leather")
        print("e. Buy Tobacco")
        print("f. Back")
        while True:
          buyInput = input().lower()
          if buyInput == "a":
            buyFish()
            break
          elif buyInput == "b":
            buyMeat()
            break
          elif buyInput == "c":
            buyRum()
            break
          elif buyInput == "d":
            buyLeather()
            break
          elif buyInput == "e":
            buyTobacco()
            break
          elif buyInput == 'f':
            break
          else:
            print("Not in the Choices. Try Again!\n")

def buyFish():
  while True:
    amountInput = int(input("Enter amount: "))
    if amountInput <= variables.storage:    
        totalPurchase = variables.fishMarketPrice * amountInput
        if totalPurchase > variables.gold:
            print("Not enough money! Try again")
        else:
            variables.gold = variables.gold - totalPurchase
            print("You've just purchased", amountInput, "Fish")
            variables.fishes = variables.fishes + amountInput
            variables.fishPrice = variables.fishMarketPrice 
            variables.storage -= amountInput
            break
    else:
        print("Not enough Storage! Try again")
      
def buyMeat():
  while True:
    amountInput = int(input("Enter amount: "))
    if amountInput <= variables.storage:
      totalPurchase = variables.meatMarketPrice * amountInput
      if totalPurchase > variables.gold:
          print("Not enough money!")
      else:
          variables.gold = variables.gold - totalPurchase
          print("You've just purchased", amountInput, "Meat")
          variables.meats = variables.meats + amountInput
          variables.meatPrice = variables.meatMarketPrice
          variables.storage -= amountInput
          break
    else:
        print("Not enough Storage!")

def buyRum():
  while True:
    amountInput = int(input("Enter amount: "))
    if amountInput <= variables.storage:
        totalPurchase = variables.rumMarketPrice * amountInput
        if totalPurchase > variables.gold:
            print("Not enough money!")
        else:
            variables.gold = variables.gold - totalPurchase
            print("You've just purchased", amountInput, "Rum")
            variables.rums = variables.rums + amountInput
            variables.rumPrice = variables.rumMarketPrice
            variables.storage -= amountInput
        break
    else:
        print("Not enough Storage!")

def buyLeather():
  while True:
    amountInput = int(input("Enter amount: "))
    if amountInput <= variables.storage:
        totalPurchase = variables.leatherMarketPrice * amountInput
        if totalPurchase > variables.gold:
            print("Not enough money!")
        else:
            variables.gold = variables.gold - totalPurchase
            print("You've just purchased", amountInput, "Leather")
            variables.leathers = variables.leathers + amountInput
            variables.leatherPrice = variables.leatherMarketPrice
            variables.storage -= amountInput
        break
    else:
        print("Not enough Storage!")

def buyTobacco():
  while True:
    amountInput = int(input("Enter amount: "))
    if amountInput <= variables.storage:
        totalPurchase = variables.tobaccoMarketPrice * amountInput
        if totalPurchase > variables.gold:
            print("Not enough money!")
        else:
            variables.gold = variables.gold - totalPurchase
            print("You've just purchased", amountInput, "Tobacco")
            variables.tobaccos = variables.tobaccos + amountInput
            variables.tobaccoPrice = variables.tobaccoMarketPrice
            variables.storage -= amountInput
        break
    else:
        print("Not enough Storage!")
                      
def inventory():
    print("\n█ █▄░█ █░█ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █▄█\n█ █░▀█ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ░█░\n")
    print(variables.fishes, "Fishes")
    print(variables.meats, "Meats")
    print(variables.rums, "Rums")
    print(variables.leathers, "Leathers")
    print(variables.tobaccos, "Tobaccos")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

def sell_inventory():
  print("a. Sell", variables.fishes, "Fishes")
  print("b. Sell", variables.meats, "Meats")
  print("c. Sell", variables.rums, "Rums")
  print("d. Sell", variables.leathers, "Leathers")
  print("e. Sell", variables.tobaccos, "Tobaccos")
  print("f. Back")
  while True:
    productInput = input().lower()
    if productInput == "a":
      sellFish()
      break
    elif productInput == "b":
      sellMeat()
      break
    elif productInput == "c":
      sellRum()
      break
    elif productInput == "d":
      sellLeather()
      break
    elif productInput == "e":
      sellTobacco()
      break
    elif productInput == "f":
      break
    else:
        print("Not in the Choices. Try Again!\n")

def sellFish():
  if variables.fishes > 0:
    variables.gold = variables.gold + (variables.fishes * variables.fishPrice)
    print("You've sold", variables.fishes, "Fishes for", variables.fishes * variables.fishPrice, "gold")
    variables.storage += variables.fishes
    variables.fishes = 0
  else:
    print("You have no Fishes to sell.")
    
def sellMeat():
  if variables.meats > 0:
    variables.gold = variables.gold + (variables.meats * variables.meatPrice)
    print("You've sold", variables.meats, "Meats for", variables.meats * variables.meatPrice, "gold")
    variables.storage += variables.meats
    variables.meats = 0
  else:
    print("You have no Meats to sell.")
    
def sellRum():
  if variables.rums > 0:
    variables.gold = variables.gold + (variables.rums * variables.rumPrice)
    print("You've sold", variables.rums, "Rums for", variables.rums * variables.rumPrice, "gold")
    variables.storage += variables.rums
    variables.rums = 0
  else:
    print("You have no Rums to sell.")
  
def sellLeather():
  if variables.leathers > 0:
    variables.gold = variables.gold + (variables.leathers * variables.leatherPrice)
    print("You've sold", variables.leathers, "Leathers for", variables.leathers * variables.leatherPrice, "gold")
    variables.storage += variables.leathers
    variables.leathers = 0
  else:
    print("You have no Leathers to sell.")
  
def sellTobacco():
  if variables.tobaccos > 0:
    variables.gold = variables.gold + (variables.tobaccos * variables.tobaccoPrice)
    print("You've sold", variables.tobaccos, "Tobaccos for", variables.tobaccos * variables.tobaccoPrice, "gold")
    variables.storage += variables.tobaccos
    variables.tobaccos = 0  
  else:
    print("You have no Tobaccos to sell.")
  









