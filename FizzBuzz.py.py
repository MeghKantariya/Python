#FIZZ-BUZZ CODING INTERVIEW QUESTION

a=range(1,101)

for i in a:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)  

