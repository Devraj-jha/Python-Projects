#scope means where the variable is visible. 

##Python looks for variables in this order:

# Local

# Enclosing

# Global

# Built-in

x = 20 #global variable 

def sub(x,y):
    x = 10 #local variable 
    return y - x #returns a value

print(sub(x,10))

x = 10

def change():
    global x ## changes the variable outer ones. 
    
    x = 20

change()
print(x)   # 20



def outer():
    x = 1100

    def inner():
        print(x) #can't acess x here 

    inner()


def outer():
    x = 10

    def inner():
        nonlocal x 
        x = 20
      
        

    inner()
    print(x)

outer()

