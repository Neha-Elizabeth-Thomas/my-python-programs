
def sprinkle(func):
    def wrapper(*args,**kargs):
        print("I have added sprinkles for you")
        func(*args,**kargs)
    return wrapper

@sprinkle
def ice_cream(flavour):
    print(f"You are eating {flavour} ice creams")
    
ice_cream("choco")