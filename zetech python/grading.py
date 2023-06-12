while True:
    mark1 = int(input("Enter the mark1: "))
    if mark1 > 0:
        break
    print("Error: Enter valid mark1")
while True:
    mark2 = int(input("Enter the mark2: "))
    if mark2 > 0:
        break
    print("Error: Enter valid mark2.")
while True:
    mark3 = int(input("Enter the mark3: "))
    if mark3 > 0:
        break
    print("Error: Enter valid mark3")
while True:
    mark4 = int(input("Enter the mark4: "))
    if mark4 > 0:
        break
    print("Error: Enter valid mark4.")

average = (mark1+mark2+mark3+mark4)/4

if average <=100 and average >=70:
    print("A")
elif average <=69 and average >=60:
    print("B")
elif average <=59 and average >=50:
    print("C")
elif average <=49 and average >=40:
    print("D")

elif average <=49 and average>=0:
    print("FAIL")

else:
    print("Invalid mark Entry")



try:
    mark1 = int(input("Enter the mark1: "))
except ValueError:
    print("Error: Please enter a valid number.")



# 70 - 100 A, 60-69B, 50-59C, 40-49D, 0-39 fail