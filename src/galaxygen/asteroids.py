from random import uniform

from . import propertyNode

def makeAsteroids(starName, max_asteroids):
    max = int(uniform(1, float(max_asteroids)))
    astContent = [] # lines of content to append to the file
    for _ in range(1, max):
        radiusBase = uniform(0,1) * 80000
        radius = int(radiusBase) + 5000
        astContent.append(propertyNode(
            description="When Jeb was originally shown a map of our galaxy he said 'Wow! Thats big! Dont suppose we get any rest stops out there do we?' This statement encouraged our scientists to look closer, And eventually this asteroid among many, Was discovered. Dont expect vending machines, And if you do find them... Dont expect candy.",
            radius=radius
        ))
    return astContent
