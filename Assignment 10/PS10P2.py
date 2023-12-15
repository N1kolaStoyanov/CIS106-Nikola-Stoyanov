def compute_square_footage(length, width, height):
  floor_ceiling_area = 2 * length * width
  wall1_area = 2 * length * height
  wall2_area = 2 * width * height

  total_area = floor_ceiling_area + wall1_area + wall2_area
  return total_area

def gallons_needed(square_footage):
  gallons_per_square_foot = 1 / 50
  return square_footage * gallons_per_square_foot

def main():
  while True:
      response = input("Do you want to calculate the number of gallons needed to paint a room? (Yes/No): ").lower()

      if response != "yes":
          break

      length = float(input("Enter the length of the room: "))
      width = float(input("Enter the width of the room: "))
      height = float(input("Enter the height of the room: "))

      square_footage = compute_square_footage(length, width, height)
      gallons = gallons_needed(square_footage)

      print(f"\nThe room requires {gallons:.2f} gallons of paint.\n")

if __name__ == "__main__":
  main()
