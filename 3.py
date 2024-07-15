subject1 = float(input("Enter marks for subject 1: ")) 
subject2 = float(input("Enter marks for subject 2: ")) 
subject3 = float(input("Enter marks for subject 3: ")) 
subject4 = float(input("Enter marks for subject 4: ")) 
subject5 = float(input("Enter marks for subject 5: ")) 
 
# Calculating total marks 
total_marks = subject1 + subject2 + subject3 + subject4 + subject5 
 
# Calculating percentage 
percentage = (total_marks / 500) * 100 
 
# Assigning grade based on percentage 
if percentage >= 90: 
    grade = 'A+' 
elif percentage >= 80: 
    grade = 'A' 
elif percentage >= 70: 
    grade = 'B' 
elif percentage >= 60: 
    grade = 'C' 
elif percentage >= 50: 
    grade = 'D' 
else: 
    grade = 'F' 
 
# Displaying the results 
print("Total Marks:", total_marks) 
print("Percentage:", percentage) 
print("Grade:", grade) 