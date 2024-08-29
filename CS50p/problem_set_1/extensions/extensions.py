#Input file name, strip whitespace, lowercase, and split the string to take only the last substring
mediatype = (input("File name: ").split('.')[-1].strip().lower())

#Identify the data type and print the corresponding data type
match mediatype:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")








