import main
import random
class market:
  def marketx():
    fishRandomPrice = random.randint(6, 13)
    meatRandomPrice = random.randint(7, 14)
    rumRandomPrice = random.randint(12, 20)
    tobaccoRandomPrice = random.randint(18, 23)
    leatherRandomPrice = random.randint(16, 25)
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
      print()
    else:
      print("Not in the Choices. Try Again!\n")
  