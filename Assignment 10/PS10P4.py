def compute_ticket_price(miles_from_chicago):
  if miles_from_chicago >= 30:
      ticket_price = 12
  elif 20 <= miles_from_chicago <= 29:
      ticket_price = 10
  elif 10 <= miles_from_chicago <= 19:
      ticket_price = 8
  else:
      ticket_price = 5

  return ticket_price

def main():
  total_ticket_price = 0

  while True:
      response = input("Do you want to calculate the train ticket price? (Yes/No): ").lower()

      if response != "yes":
          break

      last_name = input("Enter your last name: ")
      miles_from_chicago = float(input("Enter the miles from downtown Chicago: "))

      ticket_price = compute_ticket_price(miles_from_chicago)
      total_ticket_price += ticket_price

      print(f"\nHello {last_name}, the train ticket price is ${ticket_price:.2f}\n")

  print(f"\nTotal price of all tickets: ${total_ticket_price:.2f}")

if __name__ == "__main__":
  main()
