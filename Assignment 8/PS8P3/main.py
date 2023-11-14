f = open("dat.txt", "r")
tbonusf = 0
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
  print("Bonus soo far is $" ,total_bonus)
  tbonusf = tbonusf + bonusf
  print("Total bonus is $" ,tbonusf)
  name = f.readline()
