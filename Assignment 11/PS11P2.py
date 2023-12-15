def compute_exam_stats(scores):
  total_points = sum(scores)
  average_score = total_points / len(scores)
  return total_points, average_score

def main():
  last_name = input("Enter the student's last name: ")
  exam_scores = []

  for i in range(3):
      score = float(input(f"Enter exam score {i + 1}: "))
      exam_scores.append(score)

  total_points, average_score = compute_exam_stats(exam_scores)

  print(f"\nStudent Last Name: {last_name}")
  print(f"Total Points: {total_points}")
  print(f"Average Exam Score: {average_score:.2f}")

if __name__ == "__main__":
  main()
