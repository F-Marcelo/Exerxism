def equilateral(sides):
    if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[2] + sides[0] >= sides[1]:
            if sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[0]:
                return True
            return False
        return False
    return False

print(equilateral([0,0,0]))

def isosceles(sides):
    if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[2] + sides[0] >= sides[1]:
            if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
                return True
            return False
        return False
    return False        


def scalene(sides):
    if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[2] + sides[0] >= sides[1]:
            if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0] :
                return True
            return False
        return False
    return False
