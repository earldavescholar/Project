import variables

def common():
  #Dinghy
  if variables.boat == variables.boats[0]:
    variables.boat_HP = 100
    variables.repairPrice = 1*(variables.boat_HP-variables.ship_HP)
    
  #Balangay
  elif variables.boat == variables.boats[1]:
    variables.boat_HP = 200
    variables.repairPrice = 6*(variables.boat_HP-variables.ship_HP)
    
  #Baruto
  elif variables.boat == variables.boats[2]:
    variables.boat_HP = 350
    variables.repairPrice = 9*(variables.boat_HP-variables.ship_HP)
    
  #Karakoa
  elif variables.boat == variables.boats[3]:
    variables.boat_HP = 500
    variables.repairPrice = 14*(variables.boat_HP-variables.ship_HP)
    
  #Galleon
  elif variables.boat == variables.boats[4]:
    variables.boat_HP = 750
    variables.repairPrice = 23*(variables.boat_HP-variables.ship_HP)
    
  #Titanic
  elif variables.boat == variables.boats[5]:
    variables.boat_HP = 1000
    variables.repairPrice = 47*(variables.boat_HP-variables.ship_HP)
