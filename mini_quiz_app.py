score=0 # score variable keeps the track of the points scored in the qiuz
print("Welcome to the quiz!!!!!\n Lets Begin.....")
print("1.What is 2**3 ?")
print("a. 9\tb. 16\nc. 20\td. 8")
answer=input("Enter the correct option:")
if answer.lower()=='d':
    print("Correct answer!!!")
    score+=5
else:
    print("Your answer is wrong")
print("Next Question")
print("2.What is ((4/7)+(2*3)) ?")
print("a. 4.86\tb. 6.57\nc.9.64\td. 10")
answer=input("Enter the correct option:")
if answer.lower()=='b':
    print("Correct answer!!!")
    score+=5
else:
    print("Your answer is wrong")
print("Next Question")
print("3.What is 25% of 200 ?")
print("a. 100\tb. 50\nc. 175\td. 150")
answer=input("Enter the correct option:")
if answer.lower()=='b':
    print("Correct answer!!!")
    score+=5
else:
    print("Your answer is wrong")
if score>10:
    print("Score:",score)
    print("Your performance was very good!!!!")
elif score>5:
    print("Score:",score)
    print("Performance was average")
elif score>0:
    print("Score:",score)
    print("You need to work hard")
else:
    print("Score:",score)
    print("Poor Performance \nBetter luck next time")
exit()
