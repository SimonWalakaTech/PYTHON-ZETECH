#for one to vote, they must be kenyan and 18 years or above
name = input("enter name")
age = int(input("enter age"))
country = input("enter country")
country == kenya

if age>=18 and country == kenya:
    #conditions allows only 18 and above kenyans to vote
    print("qualified to vote")
    
else:
    print("not qualified to vote")