cisla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

for i in cisla:
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)