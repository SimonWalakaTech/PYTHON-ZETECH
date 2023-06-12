timeofservice = int(input("enter period of service"))
salary = int(input(" Enter salary"))
if timeofservice >10:
    bonus = salary*0.1
    print(bonus)

elif timeofservice <=10 and timeofservice >=6:
    bonus = salary*0.08
    print(bonus)

elif timeofservice <6:
    bonus = salary*0.05
    print(bonus)

else:
    print("out of range")


