name = "brock"
age = 10
city = "happyvalleygoosebay"
print(f"hi my name is {name} and I am {age} years old. I currently live in {city}")

num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {num1 + num2}.") #numbers can be added

pi = 3.141592653589793
print(f"Value of pi: {pi:.3f}") # to control how many decimals are trailing in the end syntax is {variable:.lengthofstringf}
#if requested number is longer than length of string, extra 0s are added

num = 42
print(f"{num:<5}left-aligned")
print(f"{num:>5}right-aligned")
print(f"{num:^5}centered")
# makes the string position left middle or right. < is left, > is right, ^ is centered

num = 7
print(f"Number: {num:015d}")
#adds 0 to the start of the number. format is {variable:0numoflengthofstringd}
gum = 7
print(f"Number: {gum:.015f}")

value = 3.14
padded_value = f"{value:.5f}"  # Pad with two decimal places
print(f"Padded Value: {padded_value}")

value = 3.14
print(f"Padded Value: {value:.5f}")

value = 123.456789
print(f"Value: {value:10.2f}")
#the 10 is how far to the left it should be

number = 1000000
print(f"Large Number: {number:,}")
#adds commas for numbers

name = "ray"
print(f"my name is {name}")

num = 3.14  
print(f"your total is {num:.6f}")