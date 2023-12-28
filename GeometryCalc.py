import math as ma
import sys

a: float = 0
b: float = 0
c: float = 0
d: float = 0
s: float = 0
h: float = 0
alpha: float = 0
diameter: int =0
gon: int = 0
result: int = 0
yesno: str = ""
nextone: str = "y"

def rectangleArea():
    return a*b

def rectanglePerimeter():
    return (2*a)+(2*b)

def squareArea():
    return a*a

def squarePerimeter():
    return 4*a
    
def triangleArea():
    s = (a+b+c)/2
    return ma.sqrt(s*(s-a)*(s-b)*(s-c))

def trianglePerimeter():
    return a+b+c

def circleArea():
    return ma.pi*(diameter**2)/4
    
def circlePerimeter():
    return ma.pi*diameter

def ovalArea():
    return ma.pi*a*b

def ovalPerimeter():
    return ma.pi*ma.sqrt(2*(a**2+b**2))

def parallelgramArea():
    if(yesno=="y"):
        return a*h
    else:
        return a*b*ma.sin(alpha)

def trapezoidArea():
    if(yesno=="y"):
        return (a+c)*h/2
    else:
        s = (a+b+c+d)/2
        h = (2/(abs((a-c))))*ma.sqrt((s-a)*(s-c)*(s-b-c)*(s-d-c))
        return (a+c)*h/2
    
def trapezoidPerimeter():
        return a+b+c+d

while(nextone.lower()=="y"):
    print("Currently functioning:\n2D objects: square, rectangle, triangle, circle, semicircle, oval, parallegram, trapezoid\n")
    #print("3D objects: cube, cuboid, sphere, cone, pyramid, triangular pyramid (tripyr), cylinder, prism\n")
    try:
        Definition = str(input("Which object do you want to calculate?: "))
        AreaOrSides = str(input("Do you want area or perimeter?: "))


        if (Definition.lower() == "square"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = squareArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = squarePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "rectangle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = rectangleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = rectanglePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "triangle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0 or c <=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = triangleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0 or c<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = trianglePerimeter()
                print(f"The perimeter equals to: {result}")
       
        elif(Definition.lower() == "circle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = circleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = squarePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "semicircle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = circleArea()
                print(f"The area equals to: {result/2}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = squarePerimeter()
                print(f"The perimeter equals to: {result/2}")
        
        elif(Definition.lower() == "oval"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of the halfaxis a?: "))
                    b = float(input("What is the length of the halfaxis a?: "))
                result = ovalArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of the halfaxis a?: "))
                    b = float(input("What is the length of the halfaxis a?: "))
                result = ovalPerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "parallegram"):
            if(AreaOrSides.lower() == "area"):
                while(yesno!="y" and yesno!="n"):
                    yesno = str(input("Do you know height? (y/n): "))
                if(yesno=="y"):
                    while(a<=0 or h<=0):
                        print("Height must be perpendicular to the side you will enter!")
                        a = float(input("What is the length of the side?: "))
                        h = float(input("What is the length of the height?: "))
                    result = parallelgramArea()
                else:
                    while(a<=0 or b<=0 or alpha<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        alpha = float(input("How big is alpha? (use radians, if you don't enter 0): "))
                        if(alpha==0):
                            alpha = float(input("How big is alpha? (use degrees): "))
                            alpha = ma.radians(alpha)
                    result = parallelgramArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = rectanglePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "trapezoid"):
            if(AreaOrSides.lower() == "area"):
                while(yesno!="y" and yesno!="n"):
                        yesno = str(input("Do you know height? (y/n): "))
                if(yesno=="y"):
                    while(a<=0 or c<=0 or h<=0):
                        a = float(input("What is the length of side a?: "))
                        c = float(input("What is the length of side c?: "))
                        h = float(input("What is the length of the height?: "))
                    result = trapezoidArea()
                else:
                    while(a<=0 or b<=0 or c<=0 or d<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        c = float(input("What is the length of side c?: "))
                        d = float(input("What is the length of side d?: "))
                    result = trapezoidArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0 or c<=0 or d<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        c = float(input("What is the length of side c?: "))
                        d = float(input("What is the length of side d?: "))
                result = trapezoidPerimeter()
                print(f"The perimeter equals to: {result}")
