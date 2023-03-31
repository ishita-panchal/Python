name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
     print("Your age is minor.")
elif age>=18 and age<65:
     print("You are an adult.")
elif age >= 65:
     print("You are an senior.")
else:
     print("not specified")
  