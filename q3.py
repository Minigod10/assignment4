"""Write a multiplication game program for kids. The program should give the player
ten randomly generated multiplication questions to do. After each, the program
should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right."""
import random

for i in range(1,11):
    n=random.randint(1,10)
    s=random.randint(1,10)
    x=n*s
    print(n,"*",s,"=")
    ans=int(input("Your answer:"))
    if x==ans:
        print("Right")
    else:
        print("Wrong,the correct ans is",x)