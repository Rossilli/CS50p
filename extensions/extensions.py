def main():
    #get input
    ftype = input("File name: ")
    ftype = ftype.lower().strip()

    #print image
    if ftype.endswith("jpg") or ftype.endswith("jpeg"):
        print("image/jpeg")
    elif ".gif" in ftype:
        print("image/gif")
    elif ".png" in ftype:
        print("image/png")
    elif ".zip" in ftype:
        print("application/zip")
    elif ".pdf" in ftype:
        print("application/pdf")
    elif ".txt" in ftype:
        print("text/plain")
    else:
        print("application/octet-stream")

main()