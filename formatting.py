for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("Left justified")
# Left justify using the < sign
# Use ^ to center
for i in range(1,13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Specify display precision")
print("Pi is approximately {0:12}".format(22 / 7))
# Floating point - default 6 digits
print("Pi is approximately {0:<12f}".format(22 / 7))
print("Pi is approximately {0:<12.50f}".format(22 / 7))
print("Pi is approximately {0:<52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))

# Using f-strings
print("f-string formatting")
print(f"pi is approximately {22 / 7:12.50f}")
pi = 22/7
print(f"pi is approximately {pi:12.50f}")

