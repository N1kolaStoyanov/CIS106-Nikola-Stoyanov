def compute_out_the_door_price(msrp, make, model, electric_vehicle):
  percent_off = 0.0

  if make == "Honda" and model == "Accord":
      percent_off = 0.10
  elif make == "Toyota" and model == "Rav4":
      percent_off = 0.15
  elif electric_vehicle == "Y":
      percent_off = 0.30
  else:
      percent_off = 0.05

  discount = msrp * percent_off
  new_msrp = msrp - discount
  sales_tax = 0.07 * new_msrp

  out_the_door_price = new_msrp + sales_tax

  return out_the_door_price, new_msrp

def main():
  total_msrp = 0
  total_sales_price = 0

  while True:
      response = input("Do you want to calculate the out-the-door price of an automobile? (Yes/No): ").lower()

      if response != "yes":
          break

      make = input("Enter the make of the car: ")
      model = input("Enter the model of the car: ")
      electric_vehicle = input("Is it an electric vehicle? (Y/N): ").upper()
      msrp = float(input("Enter the MSRP (sticker price) of the car: "))

      out_the_door_price, new_msrp = compute_out_the_door_price(msrp, make, model, electric_vehicle)

      total_msrp += msrp
      total_sales_price += out_the_door_price

      print(f"\nThe out-the-door price for the {make} {model} is ${out_the_door_price:.2f}\n")

  print(f"\nTotal MSRP of all cars: ${total_msrp:.2f}")
  print(f"Total sales price of all cars: ${total_sales_price:.2f}")

if __name__ == "__main__":
  main()
