def compute_commission_and_target(sales):
  if sales > 100000:
      commission = 0.10 * sales
  else:
      commission = 0.05 * sales

  next_year_target = 0.05 * sales

  return commission, next_year_target

def main():
  last_name = input("Enter the salesperson's last name: ")
  sales = float(input("Enter the sales amount: "))

  commission, next_year_target = compute_commission_and_target(sales)

  print(f"\nSalesperson Last Name: {last_name}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${next_year_target:.2f}")

if __name__ == "__main__":
  main()
