import variables
import random

def island():
  print("Enter your destination:")
  if variables.island == variables.m:
    print("a. Luzon")
    print("b. Visayas")
    print("c. Back")
    while True:
      islandInput = input()
      if islandInput.lower() == 'a':
        variables.island = variables.l
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'b':
        variables.island = variables.v
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'c':
        break
      else:
        print("Not in the Choices. Try Again!\n")
  elif variables.island == variables.v:
    print("a. Luzon")
    print("b. Mindanao")
    print("c. Back")
    while True:
      islandInput = input()
      if islandInput.lower() == 'a':
        variables.island = variables.l
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'b':
        variables.island = variables.m
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'c':
        break
      else:
        print("Not in the Choices. Try Again!\n")
  elif variables.island == variables.l:
    print("a. Visayas")
    print("b. Mindanao")
    print("c. Back")
    while True:
      islandInput = input()
      if islandInput.lower() == 'a':
        variables.island = variables.v
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'b':
        variables.island = variables.m
        travel()
        eco()
        print("Island:", variables.island)
        break
      elif islandInput.lower() == 'c':
        break
      else:
        print("Not in the Choices. Try Again!\n")

def eco():
  variables.fishMarketPrice = random.randint(6, 13)
  variables.meatMarketPrice = random.randint(7, 15)
  variables.rumMarketPrice = random.randint(12, 22)
  variables.tobaccoMarketPrice = random.randint(18, 30)
  variables.leatherMarketPrice = random.randint(21, 35)
  variables.fishPrice = variables.fishMarketPrice
  variables.meatPrice = variables.meatMarketPrice
  variables.rumPrice = variables.rumMarketPrice
  variables.tobaccoPrice = variables.tobaccoMarketPrice
  variables.leatherPrice = variables.leatherMarketPrice

def travel():
  x = random.random()
  variables.ship_HP -= variables.maintenance
  variables.balance += 1
  if x > variables.pirates:
    print("\nTravelled safely")
  else:
    y = random.random()
    print("You have been attacked by pirates!")
    if variables.pirateDamage > variables.itemDefense:
      variables.defense = variables.pirateDamage - variables.itemDefense
    else:
      variables.defense = variables.pirateDamage
    variables.ship_HP -= (variables.pirateDamage - variables.defense)
    variables.gold += variables.pirateGold
    if y > variables.pirates:
      print("Inventory is Safe")
    else:
      x = variables.fishes + variables.meats + variables.rums + variables.leathers + variables.tobaccos
      if x > 0:
        variables.fishes = 0
        variables.meats = 0
        variables.rums = 0
        variables.leathers = 0
        variables.tobaccos = 0
        print("Your products are stolen")
      else:
        print("Luckyly, you have no products to be stolen")