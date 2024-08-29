from PIL import Image,ImageOps
import sys
shirt = Image.open("shirt.png")
size = shirt.size
with Image.open(sys.argv[1]) as im:
    new_im = ImageOps.fit(im,size)
    new_im.paste(shirt,(0,0))
    new_im.save("new.jpg")









#resize to the exact size of the photo, then decide which part to mask on the original photo

