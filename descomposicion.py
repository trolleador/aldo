x="si"

while( x == "si"):
    y = (int(input("numero a descomponer\n")))
    i = 2
    

    while(y>1):
        if y%i==0:
            print(i)
            y=y/i
            i = i-1
        i= i+1

    x=input("quieres descomponer otro numero?\n")