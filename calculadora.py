#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print(2**1/12)


# In[1]:



def sumar():
    x = a + b
    print (("Resultado"), (x))
def restar():
    x = a - b
    print (("Resultado"), (x))
def multiplicar():
    x = a * b
    print (("Resultado"), (x))
def dividir():
    x = a / b
    print (("Resultado"), (x))

##########################################-2-###################################################
while True: #
    try:
        a = int(input("Ingresa el primer numero: \n")) #
        b = int(input("Ingresa el segundo numero: \n"))#
        print (("Que cálculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #
        op = str(input(""" #Ofrecemos las opciones de cálculo que van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    except:
        print ("Error")
        op = '?'
##########################################-3-##################################################
    if op == '1':
        sumar()
        break
    elif op == '2':
        restar()
        break
    elif op == '3':
        multiplicar()
        break
    elif op == '4':
        dividir()
        break
    else:
        print ("""Has ingresado un numero de opcion erroneo""") 


# In[ ]:




