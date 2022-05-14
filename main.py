# I think I was trying to write this with no 'if' statements? Not sure

print("\033[0;37;1;33mFirst Base (2-10):\n")
base1=input()

print("\nSecond Base (2-10):\n")
base2=input()

i2 = 1 
binary2 = 0

print("\n\033[0;37;1;33mPlease enter a positive integer in base %s to be coverted into base %s: \n"%(base1,base2))

number = input()
i = 1
binary = 0   

# if base1.isdigit() != True or base2.isdigit() != True or number.isdigit() != True: print("YOU UTTER FOOL"); exit()

while int(number) > 0:
  number = int(number)
  binary = int(binary)
  base1 = int(base1)
  base2 = int(base2)
  mod = number % 10
  number = number // 10
  binary += mod*i
  i *= base1
  
while binary > 0: 
  mod2 = binary % base2
  binary = binary // base2
  binary2 += mod2*i2
  i2 *= 10
  
print("\033[0;37;1;32m"); print(binary2, "\n")