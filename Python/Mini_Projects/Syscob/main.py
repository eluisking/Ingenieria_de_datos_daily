"""
Este mini proyecto trata de una app de cobro de una taqueria,
con el cual podemos cobrar una orden y agregar/eliminar productos al menu
para cobrar en las ordenes.
"""

from itertools import product


menu = {"Quesabirria": 30, "Bistek": 25, "Arrachera": 30, "Coca Cola": 30, "Agua": 20}

xtra_cheese = 5


def add_item():
    print("Producto: ")
    name = input()
    print("price: ")
    price = int(input())
    menu.update({name: price})
    print("Menu actualizado con exito!!")
    print(menu)


def total_order():
    while_it = True
    list_items = {}
    while while_it == True:
        item = input("Que item deseas suma: ")
        count = int(input("Cantidad: "))
        if item == " ":
            break


def menu_app(option):
    if option == 1:
        print("Cobraremos una cuenta:")
        total_order()
    elif option == 2:
        add_item()


print("*** BIENVENIDO *** \n")
print("1- Cobrar cuenta. \n2- Agregar producto.\n")
print("Que operacion deseas realizar: ")
option_us = int(input())
menu_app(option_us)
