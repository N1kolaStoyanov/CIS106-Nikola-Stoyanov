def battingavg(hits, bats):
  avg = hits / bats
  return avg 

r = input("Do you wish to calculate batting avarage (y/n)?")

p = 0
while r == "y":
  name = input("Enter Last Name")
  hits = float(input("Please Enter Number of Hits"))
  bats = float(input("Please Enter Number of Bats taken"))
  p = p +1
  print(name ,"'s" ,"batting Average is ", battingavg(hits, bats))
  r = input("Do you wish to calculate batting avarage (y/n)?")
print("You have calculated ", p, " batting averages")
