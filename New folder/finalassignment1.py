
length = int(input("Enter the length \n"))
width = int(input("Enter the width \n"))

if isinstance(length,int) and isinstance(width, int): 
     area = length * width
     print("The area of the rectangle is {} meters square".format(area))
    
else:
     print("Please enter an interger")
    

