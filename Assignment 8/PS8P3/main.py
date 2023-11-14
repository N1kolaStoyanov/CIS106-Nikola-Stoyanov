f = open("dat.txt", "r")

name = f.readline()

while name != "":
  
  salary = int(f.readline().strip())
  if salary >= 100000 :
    bonus = .20 
  elif salary >= 50000:
    bonus = .15
  else :
    bonus = .10
  fs = bonus * salary + salary
  print(name,"salary is $" ,salary ,"Bonus is %" ,bonus * 100,)
  bonusf = salary * bonus
  
  bonus_list = []
  bonus_list.append(bonusf)
  total_bonus = sum(bonus_list)
  print("Total bonus is $" ,total_bonus)
  name = f.readline()
