import random
import json

confirmation = False
island = ""
pirates = 0

pirateDamage = 0
maintenance = 0
itemDefense = 0
defense = 0
pirateGold = 0

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
boat = ""
item = "None"

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

#random
fishRandomPrice = random.randint(6, 13)
meatRandomPrice = random.randint(7, 15)
rumRandomPrice = random.randint(12, 22)
tobaccoRandomPrice = random.randint(18, 30)
leatherRandomPrice = random.randint(21, 35)

#events
repairPrice = 0



#market price
fishMarketPrice = 0
meatMarketPrice = 0
rumMarketPrice = 0
tobaccoMarketPrice = 0
leatherMarketPrice = 0

#items
items = ['none', 'Pintik', 'Sundang', 'Pana', 'Pusil', 'Bomba', 'Kanyon']
boats = ['Dinghy', 'Balangay', 'Baruto', 'Karakoa', 'Galleon', 'Titanic']

boat_HP = 100
repairPrice = 0

def saveGame():
  game_data = {
    "confirmation": confirmation,
    "island": island,
    "pirates": pirates,
    "pirateDamage": pirateDamage,
    "maintenance": maintenance,
    "itemDefense": itemDefense,
    "defense": defense,
    "pirateGold": pirateGold,
    "fishes": fishes,
    "meats": meats,
    "rums": rums,
    "leathers": leathers,
    "tobaccos": tobaccos,
    "ship_HP": ship_HP,
    "gold": gold,
    "storage": storage,
    "boat": boat,
    "item": item,
    "balance": balance,
    "fishPrice": fishPrice,
    "meatPrice": meatPrice,
    "rumPrice": rumPrice,
    "tobaccoPrice": tobaccoPrice,
    "leatherPrice": leatherPrice,
    "fishRandomPrice": fishRandomPrice,
    "meatRandomPrice": meatRandomPrice,
    "rumRandomPrice": rumRandomPrice,
    "tobaccoRandomPrice": tobaccoRandomPrice,
    "leatherRandomPrice": leatherRandomPrice,
    "fishMarketPrice": fishMarketPrice,
    "meatMarketPrice": meatMarketPrice,
    "rumMarketPrice": rumMarketPrice,
    "tobaccoMarketPrice": tobaccoMarketPrice,
    "leatherMarketPrice": leatherMarketPrice,
    "boat_HP": boat_HP,
    "repairPrice": repairPrice
  }
  
  json_string = json.dumps(game_data, indent=4)
  
  with open('save.json', 'w') as json_file:
      json_file.write(json_string)





  
