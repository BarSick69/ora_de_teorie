def make_pos(x):
    a=str(x)
    initial=x
    if(a[0]=="-"):
        x-=initial*2
        return x
    else:
        return x


def n_de_cifre(a):
    a=str(a)
    if(a[0]=="-"):
        return len(a)-1
    else:
        return len(a)
def n_de_cifre_p(a):
    i=0
    while(a!=0):
        cifra = a%10
        a=a//10
        if cifra%2==0 and cifra!=0:
            i+=1
    return i
def n_de_cifre_im(a):
    i=0
    while(a!=0):
        cifra = a%10
        a=a//10
        if cifra%2!=0 and cifra!=0:
            i+=1
    return i
def suma_cif(a):
    suma=0
    while(a!=0):
        cif=a%10
        a=a//10
        suma+=cif
    return suma
def cifra_max(a):
    max=0
    while(a!=0):
        cifra = a%10
        a=a//10
        if(cifra>max):
            max=cifra
    return max
def cifra_min(a):
    min=a%10
    while(a!=0):
        cifra = a%10
        a=a//10
        if(cifra<min):
            min=cifra
    return min
def media(a):
    suma = suma_cif(a)
    media_aritm = suma/n_de_cifre(a)
    return media_aritm
def repeating(a):
    a=str(a)
    repeat_list=[]
    repeating_numbers=[]
    for num in a:
        if repeat_list.count(num)<1:
            repeat_list.append(num)
        else:
            repeating_numbers.append(num)
    if(len(repeating_numbers)>0):
        repeating_numbers = set(repeating_numbers)
        return repeating_numbers
    return "nici un numar"
    
def show_cif(a):
    num = []
    while(a!=0):
        cifra = a%10
        a=a//10
        num.append(cifra)
    num = reversed(num)
    for i in num:
        print(i,end=" ")

def reverse_num(a):
    a=str(a)
    reversedn=""
    for i in range(len(a),0,-1):
        reversedn+=a[i-1]
    return reversedn

def cel_m_m(a):
    lista=[]
    a=str(a)
    for c in a:
        lista.append(int(c))
    lista=sorted(lista)
    lista=reversed(lista)
    nr=""
    for i in lista:
        nr+=str(i)
    return nr
def prim(a):
    divisors=0
    for i in range(1,a+1):
        if a%i==0:
            divisors+=1
        i+=1
    if(divisors<=2):
        return "Prim"
    else:
        return ""

n = int(input("Introduceti un numar intreg: "))
n=make_pos(n)
print("Numarul de cifre:",n_de_cifre(n))
print("Numarul de cifre pare:",n_de_cifre_p(n))
print("Numarul de cifre impare:",n_de_cifre_im(n))
print("Suma numerelor:",suma_cif(n))
print("Cifra maxima este:",cifra_max(n))
print("Cifra minima este:",cifra_min(n))
print("Media aritmetica este:",media(n))
print("Se repet numerele:",repeating(n))
print("Numerele:",end=" ")
show_cif(n)
print("\nNumarul inversat:",reverse_num(n))
print("Cel mai mare numar format: ",cel_m_m(n))
print(prim(n))



