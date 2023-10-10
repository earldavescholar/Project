import variables
import random

def shop():
  print("\n█▀ █░█ █▀█ █▀█\n▄█ █▀█ █▄█ █▀▀\n")
  print("Boat Health:", variables.ship_HP, "/", variables.boat_HP)
  print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  print("\na. Repair Boat")
  print("b. Buy Boat")
  print("c. Buy Items")
  print("d. Back")
  while True:
    shopInput = input()
    if shopInput == 'a':
      repairBoat()
      break
    elif shopInput == 'b':
      buyBoat()
      break
    elif shopInput == 'c':
      buyItems()
      break
    elif shopInput == 'd':
      break
    else:
      print("Not in the Choices. Try Again!\n")

def repairBoat():
  if variables.repairPrice <= variables.gold:
    variables.ship_HP += variables.boat_HP-variables.ship_HP
    variables.gold -= variables.repairPrice
    print("Repaired boat for", variables.repairPrice, "gold.")
  else:
    print("Not enough gold!")
    
def buyBoat():
  print("a. Balangay")
  print("b. Baruto")
  print("c. Karakoa")
  print("d. Galleon")
  print("e. Titanic")
  print("f. Back")
  while True:
    boatInput = input()
    if boatInput == 'a':
      buyBalangay()
      break
    elif boatInput == 'b':
      buyBaruto()
      break
    elif boatInput == 'c':
      buyKarakoa()
      break
    elif boatInput == 'd':
      buyGalleon()
      break
    elif boatInput == 'e':
      buyTitanic()
      break
    elif boatInput == 'f':
      break
    else:
      print("Not in the Choices. Try Again!\n")
      
def buyItems():
  buy = "a"
  print("\nRandom Items for 500 gold\n")
  print("Items:")
  print("•Common:     +1  Defense")
  print("•Uncommon:   +1  Defense | +5   Gold from pirates")
  print("•Rare:       +2  Defense | +15  Gold from pirates")
  print("•Epic:       +3  Defense | +30  Gold from pirates")
  print("•Legendary:  +5  Defense | +70  Gold from pirates")
  print("•Mythical:   +10 Defense | +100 Gold from pirates\n")
  print("Your existing item will be replaced by what you buy\n")
  while buy == 'a':
    print("a. Buy")
    print("b. Back\n")
    while True:
      buyInput = input()
      if buyInput == 'a':
        buy = 'a'
        buyItem()
        break
      elif buyInput == 'b':
        buy = 'b'
        break
      else:
        print("Not in the Choices. Try Again!\n")

def buyBalangay():
  print("Boat: Balangay\nHP: 250\nStorage: 40\nPrice: 1000 gold\n")
  print("a. Buy")
  print("b. Back")
  while True:
    buyInput = input()
    if buyInput == 'a':
      variables.gold -= 1000
      variables.ship_HP = 200
      variables.boat_HP = 200
      variables.storage = 40
      variables.pirateDamage = 2
      variables.maintenance = 1
      variables.pirates = 0.01
      variables.fishes = 0
      variables.meats = 0
      variables.rums = 0
      variables.leathers = 0
      variables.tobaccos = 0
      variables.boat = variables.boats[1]
      break
    elif buyInput == 'b':
      break
    else:
      print("Not in the Choices. Try Again!\n")
      
def buyBaruto():
  print("Boat: Baruto\nHP: 500\nStorage: 60\nPrice: 5000 gold\n")
  print("a. Buy")
  print("b. Back")
  while True:
    buyInput = input()
    if buyInput == 'a':
      variables.gold -= 5000
      variables.ship_HP = 350
      variables.boat_HP = 350
      variables.storage = 60
      variables.pirateDamage = 5
      variables.maintenance = 2
      variables.pirates = 0.05
      variables.fishes = 0
      variables.meats = 0
      variables.rums = 0
      variables.leathers = 0
      variables.tobaccos = 0
      variables.boat = variables.boats[2]
      break
    elif buyInput == 'b':
      break
    else:
      print("Not in the Choices. Try Again!\n")
      
