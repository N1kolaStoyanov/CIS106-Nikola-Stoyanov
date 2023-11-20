def millespergallon(milles, gallons):
  MPG = milles / gallons
  return MPG 

t = 0
r = input("Do you want to calculate the MPG (y/n)")

while r == "y":
  name = input("Enter Destination Name")
  milles = float(input("Enter milles driven"))
  gallons = float(input("Enter Gallons used"))
  MPG = millespergallon(milles, gallons)
  t = t + 1
  print("destination is",name ,"and the milles dirven are" ,milles ,", the milles per Gallons are" ,MPG)
  
  r = input("Do you want to calculate the MPG (y/n)")
  
  print("Trips calculated are" ,t)
