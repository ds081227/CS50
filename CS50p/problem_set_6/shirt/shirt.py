import sys
import os
from PIL import Image,ImageOps
def main():
    length_check()
    extension_check1()
    convert()

def length_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        return True

def extension_check1():
    extension_list = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1].lower())[1]
    ext2 = os.path.splitext(sys.argv[2].lower())[1]
    if ext1 in extension_list and ext2 in extension_list:
        if ext1 == ext2:
            return True
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")
def convert():
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(sys.argv[1]) as im:
        new_im = ImageOps.fit(im,size)
        new_im.paste(shirt,(0,0),shirt)
        new_im.save(sys.argv[2])




if __name__ == "__main__":
    main()

