#any amount that exceeds 1000 gets a 5% discount

#prompt inputs
discount = 0.05
amountSpend = int(input("enter amount spend: "))
discoumount = discount*amountSpend
pay = amountSpend-discoumount
if amountSpend <=1000:
    print("no discount for amount",amountSpend)

elif amountSpend>1000:
    print("after discount pay: ",pay)
