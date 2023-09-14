import time
import random

print("Welcome to Pira-Sea\n\n")
print("a. Start Game")
print("b. Quit Game\n")

confirmation = False
island = ""

#inventory
fishes = 0
meats = 0
rums = 0
leathers = 0
tobaccos = 0

# status
ship_HP = 100
gold = 100
storage = 20
vessel = ""

# islands
l = "Luzon"
v = "Visayas"
m = "Mindanao"

# Bank
balance = 0

#Price
fishPrice = 0
meatPrice = 0
rumPrice = 0
tobaccoPrice = 0
leatherPrice = 0


# Main Screen
while True:
    inp = input()
    if inp.lower() == 'a':
        print("\nLoading...")
        time.sleep(0)
        print("\n>You are now on an island")
        island = m
        confirmation = True
        break
    elif inp == 'b':
        print("\nThank you, Come again:)")
        break
        exit()
    else:
        print("Not in the Choices. Try Again!\n")
x = True
# Nagdula na
if confirmation == True and island == m:
    # market random prices
    fishRandomPrice = random.randint(6, 13)
    meatRandomPrice = random.randint(7, 14)
    rumRandomPrice = random.randint(12, 20)
    tobaccoRandomPrice = random.randint(18, 23)
    leatherRandomPrice = random.randint(16, 25)
    while x:
        print("\nIsland:", island)
        print("\na. Status")
        print("b. Market")
        print("c. Bank")
        print("d. Set Sail\n")
        while True:
            input1 = input()
            if input1.lower() == "a":
                print("Status")
                print("Gold:", gold)
                print("Boat HP:", ship_HP)
                print("Vessel:", vessel)
                break
            elif input1.lower() == "b":
                while True:
                  print("Market")
                  print("a. Buy")
                  print("b. Sell")
                  print("c. Back")
                  marketInput = input()
                  if marketInput.lower() == "a":
                      print("a. Fish -", fishRandomPrice)
                      print("b. Meat -", meatRandomPrice)
                      print("c. Rum -", rumRandomPrice)
                      print("d. Leather -", leatherRandomPrice)
                      print("e. Tobacco -", tobaccoRandomPrice)
                      print("f. Back")
                      while True:
                          buyInput = input()
                          if buyInput.lower() == "a":
                            while True:
                              amountInput = int(input("Enter amount: "))
                              if amountInput <= storage:
                                  totalPurchase = fishRandomPrice * amountInput
                                  if totalPurchase > gold:
                                      print("Not enough money! Try again")
                                  else:
                                      gold = gold - totalPurchase
                                      print("You've just purchased", amountInput, "Fish")
                                      fishes = fishes + amountInput
                                      fishPrice = fishRandomPrice
                                      break
                                  break
                              else:
                                  print("Not enough Storage! Try again")
                                  
                          elif buyInput.lower() == "b":
                              amountInput = int(input("Enter amount: "))
                              if amountInput <= storage:
                                  totalPurchase = meatRandomPrice * amountInput
                                  if totalPurchase > gold:
                                      print("Not enough money!")
                                  else:
                                      gold = gold - totalPurchase
                                      print("You've just purchased", amountInput, "Meat")
                                      meats = meats + amountInput
                                      meatPrice = meatRandomPrice
                                      break
                              else:
                                  print("Not enough Storage!")
  
                          elif buyInput.lower() == "c":
                              amountInput = int(input("Enter amount: "))
                              if amountInput <= storage:
                                  totalPurchase = rumRandomPrice * amountInput
                                  if totalPurchase > gold:
                                      print("Not enough money!")
                                  else:
                                      gold = gold - totalPurchase
                                      print("You've just purchased", amountInput, "Rum")
                                      rums = rums + amountInput
                                      rumPrice = rumRandomPrice
                                      break
                              else:
                                  print("Not enough Storage!")
  
                          elif buyInput.lower() == "d":
                              amountInput = int(input("Enter amount: "))
                              if amountInput <= storage:
                                  totalPurchase = leatherRandomPrice * amountInput
                                  if totalPurchase > gold:
                                      print("Not enough money!")
                                  else:
                                      gold = gold - totalPurchase
                                      print("You've just purchased", amountInput, "Leather")
                                      leathers = leathers + amountInput
                                      leatherPrice = leatherRandomPrice
                                      break
                              else:
                                  print("Not enough Storage!")
  
                          elif buyInput.lower() == "e":
                              amountInput = int(input("Enter amount: "))
                              if amountInput <= storage:
                                  totalPurchase = tobaccoRandomPrice * amountInput
                                  if totalPurchase > gold:
                                      print("Not enough money!")
                                  else:
                                      gold = gold - totalPurchase
                                      print("You've just purchased", amountInput, "Tobacco")
                                      tobaccos = tobaccos + amountInput
                                      tobaccoPrice = tobaccoRandomPrice
                                      break
                              else:
                                  print("Not enough Storage!")
                          elif buyInput.lower() == 'f':
                            break
                          else:
                              # basta mu loop
                              print("Not in the Choices. Try Again!\n")
  
                  elif marketInput.lower() == "b":
                    print("Inventory: ")
                    print(fishes, "Fishes")
                    print(meats, "Meats")
                    print(rums, "Rums")
                    print(leathers, "Leathers")
                    print(tobaccos, "Tobaccos")
                    print("\na. sell")
                    print("b. back")
                    while True:
                      sellInput = input()
                      if sellInput.lower()=='a':
                        print("a. Sell", fishes, "Fishes")
                        print("b. Sell", meats, "Meats")
                        print("c. Sell", rums, "Rums")
                        print("d. Sell", leathers, "Leathers")
                        print("e. Sell", tobaccos, "Tobaccos")
                        productInput = input()
                        if productInput.lower() == "a":
                          gold = gold + (fishes * fishPrice)
                          fishes = 0
                          break
                        elif productInput.lower() == "b":
                          gold = gold + (meats * meatPrice)
                          meats = 0
                          break
                        elif productInput.lower() == "c":
                          gold = gold + (rums * rumPrice)
                          rums = 0
                          break
                        elif productInput.lower() == "d":
                          gold = gold + (leathers * leatherPrice)
                          leathers = 0
                          break
                        elif productInput.lower() == "e":
                          gold = gold + (tobaccos * tobaccoPrice)
                          tobaccos = 0
                          break
                        else:
                          print("Not in the Choices. Try Again!\n")
                      elif sellInput.lower() == 'b':
                        break
                      else:
                        print("Not in the Choices. Try Again!\n")
                  elif marketInput.lower() == "c":
                    break
                  else:
                    print("Not in the Choices. Try Again!\n")
                break
            elif input1.lower() == "c":
                print("Bank Balance:", balance)
                print("a. Deposit")
                print("b. Withdraw")
                bankInput = input()
                if bankInput.lower() == 'a':
                    deposit = int(input("Enter Amount to Deposit: "))
                    if deposit <= gold:
                        balance = deposit + balance
                        print("Bank Balance:", balance)
                    else:
                        print("Not enough money!")
                x = False
                break
            elif input1.lower() == "d":
                print("Enter your destination:")
                if island == m:
                    print("a. Luzon")
                    print("b. Visayas")
                    islandInput = input()
                    if islandInput.lower() == 'a':
                        island = l
                    elif islandInput.lower() == 'b':
                        island = v
                elif island.lower() == v:
                    print("Enter your destination:")
                    print("a. Luzon")
                    print("b. Mindanao")
                    islandInput = input()
                elif island.lower() == l:
                    print("Enter your destination:")
                    print("a. Visayas")
                    print("b. Mindanao")
                    islandInput = input()
                x = False
                break
            else:
                print("Not in the Choices. Try Again!\n")
                x == False


