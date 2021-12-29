#            012345678901234
parrot =    "Norwegian Blue"

print(parrot)

# Negative Indexes start at the end of the string.
# The last character is at -1
print(parrot[-1])   # 'e'
print(parrot[-14])  # 'N'

# Slicing start:stop:step
print(parrot[0:6])  # Start at 0 and slice up to, but not including, position 6 (Norweg)
print(parrot[3:5])  # 'we'

print(parrot[0:9])  # "Norwegian" two different ways
print(parrot[:9])   # The 0 is implied
print(parrot[10:14])
print(parrot[10:])  # The ending location is optional
                    # The ':' is reqired to make a slice, otherwise it's an array
print(parrot[:])    # Fist and second number omitted returns the entire string.
#   slice using negative numbers
print('Slice using negative nunmbers')
print(parrot[-4:-2])    # Return from -4 character from teh end upto, but not including, -2 from the end

print("Slicing with step")
print(parrot[0:6:2])    # Slice with step 2
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

print('Slicing backwards')
letters = 'abcdefghijklmnopqrstuvwxyz'
backwards = letters[25:0:-1]
print(backwards)    # Missing the first letter 'a' because UP TO and NOT INCLUDING the stop value
backwards = letters[25::-1] # Omit 0 stop value to get all letters. Can also omit 25 since it's the end
print(backwards)    # Complete z to a

print('Python Idioms')
# [::-1] is a Python idiom to reverse the strung
print(letters[::-1])
# [-1:] returns the last character - Python idiom
print(letters[-1:])
# [:1] returns the first character - Python idiom
print(letters[:1])
