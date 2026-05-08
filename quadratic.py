# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    salida=""
    if a==0:print("no es posible")
    elif (b**2)-(4*a*c)==0:    
        salida=f"({(-b/(2*a))})"
    
    elif (b**2)-(4*a*c)<0:
        salida="( )"

    else:    
        r1=(-b+((b**2)-(4*a*c))**.5)/2*a

        r2=(-b-((b**2)-(4*a*c))**.5)/2*a

        salida=f"({r1}, {r2})"

    return salida


def value_y(a, b, c, x):
    salida=(a*(x**2)+(b*x)+c)

    return salida


def to_string(a, b, c):
    salida="f(x) ="
    if a==0: 
        if b==0:
            salida+=f" {c}"
            
        else:
            salida+=f" {b} * X "
            salida+=f"+ {c}"
            


    else:
        salida+=f" {a} * X^2 "
        if b==0:
            salida+=f"+ {c}"
            
        else:
            salida+=f"+ {b} * X "
            salida+=f"+ {c}"
            


    return salida


def derivation(a, b, c):
    salida=""
    if a!=0:
        if b!=0: salida= f"f'(x) = {a*2} * X + {b}"
        else: salida= f"f'(x) = {a*2} * X"
    else:
        if b!=0:salida= f"f'(x) = {b}"
        else: salida="f'(x) = 0"

    return salida
