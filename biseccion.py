from math import *
#Instrucciones:
#Simplemente deben darle run al programa.
print("Ingrese una función")
fx=input("Por ejemplo: 'tan(x) + x**2 - x'. Solo ingrese la expresion, no las comillas ")
fun = lambda x: eval(fx)
while(1):
    n = input("ingrese el numero maximo de iteraciones que desea ")
    try:
        n=int(n)
    except:
        print(" ¡ error ! --- Ingrese un numero entero --- ")
        continue
    print("Ingrese el intervalo de la forma [a,b]")
    a=input("ingrese el valor de a ")
    b=input("ingrese el valor de b ")
    try:
        a, b = float(a), float(b)
    except:
        print(" ¡ error ! --- Ingrese solo numeros --- ")
        continue
    if a>b:
        print(" ¡ error ! --- Asegurese de que a < b --- ")
        continue
    iteracion, an, bn = 0, a, b

    """
    Ahora viene lo interesante, el comando while realiza lo que esta dentro de su bloque hasta que el valor de "iteracion" supere a "n"
    fa será el valor de la funcion evaluada en "an" y lo mismo para fb,
    chequeo si fa*fb<=0 en cuyo caso voy buscando de a mitades la raiz
    """
    while((iteracion < n)):
        fa, fb = fun(an), fun(bn)
        if fa*fb>0:
            print("No es posible aplicar el metodo de la bisección ya que f(a)*f(b)>0")
            break
        else: #en este caso ocurre que f(a)*f(b)<0
            cn=(an+bn)/2.0
            fc=fun(cn)
            if fc*fa<0:
                bn=cn
            else:
                an=cn
        iteracion+=1
    print("Resultado: ")
    print(" La iteracion termino en n= "+str(iteracion))
    print(" La raiz aproximada de la funcion "+ str(fx)+" es x= "+str(cn)+ " en el intervalo ["+str(a)+","+str(b)+"]")
    break