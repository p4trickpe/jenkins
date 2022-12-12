import sys

def func(value):
  if value % 2 == 0:
    print(f"Value {value} is even")
  else:
    print(f"Value {value} is odd")


user_input = int(sys.argv[1])
print("Hello World!")
print(str(user_input))
for i in range(user_input):
  func(i)
