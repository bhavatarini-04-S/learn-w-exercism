def equilateral(sides):
    a,b,c=sorted(sides)
    if (a>0 and b>0 and c>0) and a==b==c:
        return True
    else:
        return False
    
def isosceles(sides):
    a,b,c=sorted(sides)
    if a+b<=c:
        return False
    return a==b or b==c or a==c

def scalene(sides):
    a,b,c=sorted(sides)
    if a==b or b==c or a==c or a+b<=c:
        return False
    else:
        return True
    
