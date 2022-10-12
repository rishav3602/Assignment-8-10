'''
1. Count the number of times iNeuron appears in the string.

text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"
'''

text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron "
print(text.count("iNeuron"))


'''
2. Check if position 5 to 11 ends with the phrase iNeuron. in the string

txt = "Hello, welcome to FSDS 2.0 at iNeuron.
'''

txt = "Hello, welcome to FSDS 2.0 at iNeuron"
if (txt[5:12]) == "iNeuron":
    print(f"Yes, it has iNeuron at this given position")
else:
    print(f"No, it doesn't has iNeuron at this given position")


'''
3.  Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Sunny Bhaveen Chandra, then the output should be S.B.Chandra.
    
'''

name = input("Enter your full name : ")
first_name = name[0:1]
middle_name = name[7:8]
last_name = name[13:]
print(f"{first_name}.{middle_name}.{last_name}")


'''
4.Join all items in a list into a string, using a hash(#) character as separator:

LIST = ["My", "name", "is", "Rishav", "Dash"]

'''



LIST = ["My", "name", "is", "Rishav", "Dash"]

print(f"{LIST[0]} # {LIST[1]} # {LIST[2]} # {LIST[3]} # {LIST[4]}")


'''
5.Write example for the following string manipulation function,

- isdecimal()
- islower()
- isupper()
- isalpha()
- isnumeric()

'''
num = 1234345
name = input("Enter your name : ")
print(f"The name is in lower form : {name.islower()}")
print(f"The name is in upper form : {name.isupper()}")



'''
6.Indian PAN card format follows the following formats -

AYEPC7894X
ABCDE9999Y Take user input for PAN_CARD and validate as per the above example.

'''

PAN_CARD = input("Enter your Indian pan card number : ")
if  PAN_CARD.isalnum() and PAN_CARD[0:5].isalpha() and PAN_CARD[5:9].isdigit() and  PAN_CARD[9].isalpha() and len(PAN_CARD) is 10 :
    print(f"The given card number is valid.")
else:
    print("Invalid card number")



