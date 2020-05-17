import time
mystack = []
while True:
    print("Enter a word")
    h = input(">")
    if  h == "print":
        for item in mystack:
            print("You are not funny if you have ever in your life once typed in ", str(item))
    elif h == "doctor who":
        with open("when.txt", 'r') as f:
            lines = f.readlines()

        for line in lines:
            print (line)
            time.sleep(0.1)
    else:
        mystack.append(h)
