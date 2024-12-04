import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("This is geometry calculator!")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your figure (1/2/3): ")

    if choice == "1":
        radius = float(input("Enter the radius of the circle:  "))
        print(f"The radius of the circle is: {area_circle(radius)}")
    elif choice == "2":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the triangle is: {area_rectangle(length, width)}")
    elif choice == "3":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(base, height)}")
    else:
        print("Input is incorrect")

if __name__ == "__main__":
    main()