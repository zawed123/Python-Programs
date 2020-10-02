a = input("Enter your number here ")
b = input("Enter your number here ")
try:
    print(int(a)+int(b))
except Exception as e:
    print(e)