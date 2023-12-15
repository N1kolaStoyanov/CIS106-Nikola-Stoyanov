class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition_owed(self):
      if self.district_code == 'I':
          tuition_rate = 250.00
      else:
          tuition_rate = 500.00

      tuition_owed = self.enrolled_credits * tuition_rate
      return tuition_owed

def main():
  # Test the class by instantiating an object and adding data
  student1 = Student("John", "Doe", "I", 12)
  student2 = Student("Jane", "Smith", "O", 15)

  # Display tuition owed for each student
  print(f"{student1.first_name} {student1.last_name} owes ${student1.compute_tuition_owed():.2f} in tuition.")
  print(f"{student2.first_name} {student2.last_name} owes ${student2.compute_tuition_owed():.2f} in tuition.")

if __name__ == "__main__":
  main()
