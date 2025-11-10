global_message = "Döner global"

def show_variables():
    print("Global message:", global_message)
    local_message = "Döner local."
    print("Local message:", local_message)

show_variables()


counter = 0

def increment_counter():
    global counter
    counter += 1

print("counter:", counter)
increment_counter()
print("After 1:", counter)
increment_counter()
increment_counter()
print("After 3:", counter)



import math

print("Square root of 144:", math.sqrt(144))
print("Value of Pi:", math.pi)
print("2 to the power of 5:", math.pow(2, 5))


import my_functions

print(my_functions.greet_user("Denys"))
print("10 / 2 =", my_functions.divide(10, 2))
print("10 / 0 =", my_functions.divide(10, 0))