def buyKarakoa():
  print("Boat: Karakoa\nHP: 900\nStorage: 90\nPrice: 9000 gold\n")
  print("a. Buy")
  print("b. Back")
  while True:
    buyInput = input()
    if buyInput == 'a':
      variables.gold -= 9000
      variables.ship_HP = 500
      variables.boat_HP = 500
      variables.storage = 90
      variables.pirateDamage = 7
      variables.maintenance = 3
      variables.pirates = 0.1
      variables.fishes = 0
      variables.meats = 0
      variables.rums = 0
      variables.leathers = 0
      variables.tobaccos = 0
      variables.boat = variables.boats[3]
      break
    elif buyInput == 'b':
      break
    else:
      print("Not in the Choices. Try Again!\n")

def buyGalleon():
  print("Boat: Galleon\nHP: 1500\nStorage: 130\nPrice: 15000 gold\n")
  print("a. Buy")
  print("b. Back")
  while True:
    buyInput = input()
    if buyInput == 'a':
      variables.gold -= 9000
      variables.ship_HP = 750
      variables.boat_HP = 750
      variables.storage = 130
      variables.pirateDamage = 10
      variables.maintenance = 4
      variables.pirates = 0.3
      variables.fishes = 0
      variables.meats = 0
      variables.rums = 0
      variables.leathers = 0
      variables.tobaccos = 0
      variables.boat = variables.boats[4]
      break
    elif buyInput == 'b':
      break
    else:
      print("Not in the Choices. Try Again!\n")

def buyTitanic():
  print("Boat: Titanic\nHP: 3000\nStorage: 200\nPrice: 25000 gold\n")
  print("a. Buy")
  print("b. Back")
  while True:
    buyInput = input()
    if buyInput == 'a':
      variables.gold -= 25000
      variables.ship_HP = 1000
      variables.boat_HP = 1000
      variables.storage = 130
      variables.pirateDamage = 13
      variables.maintenance = 5
      variables.pirates = 0.5
      variables.fishes = 0
      variables.meats = 0
      variables.rums = 0
      variables.leathers = 0
      variables.tobaccos = 0
      variables.boat = variables.boats[5]
      break
    elif buyInput == 'b':
      break
    else:
      print("Not in the Choices. Try Again!\n")

def buyItem():
  if variables.gold > 500:
    variables.gold -= 500
    item = random.random()
    if item < 0.01:
      variables.item = variables.items[6]
      variables.itemDefense = 10
      variables.pirateGold = 100
      print("You got a mythical item: Kanyon")
    elif item < 0.02:
      variables.item = variables.items[5]
      variables.itemDefense = 5
      variables.pirateGold = 70
      print("You got a legendary item: Bomba")
    elif item < 0.05:
      variables.item = variables.items[4]
      variables.itemDefense = 3
      variables.pirateGold = 30
      print("You got an epic item: Pusil")
    elif item < 0.1:
      variables.item = variables.items[3]
      variables.itemDefense = 2
      variables.pirateGold = 15
      print("You got a rare item: Pana")
    elif item <= 0.4:
      variables.item = variables.items[2]
      variables.itemDefense = 1
      variables.pirateGold = 5
      print("\nGot an item!\n")
      print("\n     █▀▀ █░░█ █▀▀▄ █▀▀▄ █▀▀█ █▀▀▄ █▀▀▀")
      print("     ▀▀█ █░░█ █░░█ █░░█ █▄▄█ █░░█ █░▀█")
      print("     ▀▀▀ ░▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀░░▀ ▀▀▀▀")
      print("  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
      print("\n   █░█ █▄░█ █▀▀ █▀█ █▀▄▀█ █▀▄▀█ █▀█ █▄░█")
      print("   █▄█ █░▀█ █▄▄ █▄█ █░▀░█ █░▀░█ █▄█ █░▀█\n")



    elif item > 0.4:
      variables.item = variables.items[1]
      variables.itemDefense = 1
      print("\nGot an item!\n")
      print("\n▒█▀▀█ ▀█▀ ▒█▄░▒█ ▀▀█▀▀ ▀█▀ ▒█░▄▀")
      print("▒█▄▄█ ▒█░ ▒█▒█▒█ ░▒█░░ ▒█░ ▒█▀▄░")
      print("▒█░░░ ▄█▄ ▒█░░▀█ ░▒█░░ ▄█▄ ▒█░▒█")
      print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
      print("\n  █▀▀ █▀█ █▀▄▀█ █▀▄▀█ █▀█ █▄░█")
      print("  █▄▄ █▄█ █░▀░█ █░▀░█ █▄█ █░▀█\n")
    else:
      print("No luck:( Try again next time:)")
  else:
    print("Not enough gold!")

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 
 

