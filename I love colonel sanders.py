import time
input("Welcome to: I love you Colonel Sanders!")
input("The finger licking good dating sim!")
input("Soon you will meet our handsome friend")
print("But first, what is your name?")
name = input(">")
input("...")
time.sleep(0.8)
print(name, "?")
time.sleep(0.8)
print(name.upper(), "???")
time.sleep(0.8)
input("No no no that just wont do!")
input("From now on, you will be called Joe")
input("Yes, Joe - a wonderful name")
input("So, Joe Swanson, do you think that you are ready to meet Colonel Sanders?")
input("Because I fucking don't - look at you, you are a mess, you can't meet him like this")
print("At least make some effort to prepare - you could do your (h)air, put on some (c)lothes")
check = False
while check == False:
    choice1 = input(">").lower()
    if choice1 == ("h") or choice1 == ("c"):
        check = True
    else:
        print("Please enter h or c to choose an option")
if choice1 == ("h"):
    prep = 0
    input("You wash, blow dry and comb your head. You then put your hair on.")
elif choice1 == ("c"):
    prep = 1
    input("You put on your limited edition gucci off white yeezy 350s in diamond blue. You have no other clothes.")
