def compute_averages(scores, handicap):
  average_score = sum(scores) / len(scores)
  average_score_with_handicap = average_score + handicap
  return average_score, average_score_with_handicap

def main():
  last_name = input("Enter the bowler's last name: ")
  game_scores = []

  for i in range(3):
      score = float(input(f"Enter game score {i + 1}: "))
      game_scores.append(score)

  handicap = float(input("Enter the handicap: "))

  average_score, average_score_with_handicap = compute_averages(game_scores, handicap)

  print(f"\nBowler Last Name: {last_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Average Score with Handicap: {average_score_with_handicap:.2f}")

if __name__ == "__main__":
  main()
