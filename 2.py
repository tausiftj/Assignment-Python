#Write a Function to return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.

def fun(a):
    Flag=False;
    for i in a[1].lower():
        if i in a[0].lower():
            Flag= True;
        else:
            Flag=False;
            break;
    print(Flag);
a=["fsia", "ASiF"]
fun(a)

     
