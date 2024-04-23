import math

def roots(a, b, c):
    
    det = b**2 - 4*a*c


    if det > 0:
        return f"({(-b + math.sqrt(det))/2*a}, {(-b - math.sqrt(det))/2*a})" 

    elif det == 0:
        return f"({-b/2})"

    elif det < 0:
        return f"( )"     


def value_y(a, b, c, x):
    return (a*(x**2))+(b*x)+(c)


def to_string(a, b, c):
    if (a != 0) and (b != 0) and (c != 0):
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

    elif (a == 0) and (b != 0) and (c != 0):
        return f"f(x) = {b} * X + {c}"

    elif (a == 0) and (b == 0) and (c != 0):
        return f"f(x) = {c}"

    elif (a != 0) and (b == 0) and (c != 0):
        return f"f(x) = {a} * X^2 + {c}"

    elif (a!= 0) and (b != 0) and (c == 0):
        return f"f(x)= {a} * X^2 + {b} * X"

    elif (a == 0) and (b != 0) and (c != 0):
        return f"f(x) = {b} * X + {c}"

    elif (a != 0) and (b == 0) and (c == 0):
        return f"f(x)= {a} * X^2"

    elif (a == 0) and (b != 0) and (c == 0):
        return f"f(x)= {b} * X"

    elif (a == 0) and (b == 0) and (c == 0):
        return f"f(x)= 0"

    


def derivation(a, b, c):
    if a != 0 and b!= 0:
        return f"f'(x) = {a*2} * X + {b}"
    elif a ==0 and b!= 0:
        return f"f'(x) = {b}" 
    elif a != 0 and b == 0:
        return f"f'(x) = {a*2} * X"
    else:
        return f"f'(x) = 0"

