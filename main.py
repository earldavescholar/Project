import random
import time
import json

from market import marketx
from market import inventory
import variables
from bank import bank
from shop import shop
from island import island
from common import common
from variables import saveGame



print(    "\n\n █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─█")
print(    " ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█")
print(    " ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀\n")
print(    "                     ▀█▀ █▀█")
print(    "                     ░█░ █▄█\n")
print(    "██████╗░██╗██████╗░░█████╗░░██████╗███████╗░█████╗░")
print(    "██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗")
print(    "██████╔╝██║██████╔╝███████║╚█████╗░█████╗░░███████║")
print(    "██╔═══╝░██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░██╔══██║")
print(    "██║░░░░░██║██║░░██║██║░░██║██████╔╝███████╗██║░░██║")
print(    "╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝\n\n")

print("a. Start Game")
print("b. Quit Game\n")

# Main Screen
while True:
    inp = input()
    if inp.lower() == 'a':
        print("\nLoading...")
        time.sleep(2)
        print("\n>You are now on an island\n")
        variables.island = variables.m
        print("Island:", variables.island)
        variables.fishMarketPrice = variables.fishRandomPrice
        variables.meatMarketPrice = variables.meatRandomPrice
        variables.rumMarketPrice = variables.rumRandomPrice
        variables.tobaccoMarketPrice = variables.tobaccoRandomPrice
        variables.leatherMarketPrice = variables.leatherRandomPrice
        variables.boat = variables.boats[0]
    elif inp == 'b':
        print("\nThank you, Come again:)")
        break
        exit()
    else:
        print("Not in the Choices. Try Again!\n")
      
    while True:
      if variables.island == variables.m:
        while True:
          common()
          print("\na. Status")
          print("b. Inventory")
          print("c. Market")
          print("d. Bank")
          print("e. Set Sail")
          print("f. Save Game")
          print("g. Save & Quit Game\n")
          while True:
            input1 = input()
            if input1.lower() == "a":
              print("\n█▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀\n▄█ ░█░ █▀█ ░█░ █▄█ ▄█\n")
              print("Gold:", variables.gold)
              print("Storage:", variables.storage)
              print("Item:", variables.item)
              print("Boat HP:", variables.ship_HP)
              print("Boat:", variables.boat)
              print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
              break
            elif input1.lower() == 'b':
              inventory()
              break
            elif input1.lower() == "c":
              marketx()
              break
            elif input1.lower() == "d":
              bank()
              break
            elif input1.lower() == "e":
              island()
              break
            elif input1.lower() == "f":
              saveGame()
              print("Game Saved")
            elif input1.lower() == "g":
              saveGame()
              print("Thank you for playing!")
              exit()
            else:
              print("Not in the Choices. Try Again!\n")
          break           
      
      if variables.island == variables.l:
        while True:
          common()
          print("\na. Status")
          print("b. Inventory")
          print("c. Market")
          print("d. Shop")
          print("e. Set Sail")
          print("f. Save Game")
          print("g. Quit Game\n")
          while True:
            input1 = input()
            if input1.lower() == "a":
              print("\n█▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀\n▄█ ░█░ █▀█ ░█░ █▄█ ▄█\n")
              print("Gold:", variables.gold)
              print("Storage:", variables.storage)
              print("Item:", variables.item)
              print("Boat HP:", variables.ship_HP)
              print("Boat:", variables.boat)
              print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
              break
            elif input1.lower() == 'b':
              inventory()
              break
            elif input1.lower() == "c":
              marketx()
              break
            elif input1.lower() == "d":
              shop()
              break
            elif input1.lower() == "e":
              island()
              break
            elif input1.lower() == "f":
              saveGame()
              print("Game Saved")
            elif input1.lower() == "g":
              saveGame()
              print("Thank you for playing!")
              exit()
            else:
              print("Not in the Choices. Try Again!\n")
          break
      
      if variables.island == variables.v:
        while True:
          common()
          print("\na. Status")
          print("b. Inventory")
          print("c. Market")
          print("d. Set Sail")
          print("e. Save Game")
          print("f. Quit Game\n")
          while True:
            input1 = input()
            if input1.lower() == "a":
              print("\n█▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀\n▄█ ░█░ █▀█ ░█░ █▄█ ▄█\n")
              print("Gold:", variables.gold)
              print("Storage:", variables.storage)
              print("Item:", variables.item)
              print("Boat HP:", variables.ship_HP)
              print("Boat:", variables.boat)
              print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
              break
            elif input1.lower() == 'b':
              inventory()
              break
            elif input1.lower() == "c":
              marketx()
              break
            elif input1.lower() == "d":
              island()
              break
            elif input1.lower() == "e":
              saveGame()
              print("Game Saved")
            elif input1.lower() == "f":
              saveGame()
              print("Thank you for playing!")
              exit()
            else:
              print("Not in the Choices. Try Again!\n")
          break

