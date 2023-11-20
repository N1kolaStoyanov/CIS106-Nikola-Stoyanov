def PR(jobcode, hours):
  if jobcode == "L":
    pph = 25
    if hours > 40:
      pay = 40 * pph + (hours - 40) * (pph * 1.5)
    else:
      pay = hours * pph

  elif jobcode == "A":
    pph = 30
    if hours > 40:
      pay = 40 * pph + (hours - 40) * (pph * 1.5)
    else: 
      pay = hours * pph
  elif jobcode == "J":
    pph = 50
    if hours > 40:
      pay = 40 * pph + (hours - 40) * (pph * 1.5)
    else:
      pay = hours * pph

  return pay
grosspay = 0

r = input("Do you wish to calculate payrate (y/n)?")

while r == "y":
  name = input("Enter Last name")
  jobcode = input("Enter job code (L,A,J)")
  hours = float(input("Enter hours worked"))
  pay = PR(jobcode, hours)
  print(name, pay)
  grosspay = grosspay + pay
  r = input("Do you wish to calculate payrate (y/n)?")
  print("Gross pay is", grosspay)
