while True:
    print ("1 -- > Opening a File ")
    print ("2 -- > Adding Contents to a file ")
    print ("3 -- > Read The Contents of the File ")
    print ("4 -- > Count the Number of words ")
    print ("5 -- > Finding The Word ")
    print ("6 -- > Replacing the Word ")
    print ("7 -- > Converting to upper case and storing to other file ")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        print ("Enter the File Name to be opened: ")
        a = input("Enter The File Name \n")
        f = open(a,"w")
        print ("-"*60)
        print ("File ", a," is created ")
        print ("-"*60) 
    elif choice == 2:
        print ("Plz enter alteast Two Meaning Full Pharagraphs: ")
        b = input("Enter The contents:  \n")
        f.write(b)
        f.close()
        print ("-"*60)
        print ("Contents Added Successfully ")
        print ("-"*60)
    elif choice == 3:
        print ("Displaying the Contents of the File ")
        f = open(a,"r")
        c = f.read()
        print ("-"*60)
        print (c)
        print ("-"*60)
        f.close()
    elif choice == 4:
        print ("Counting Number of Words ")
        f = open(a,"r")
        c = f.read()
        print (c)
        print ("-"*60)
        print ("Spliting  ==> ", c.split())
        print ("Total Length ==> ", len(c.split()))
        print ("-"*60)
        f.close()
    elif choice == 5:
        print ("Find the word/space in a file: ")
        f = open(a,"r")
        c = f.read()
        print (c)
        n = input("Enter the word to be find in the file: ")
        print ("-"*60)
        w = c.find(n)
        print ("Word is find at index:   ==> ", w)
        print ("-"*60)
        f.close()
    elif choice == 6:
        print ("Replace the String ")
        f = open(a,"r")
        c = f.read()
        print (c)
        r = input("Enter which word to be replaced in the file: ")
        p = input("Enter the word to be replaced in the file: ")
        print ("-"*60)
        w = c.replace(r,p)
        print ("Replaced String   ==> ", w)
        print ("-"*60)
        f.close()
    elif choice == 7:
        print ("Converting to Upper case and storing to another File ")
        f = open(a,"r")
        c = f.read()
        n = input("Enter the New file Name to be created: ")
        g = open(n,"w")
        g.write(c.upper())
        g.close()
        f.close()
        g = open(n,"r")
        print ("-"*60)
        print("New File Contents ", g.read())
        print ("-"*60)
        g.close()
        print ("-"*60)
    else:
        print ("Invalid Choice")
