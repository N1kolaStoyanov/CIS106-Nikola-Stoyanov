def compute_assessed_value(county, market_value):
  assessed_value_percent = 0.0

  if county == "Cook":
      assessed_value_percent = 0.90
  elif county == "DuPage":
      assessed_value_percent = 0.80
  elif county == "McHenry":
      assessed_value_percent = 0.75
  elif county == "Kane":
      assessed_value_percent = 0.60
  else:
      assessed_value_percent = 0.70

  assessed_value = market_value * assessed_value_percent
  return assessed_value

def main():
  total_market_values = 0
  total_assessed_values = 0

  while True:
      response = input("Do you want to calculate the assessed value of a home? (Yes/No): ").lower()

      if response != "yes":
          break

      county = input("Enter the county of the home: ")
      market_value = float(input("Enter the market value of the home: "))

      assessed_value = compute_assessed_value(county, market_value)
      total_market_values += market_value
      total_assessed_values += assessed_value

      print(f"\nThe assessed value of the home in {county} County is ${assessed_value:.2f}\n")

  print(f"\nTotal market values of all homes: ${total_market_values:.2f}")
  print(f"Total assessed values of all homes: ${total_assessed_values:.2f}")

if __name__ == "__main__":
  main()
