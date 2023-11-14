f = open("data.txt" ,"r")
c = 0
totep = 0


item = f.readline().rstrip('\n')
while item != "":
  qty = float(f.readline())
  price = float(f.readline())
  ep = qty * price
 
  totep = totep + ep 
  c = c + 1 

  print("item is " ,item)
  print("Quantity is" ,qty)
  print("Price is $" ,price)
  print("Extended price is $" ,ep)
  item = f.readline().rstrip('\n')
avg = totep / c
print("Total extended price is $" ,totep)
print("Total items is " ,c)
print("Average is $" ,avg)
