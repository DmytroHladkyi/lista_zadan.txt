user1 = -1 # wartość inna od wartości ewentualnego wyboru użytkownika. 

lista = []


def liczba():
    list_index = 0
    for list in lista:
        print(list + " [ " + str(list_index) + " ] ")
        list_index += 1

def add_lista():
    list = input("Dodaj zadanie: ") # co wpiszemy do "list" jako zadanie, potem powinniśmy wpisac do ("list" do "lista = []" to co potem będzie zapisywane do lista.append() )
    lista.append(list)
    print("Zadanie zostało dodane.")

def delete_lista():
    list_index = int(input("Podaj index zadania, którego chcesz usunąć."))
    if list_index < 0 or list_index > len(lista) - 1: # dodajemy (-1) poniważ lista zaczyna się do 0
        print("Zadanie z takim numerem nie istnieje.")
        return
    lista.pop(list_index) #funkcja do usuwania nazywa się - pop
    print("Zadanie zostało usunięte")

def save_file():
    file = open("lista_zadan.txt", "w+") # "w" oznacza zapisywanie a "w+" oznacza zapisywanie o odczytywanie
    for task in lista:
        file.write(task + "\n") # \n oznacza koniec linii
    file.close()
    print("Lista została zapisana")

def load_to_file():
    try:
        file = open("lista_zadan.txt")
        for line in file.readlines(): # pętla do każdego zadania, które znajduje się na osobnej linii 
            lista.append(line.strip()) # używamy strip ponieważ pod czas zapisywania zadanie w pliku dodaliśmy "\n  "
        file.close()
    except FileNotFoundError: # dodajemy funkcje  except FileNotFoundError jeżeli plik nasz lista_zadan.txt jeszcze nie istnieje. 
        return

def numer_zadania():
     if user1 <= 0 or user1 >= 6:
        print("Zadanie z takim numerem nie istnieje. Wybierz w przedziale od 1 do 5")
     return

load_to_file()

while user1 != 5: # dopóki wybór użytkowmnika różni się od 5 - wykonujemy pętle "while"
    if user1 == 1:
       liczba()

    if user1 == 2:
       add_lista()
    
    if user1 == 3:
       delete_lista()

    if user1 == 4:
        save_file()
    
    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdż")

    user1 = int(input("Wybierz liczbę: "))
    numer_zadania()  