
def area_rectangle(a,b):
    area = (a)*(b)
    return area

print(area_rectangle(2.5,2))

while True:
    length = input("Please enter a length \n ")
    width = input("Please enter a width \n")
    try:
        length = int(length)
        width = int(width)
        print("The length of the rectangle is {} and the width is {}". format(length,width))
        print("The area of the rectangele is {} meters square".format(area_rectangle(length,width)))
        break;
    except ValueError:
        try:
            float_length = float(length)
            float_width = float(width)
            print("The length of the rectangle is {} and the width is {}". format(float_length,float_width))
            print("The area of the rectangele is {} meters square".format(area_rectangle(float_length,float_width)))
            break;
        except ValueError:
            print("please enter valid numbers")