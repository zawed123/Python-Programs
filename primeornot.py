# https://www.facebook.com/graeyaki/posts/3604553256276181
# Subscribed by Pranav Kumar Mishra



num = int(input("Enter a number: "))


if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

#
else:
    print(num, "is not a prime number")
