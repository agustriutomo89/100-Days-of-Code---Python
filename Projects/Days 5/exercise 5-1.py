# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalStudents = 0
totalScores = 0

for student_height in student_heights:
  totalStudents += 1
  totalScores += student_height

average_score = round(totalScores/totalStudents)
print(average_score)






