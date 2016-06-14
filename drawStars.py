def draw_stars(mylist):
    for item in mylist:
        if (type(item) == int):
            print("*" * item)
        else:
            print(item[0].lower()*len(item))

x = [4, "David", 2, "Tess", 2, "Jessica", 10]

draw_stars(x)
