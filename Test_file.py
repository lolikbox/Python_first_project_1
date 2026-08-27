def square(num):
    return num * num


def annual_salary(num):
    return num*365

def star(n):
    for i in range (n):
        for j in range (n-1-i):
            print (" ", end="")
        for k in range(2*i + 1):
            print ("*", end="")
        print(" ")

print('Square of your number is ',square(int(input('Enter a number: '))))
print('Your annual salary is ',annual_salary(int(input('Enter a daily profit: '))))
star(int(input('Enter a number of lines: ')))