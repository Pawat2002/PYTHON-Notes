# to create a function we need to begin with def

def say_hi(name, age):
    print("Hello " + name + ", you are " + age + ".")

say_hi("Mike", "35")
say_hi("Steve", "40")

# a Function with return statement

def cube(num):
    return num*num*num
result = cube(3)
print("the cube of three is " + str(result))




