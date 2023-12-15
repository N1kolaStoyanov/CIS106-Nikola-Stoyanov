def display_names(names):
  print("Names:")
  for name in names:
      print(name)

def display_names_reverse(names):
  print("\nNames in Reverse Order:")
  for name in reversed(names):
      print(name)

def main():
  # Assign 10 last names to an array
  last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

  # Display names
  display_names(last_names)

  # Display names in reverse order
  display_names_reverse(last_names)

if __name__ == "__main__":
  main()
