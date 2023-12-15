def display_student_info(last_names, exam_scores):
  print("Student Information:")
  for i in range(len(last_names)):
      print(f"Name: {last_names[i]}, Exam Score: {exam_scores[i]}")

def display_student_info_reverse(last_names, exam_scores):
  print("\nStudent Information in Reverse Order:")
  for i in range(len(last_names) - 1, -1, -1):
      print(f"Name: {last_names[i]}, Exam Score: {exam_scores[i]}")

def main():
  # Arrays of last names and exam scores (parallel arrays)
  last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
  exam_scores = [85, 90, 78, 92, 88, 95, 87, 89, 79, 93]

  # Display student information
  display_student_info(last_names, exam_scores)

  # Display student information in reverse order
  display_student_info_reverse(last_names, exam_scores)

if __name__ == "__main__":
  main()
