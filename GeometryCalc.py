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

class MathFormulas:
    def __init__():
        return True

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

    def cubeArea():
        return a*a*6

    def cubeVolume():
        return a*a*a

    def cuboidArea():
        return (a*b*2)+(a*c*2)+(b*c*2)

    def cuboidVolume():
        return a*b*c

    def sphereArea():
        return ma.pi*diameter**2

    def sphereVolume():
        return 1/6*(ma.pi*diameter**3)

    def coneArea():
        a = diameter/2
        return ma.pi*a*(a+s)

    def coneVolume():
        return (1/12)*ma.pi*(diameter**2)*h

    def pyramidArea():
        return a*(a+ma.sqrt(4*(h**2)+a**2))

    def pyramidVolume():
        return 1/3*a**2*h

    def tetraedrArea():
        return ma.sqrt(3)*a**2

    def tetraedrVolume():
        return ma.sqrt(2)/12*a**3

    def cylinderArea():
        b = obj.circleArea()
        c = obj.circlePerimeter
        return c*h+2*b

    def cylinderVolume():
        b = obj.circleArea()
        return b*h

obj = MathFormulas


while(nextone.lower()=="y"):
    print("Currently functioning:\n2D objects: square, rectangle, triangle, circle, semicircle, oval, parallegram, trapezoid\n")
    print("3D objects: cube, cuboid, sphere, cone, pyramid, tetraedr, cylinder\n")
    try:
        Definition = str(input("Which object do you want to calculate?: "))
        if(Definition=="square" or Definition=="rectangle" or Definition=="triangle" or Definition=="circle" or Definition=="semicircle" or Definition=="oval" or Definition=="parallegram" or Definition=="trapezoid"):
            AreaOrSides = str(input("Do you want area or perimeter?: "))
        else:
            AreaOrSides = str(input("Do you want area or volume?: "))


        if (Definition.lower() == "square"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = obj.squareArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = obj.squarePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "rectangle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = obj.rectangleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = obj.rectanglePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "triangle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0 or c <=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = obj.triangleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0 or c<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = obj.trianglePerimeter()
                print(f"The perimeter equals to: {result}")
       
        elif(Definition.lower() == "circle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = obj.circleArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = obj.squarePerimeter()
                print(f"The perimeter equals to: {result}")
        
        elif(Definition.lower() == "semicircle"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = obj.circleArea()
                print(f"The area equals to: {result/2}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0):
                    a = float(input("What is the length of the diameter?: "))
                result = obj.squarePerimeter()
                print(f"The perimeter equals to: {result/2}")
        
        elif(Definition.lower() == "oval"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of the halfaxis a?: "))
                    b = float(input("What is the length of the halfaxis a?: "))
                result = obj.ovalArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of the halfaxis a?: "))
                    b = float(input("What is the length of the halfaxis a?: "))
                result = obj.ovalPerimeter()
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
                    result = obj.parallelgramArea()
                else:
                    while(a<=0 or b<=0 or alpha<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        alpha = float(input("How big is alpha? (use radians, if you don't enter 0): "))
                        if(alpha==0):
                            alpha = float(input("How big is alpha? (use degrees): "))
                            alpha = ma.radians(alpha)
                    result = obj.parallelgramArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                result = obj.rectanglePerimeter()
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
                    result = obj.trapezoidArea()
                else:
                    while(a<=0 or b<=0 or c<=0 or d<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        c = float(input("What is the length of side c?: "))
                        d = float(input("What is the length of side d?: "))
                    result = obj.trapezoidArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "perimeter"):
                while(a<=0 or b<=0 or c<=0 or d<=0):
                        a = float(input("What is the length of side a?: "))
                        b = float(input("What is the length of side b?: "))
                        c = float(input("What is the length of side c?: "))
                        d = float(input("What is the length of side d?: "))
                result = obj.trapezoidPerimeter()
                print(f"The perimeter equals to: {result}")




                #3D objects




        elif(Definition.lower() == "cube"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = obj.cubeArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(a<=0):
                    a = float(input("What is the length of the side?: "))
                result = obj.cubeVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "cuboid"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or b<=0 or c<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = obj.cuboidArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(a<=0 or b<=0 or c<=0):
                    a = float(input("What is the length of side a?: "))
                    b = float(input("What is the length of side b?: "))
                    c = float(input("What is the length of side c?: "))
                result = obj.cuboidVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "sphere"):
            if(AreaOrSides.lower() == "area"):
                while(diameter<=0):
                    diameter = float(input("What is the length of the diameter?: "))
                result = obj.sphereArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(diameter<=0):
                    diameter = float(input("What is the length of the diameter?: "))
                result = obj.sphereVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "cone"):
            if(AreaOrSides.lower() == "area"):
                while(s<=0 or diameter<=0):
                    diameter = float(input("What is the length of the diameter?: "))
                    s = float(input("What is the length of side s?: "))
                result = obj.coneArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(h<=0 or diameter<=0):
                    diameter = float(input("What is the length of the diameter?: "))
                    h = float(input("What is the length of the height?: "))
                result = obj.coneVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "pyramid"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0 or h<=0):
                    a = float(input("What is the length of the side?: "))
                    h = float(input("What is the length of the height?: "))
                result = obj.pyramidArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(a<=0 or h<=0):
                    a = float(input("What is the length of the side?: "))
                    h = float(input("What is the length of the height?: "))
                result = obj.pyramidVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "tetraedr"):
            if(AreaOrSides.lower() == "area"):
                while(a<=0):
                    a = float(input("What is the length of side a?: "))
                result = obj.tetraedrArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(a<=0):
                    a = float(input("What is the length of side a?: "))
                result = obj.tetraedrVolume()
                print(f"The volume equals to: {result}")
        

        elif(Definition.lower() == "cylinder"):
            if(AreaOrSides.lower() == "area"):
                while(diameter<=0 or h<=0):
                    h = float(input("What is the length of the height?: "))
                    diameter = float(input("What is the length of the diameter?: "))
                result = obj.cylinderArea()
                print(f"The area equals to: {result}")
            elif(AreaOrSides.lower() == "volume"):
                while(diameter<=0 or h<=0):
                    h = float(input("What is the length of the height?: "))
                    diameter = float(input("What is the length of the diameter?: "))
                result = obj.cylinderVolume()
                print(f"The volume equals to: {result}")
    except:
        print("Oops, something went wrong...")

    nextone = str(input("Do you want to continue?(y/n): "))
    print("\n\n\n")
