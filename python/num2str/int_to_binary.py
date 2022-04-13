# int_to_binary.py
# Convert integer to binary string
# Sparisoma Viridi | https://github.com/dudung/cookbook
# 20220413 Summarize and add some lines of examples.

# set an int
num = 11
print('num =', num)
print()

# set number of digits
digit = 6
print('digit =', digit)
print()


# url https://stackoverflow.com/a/63485151/9475509 [20220413]
numbs1 = f'0b{num:08b}'
print("f'0b{num:08b}'")
print(numbs1)
print()

# print without prefix '0b' and in 10 digit, with leading '0'
numbs2 = f'{num:010b}'
print("f'{num:010b}'")
print(numbs2)
print()

# print without leading '0'
numbs3 = f'{num:b}'
print("f'{num:b}'")
print(numbs3)
print()


# url https://stackoverflow.com/a/62587270/9475509 [20220413]
numbs4 = bin(num)
print('bin(num)')
print(numbs4)
print()

# print without prefix '0b'
numbs5 = bin(num)[2:]
print('bin(num)[2:]')
print(numbs5)
print()


# url https://stackoverflow.com/a/53275552/9475509 [20220413]
numbs6 = format(num, '06b')
print("format(num, '06b')")
print(numbs6)
print()


# url https://stackoverflow.com/a/55932455/9475509 [20220413]
numbs7 = format(num, '0{}b'.format(digit))
print("format(num, '0{}b'.format(digit))")
print(numbs7)
print()


# url https://stackoverflow.com/a/56500977/9475509 [20220413]
numbs8 = f'{num:0{digit}b}'
print("f'{num:0{digit}b}'")
print(numbs8)
print()


# define a binary number
bb = 0b1111 # 15
print("bb = 0b1111")
print("print(bb)")
print(bb)
print()

# define a hexadecimal number
cc = 0x17
print("cc = 0x17")
print("print(cc)")
print(cc)
print()

# add previous numbers as int
dd = bb + cc
print("dd = bb + cc")
print(f'{dd} = {bb} + {cc}')
print()
