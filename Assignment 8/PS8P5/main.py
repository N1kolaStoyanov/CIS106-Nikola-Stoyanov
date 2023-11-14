f = open("data.txt" , "r")
tt = 0
c = 0

lastname = str(f.readline().rstrip('\n'))

while lastname != "":
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())

  if dcode == "I":
    cpc = 250 
  else :
    cpc = 500
  
  tuition = cpc * credits
  c = c + 1
  tt = tt + tuition


  print("Student: " ,lastname)
  print("Credits taken " ,credits)
  print("Tuition owed" ,tuition)
    
  lastname = str(f.readline().rstrip('\n'))

f.close()

print("Number of students: ", c)
print("Total Tuition owed by all:" ,tt)
