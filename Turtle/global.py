side_length = 100

def draw_square():
    global side_length
    side_length = 200
    print("side_length: ", side_length)

print(side_length)
draw_square()
print(side_length)