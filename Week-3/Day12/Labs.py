# Lab 1
course = "Web Development Bootcamp"
duration = 12

def type(course):
    print("Opss!")

print(course)
print(duration)
print(type(course)) #print opss!, beacuse nearest function | before def type print str
print(globals()) # print all global variables

# Lab 2
building = "Tuwaiq Academy"
cohort_size = 20

print(f"Welcome to {building}, class limit is  {cohort_size}")
print("Tuwaiq" in building)
print("cohort_size" in globals())
print(globals()["building"])

# Lab 3 
location = "Global"
def outter():
    location = "Outter"
    print(f"From outter: {location}")
    def inner():
        location = "Inner"
        print(f"From inner: {location}")

    inner()
    
outter()

# Lab 4
def outter():
    location = 1
    print(f"From outter: {location}")
    def inner():
        nonlocal location #nonlocal
        location += 2
        print(f"From inner: {location}")

    inner()
    
outter()

# Lab 5
def printer():
    print("Welcome World")

def desk():
    printer()

def room():
    desk()

def house():
    room()

def city():
    house()

def country():
    city()

country()

# Lab 6
language = "Python"

def show_lang(language):
    print(language)

show_lang("Dart")
print(language)

# Lab 7
rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total

#Its the same
print(f"Total: {getTotal(199.99):.2f}")
print(round(getTotal(199.99), 2))

# Lab 8 
def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])

inspect_order("Pen", 10)
