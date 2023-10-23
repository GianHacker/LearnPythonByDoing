if __name__ == "__main__":
    whandle = open("Python101\\test.txt") # default mode is to read also the path isn't considered as raw string
    dataa = whandle.read()
    print(dataa)

    print("**************************************************************")

    whdl = open(r"Python101\test.txt", "r") #
    dat = whdl.read()
    print(dat)

    print("**************************************************************")

    handle = open(r"D:\learning\LearnPythonByDoing\Python101\test.txt", "r")
    data = handle.read()
    print(data)
    handle.close()

    print("**************************************************************")

    handl = open(r"Python101\test.txt")
    da_ta = handl.readline() # Reads only one line 
    print(da_ta)
    handl.close() # Closing the opened file

    print("**************************************************************")

    han = open(r"Python101\test.txt")
    dat_a = han.readlines() # Read ALL the lines & print as list
    print(dat_a)
    han.close()

    print("**************************************************************")
    hana = open(r"Python101\test.txt")
    for h in hana:
        print(h)
    han.close()

    maha = open(r"Python101\Mahabharata.pdf", "rb")
    while True:
        d = maha.read()
        print(d)
        if not d:
            break