import sys

def is_even(value):
  if value % 2 == 0:
    print(f"Value {value} is even")
    return True
  else:
    print(f"Value {value} is odd")
    return False


user_input = int(sys.argv[1])
result = is_even(user_input)
return result
# print("Hello World!")

# print(str(user_input))
# for i in range(user_input):
#   func(i)
