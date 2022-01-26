print("start")
def bimplouf(x,y):
    if x==4 and y==4 :
        print("hit")
    elif x==4 and y != 4 or x!=4 and y==4 :
        print("en vue !")
        else :
            print("a l'eau")
x=int(input("ligne"))
y=int(input("colonne"))
bimplouf(x,y)
