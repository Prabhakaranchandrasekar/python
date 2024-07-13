Name=input("Enter your name:")
Age=int(input("Enter your age:"))
print("Name:",Name)
print("Age:",Age)

detail={"Name:":"Raja","Age:":25,"Contact:":9962457545}
for x in detail:
    print(x,detail[x])


person=int(input("Enter the number of persons:"))
for x in range(1,person+1):
  Name=input("Enter your name:")
  Age=int(input("Enter your age:"))
  print("Name:",Name)
  print("Age:",Age)

person = int(input("Enter the number of persons: "))
for x in range(1, person + 1):
 Name = input(f"Enter name of person {x}: ")
 Age = int(input(f"Enter age of person {x}: "))
 print(f"Name: {Name}")
 print(f"Age: {Age}")