test_case=int(input())   #number of test cases


for i in range(test_case):
    number=input()       #input  number is converted into string
    y = number[len(number) - 1:0:-1] + number[0]    #reverse of the number is obtained

    #the number and reverse number are compared
    if number==y:
        print("wins")
    else:
        print("losses")




