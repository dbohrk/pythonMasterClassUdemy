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



