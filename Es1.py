def menu():
    print("Menu.\nNew task\nRemove\nSorted\nClose")
    scelta=input()
    return int(scelta)
def insert(lista):
    print("Inserire il task: ",end='')
    task=input()
    lista.append(task)
    return lista
def rimuovi(lista):
    print("Cosa devo rimuovere? ",end='')
    task=input()
    if (task in lista):
        lista.remove(task)
    return lista

val=0
lista = []
while val!=4:
    val=menu()
    if val==1:
        lista=insert(lista)
    elif val==3:
        ordinata=sorted(lista)
        print(ordinata)
    elif val==2:
        lista = rimuovi(lista)

