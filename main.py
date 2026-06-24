from core.vector import Vector

position = Vector(0,0,0)

direction = Vector(0,0,1)

step = 0.5

new_position = position + direction * step

print(new_position)