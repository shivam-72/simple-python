student_heights = input("Input a list of student heights ").split()
count=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count = count+student_heights[n]
print(round(count/n))