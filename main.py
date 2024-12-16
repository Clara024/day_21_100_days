print("Math Multiplication Calculator")

#Get user input for the multiple needed
m = int (input("Name the multiple of your choice:"))
counter =0
for i in range(1,11):
  a= i * m
  print( i ,"x",m)
  answer = int(input("What is the answer?:"))
  if answer == a:
    print("That is correct!!")
    counter += 1
  else:
    print("That is wrong, It should have been",a)
  if counter == 10:
    print("What a perfect score now")
  else:
    print ("You scored",counter,"out of 10")