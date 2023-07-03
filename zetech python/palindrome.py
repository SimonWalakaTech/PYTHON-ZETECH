#a palidrome is a letter that when inverted it still reads the same like Madam

#prompt inputs
name = input("enter name")
#reverses the name
name2 = name.reverse()

if name == name2:
    print(name ,"is a palindrome")
    
else:
    print(name," is not a palindrome")