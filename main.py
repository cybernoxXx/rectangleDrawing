def drawRectangle(width, height):
    # If a dimension is 0 or negative I return none
    if width <= 0 or height <= 0:
        return None
    # Cycling on height
    for i in range(0,height):
        # Cycling on width to draw a row
        for j in range(0,width):
            # Checking if I'm printing the last character of the raw because I need to print a new row after this
            if j == width-1:
                print("#")
            # If I'm printing a row I shouldn't go newline everytime
            else:
                print("#", end='')

drawRectangle(10,8)
print("\n")
drawRectangle(2,3)
print("\n")
drawRectangle(3,0)
