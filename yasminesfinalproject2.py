#code to add numbers together for the test score
math_test = int(input("what did you score on your math test? :"))
science_test = int(input("what grade did you get on your science test? :"))
english_test = int(input("what did you get on your english exam? :"))
history_test = int(input("what did you score on your history quiz? :"))
test_total = math_test + science_test + english_test + history_test
test_average = test_total/4
print(test_total)
print(test_average)
fifty_percent = test_average*.5
print(fifty_percent)

#code to add numbers together for the homework score
math_homework = int(input("what did you score on your math homework? :"))
science_homework = int(input("what grade did you get on your science homework? :"))
english_homework = int(input("what did you get on your english homework ? :"))
history_homework = int(input("what did you get on your history homework? :"))
homework_total = math_homework + science_homework + english_homework + history_homework
homework_average = homework_total/4
print(homework_total)
print(homework_average)
ten_percent = homework_average*.5
print(ten_percent)

math_midterm = int(input("what did you score on your math midterm? :"))
science_midterm = int(input("what grade did you get on your science midterm? :"))
english_midterm = int(input("what did you get on your english midterm? :"))
history_midterm = int(input("what did you get on your history midterm? :"))
midterm_total = math_midterm + science_midterm + english_midterm + history_midterm
midterm_average = midterm_total/4
print(midterm_total)
print(midterm_average)
thirty_percent = midterm_average*.5
print(fifty_percent)

#code to add numbers together for the participation score
participation_grade = int(input("what did you get for your participation grade? :"))
print(participation_grade)
twenty_percent = participation_grade*.2
print(twenty_percent)

text = input("how do you think you did? :")
text = input("are you ready to see how you scored? :")
print("DRUMROLL PLEASE...")


final_score = twenty_percent + thirty_percent + fifty_percent
print("your final score is...",final_score)

#code to get averages
test_average8 = test_total / 3
homework_average = homework_total / 3

#code to get the final scores for each seperate category
test_total = test_average* 0.5
homework_total = homework_average* 0.3
participation_grade = participation_grade * 0.2

#code to get final number grade
grade = test_total + homework_total + participation_grade
print(grade)

#code to transfer number grade into letters
if grade >= 96 and grade <= 100:
    print("you got an A+, great job!")
elif grade >= 92:
    print("you got an A, good job!")
elif grade >= 90:
    print("you got an A-, yayyy")
elif grade >= 86:
    print(" you got a B+")
elif grade >= 83:
    print("you got a B")
elif grade >= 80:
    print("you got a B-")
elif grade >= 76:
    print("you got a C+")
elif grade >= 73:
    print("you got a C")
elif grade >= 70:
    print("you got a C-")
elif grade >= 66:
    print("you got a D+")
elif grade >= 63:
    print("you got a D")
elif grade >= 60:
    print("you got a D-")
elif grade >= 53:
    print("you got an F,but that's fine, try again next time..")
elif grade >= 0:
    print("your in the negatives ToT...")
else:
    print("Invalid Scores")
    