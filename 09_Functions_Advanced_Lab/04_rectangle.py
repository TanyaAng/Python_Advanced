def rectangle (length,width):
    if not type(length)==int or not type(width)==int:
        return f"Enter valid values!"
    return f"Rectangle area: {area(length,width)}\nRectangle perimeter: {perimeter(length,width)}"

def area (length,width):
    return length*width

def perimeter(lenght, width):
    return 2*lenght+2*width


print(rectangle(2, 10))
print(rectangle('2', 10))


