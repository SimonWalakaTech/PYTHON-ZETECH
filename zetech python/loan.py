#to qualify for loan one must be 21 years old or more and least income of 21,000 to get loan

#prompt inputs

age = int(input("enter age: "))
income = int(input("enter income: "))
# use looping to check criteria
if age>=21 and income==21000:
    print("conguratulations you qualify for loan")
    
    
else:
    print("unfortunately we are not able to offer you a loan")