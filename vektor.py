import numpy as np
import matplotlib.pyplot as plt
import math
    
    
def main():
    print("1. persamaan vektor")
    print("2. rumus penjumlahan")
    print("3. perkalian")
    
    choice= int(input("masukan nomor pilihan anda: "))
    
    if choice == 1:
        persamaan()
    elif choice == 2:
        penjumlahan()
    elif choice == 3:

        perkalian()
    else:
        print("invalid")



def persamaan():
        a = float(input("masukan besar sumbu x: "))
        b = float(input("masukan besar sumbu y: "))
        V = np.array([[a, b]])
        origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
        print(f"persamaan = {a}x + {b}y")
        plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
        plt.show()

def perkalian():
    print("1. perkalian cross ab")
    print("2. perkalian cross ijk")
    print("3. perkalian dot ab")
    print("4. perkalian dot ijk")
    
    option = int(input("masukan nomor menu: "))
    if option== 1:
        a= float(input("masukan vektor A: "))
        b= float(input("masukan vektor B: "))
        c= float(input("masukan sin: "))
        rad= math.radians(c)
        ab= a*b*math.sin(rad)
        print(ab)
    elif option== 2:
        a= float(input("masukan nilai i A"))
        b= float(input("masukan nilai i B"))
        c= float(input("masukan nilai j A"))
        d= float(input("masukan nilai j B"))
        e= float(input("masukan nilai k A"))
        f= float(input("masukan nilai k B"))
        
        i= c*f-e*d
        j= e*b-a*f
        k= a*d-c*b
        
        axb= math.sqrt(i**2+j**2+k**2)
        print(axb)
    elif option== 3:
        a= float(input("masukan vektor A: "))
        b= float(input("masukan vektor B: "))
        c= float(input("masukan cos: "))
        rad= math.radians(c)
        ab= a*b*math.cos(rad)
        print(ab)
    elif option== 4:
        a= float(input("masukan nilai i A"))
        b= float(input("masukan nilai i B"))
        c= float(input("masukan nilai j A"))
        d= float(input("masukan nilai j B"))
        e= float(input("masukan nilai k A"))
        f= float(input("masukan nilai k B"))
             
        hasil= (a*b)+(c*d)+(e*f)
        
        print(hasil)
def penjumlahan():
    print("1. penjumlahan segaris")
    print("2. penjumlahan kosinus")
    print("3. penjumlahan sqrt(Fx**2+Fy**2)")
    print("4. penjumlahan besar sumbu x dan y")
    
    option = int(input("masukan nomor pilihan anda: "))
    if option == 1:
        a= float(input("masukan vektor pertama: "))
        b= float(input("masukan vektor kedua: "))
        c= a+b
        V = np.array([[a, b]])
        origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
        plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
        plt.show()
        print(c)
    elif option == 2:
        print("bagian kosinus")
        a= float(input("masukan vektor 1(x): "))
        b= float(input("masukan vektor 2(y): "))
        c= float(input("masukan sudut: "))
        
        V = np.array([[a, b]])
        origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin 
        plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
        plt.show()
        d= math.sqrt((a**2)+(b**2)+(2*a*b*math.cos(c)))
        
        print(f"besar vektor nya secara kosinus: ", d)
    elif option == 3:
        print("bagian vektor 3d")
        a= float(input("masukan vektor 1(x): "))
        b= float(input("masukan vektor 2(x): "))
        c= float(input("masukan vektor 1(y): "))
        d= float(input("masukan vektor 2(y): "))
        
        
        x= a+b
        y= c+d
        e= math.sqrt((x**2)+(y**2))
        rad= y/x
        ar= math.atan(rad)
        degre= np.degrees(ar)
        V = np.array([[x, y]])
        origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
        print(f"persamaan = {a}x + {b}y")
        plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
        plt.show()
        print(f"besar vektor nya secara 3 d penjumlahan : ", e)
        print(f"besar sudut vektor", degre)
    elif option == 4:
        print("1. mencari x vektor")
        print("2. mencari y vektor")
        choice= int(input("masukan nomor menu: "))
        
        if choice == 1:
            a= float(input("masukan besar vektor: "))
            b= int(input("masukan sudut: "))
            rad= math.radians(b)
            fx= a*(math.cos(rad))
            print(fx)
            V = np.array([[fx, 0]])
            origin = np.array([[0, 0, 0,0,0,0,0,0,0,0,0],[0, 0, 0]]) # origin point
            print(f"persamaan = {a}x + {b}y")
            plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=40)
            plt.show()
            
        elif choice == 2:
            a= float(input("masukan besar vektor: "))
            b= int(input("masukan sudut: "))
            rad= math.radians(b)
            fy= a*math.sin(rad)
            
            print(fy)
            V = np.array([[0, fy]])
            origin = np.array([[0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) # origin point
            print(f"persamaan = {a}x + {b}y")
            plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=40)
            plt.show()
        else:
            print("invalid")
            
            
if __name__ == "__main__":
    main()