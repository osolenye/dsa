def greet(name):
    print(f'hi {name}!')
    greet2(name)
    print("getting ready to say goodbye...")
    bye(name)

def greet2(name):
    print(f'how you doin {name}?')
def bye(name):
    print(f'goodbye {name}?')

greet("bekzat")


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

print(fact(5))
