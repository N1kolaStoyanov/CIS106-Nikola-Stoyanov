def compextprice(qty, unitprice):
  extprice = qty * unitprice

  if extprice > 10000:
    discamt = extprice * 0.10
  else :
    discamt = 0.0
    
  return extprice 

totalextprice = 0
r = input("Do you want to compute extended price (y/n)?")

while r  == "y":
  qty = float(input("Enter Quantity:"))
  unitprice = float(input("Enter unit price:"))
  extprice = compextprice(qty , unitprice)
  totalextprice = totalextprice + extprice
  print("Extended price is $" ,extprice)
  r = input("Do you want to compute extended price (y/n)?")

print("Total extended price is $" ,totalextprice)
