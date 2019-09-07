#cookToCode

#This program is an introduction to "if statements"
#if statments are ways to compare values of a variable


#This program allows an unlimited amount of user inputs and assesses each input everytime

answer = 'y'

print('This program will tell you the class of your IP\n\n')
while answer == 'y':
    iP=(input('Enter an IP address:  '))
    iP_split=iP.split('.')          #<---This is the first instance of splitting a string
                                    #this code tells the computer to separate the value of iP between every "."
    first_octet = int(iP_split[0])  #<---After a string is split it is put in an array(we will talk about this later)
    #print(first_octet)
    if first_octet <= 127:          #<---The if statement is started with an "if" and has the same syntax as a function
        print(f'{iP} is Class A')
    elif first_octet <= 191:        #<----If the first if statement fails, then the code will check the next statement
        print(f'{iP} is Class B')
    elif first_octet <= 223:        #<----Same as above
        print(f'{iP} is Class C')
    else:                           #<---If all statements fail to be true, then the else statement is chosen
        print('Something went wrong...(your IP started with a number greater than 223)')
        print()
    answer = input('Would you like to enter another IP address?(y/n)  ')