def tution(chours, dcode):
  if dcode == "I":
    cph = 250
    total = cph * chours
    return total
  elif dcode =="O":
    cph = 550
    total = cph * chours
    return total

tt = 0

r = input("Do you wish to calculate tution (Y/N)?")
while r =="Y":
  name = input("Enter Students name: ")
  dcode = input("Enter district code (I/O)")
  chours = float(input("Enret amount of credit hours taken"))
  total = tution(chours, dcode)
  print("Student:" ,name ,"has tution of $", total)
  tt = tt + total
  r = input("Do you wish to calculate tution (y/n)?")
  print ("Tuituon owed by everyone is $" ,tt)
