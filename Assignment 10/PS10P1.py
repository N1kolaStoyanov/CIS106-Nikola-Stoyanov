def compute_forecast(month, sales):
  forecast_percent = 0.0

  if month in ["Jan", "Feb", "Mar"]:
      forecast_percent = 0.10
  elif month in ["Apr", "May", "Jun"]:
      forecast_percent = 0.15
  elif month in ["Jul", "Aug", "Sep"]:
      forecast_percent = 0.20
  elif month in ["Oct", "Nov", "Dec"]:
      forecast_percent = 0.25

  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

def main():
  while True:
      response = input("Do you want to calculate the next month's forecast? (Yes/No): ").lower()

      if response != "yes":
          break

      last_name = input("Enter your last name: ")
      month = input("Enter the month (Jan, Feb, ..., Dec): ").capitalize()
      sales = float(input("Enter the current month's sales: "))

      next_month_sales = compute_forecast(month, sales)

      print(f"\nHello {last_name}, the forecast for {month} is {next_month_sales:.2f}.\n")

if __name__ == "__main__":
  main()
