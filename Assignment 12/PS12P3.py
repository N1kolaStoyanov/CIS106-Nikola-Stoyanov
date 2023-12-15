def load_data_from_file(file_path):
  last_names = []
  scores = []

  try:
      with open(file_path, 'r') as file:
          for line in file:
              data = line.strip().split(',')
              last_name = data[0]
              score = int(data[1])
              last_names.append(last_name)
              scores.append(score)
  except FileNotFoundError:
      print(f"File '{file_path}' not found.")
  except Exception as e:
      print(f"Error loading data: {e}")

  return last_names, scores

def display_student_info(last_names, scores):
  print("Student Information:")
  for i in range(len(last_names)):
      print(f"Name: {last_names[i]}, Score: {scores[i]}")

def display_highest_lowest(last_names, scores):
  if not last_names or not scores:
      print("No data available.")
      return

  high_var = 0
  low_var = 999
  high_index = low_index = 0

  for i in range(len(scores)):
      if scores[i] > high_var:
          high_var = scores[i]
          high_index = i
      if scores[i] < low_var:
          low_var = scores[i]
          low_index = i

  print("\nStudent with Highest Score:")
  print(f"Name: {last_names[high_index]}, Score: {high_var}")

  print("\nStudent with Lowest Score:")
  print(f"Name: {last_names[low_index]}, Score: {low_var}")

def main():
  file_path = "student_data.txt"  # Replace with the path to your file
  last_names, scores = load_data_from_file(file_path)

  # Display student information
  display_student_info(last_names, scores)

  # Display student with highest and lowest scores
  display_highest_lowest(last_names, scores)

if __name__ == "__main__":
  main()
