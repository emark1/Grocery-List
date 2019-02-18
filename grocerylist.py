#Grocery List, with Classes and Objects


def show_menu():
    print("""Press 1 to create a new shopping list.
Press 2 to edit an existing list.
Press 3 to select a list to display.
Press Q to quit.""")

def edit_menu():
    print("")

list_array = []

class List:
    def __init__(self,store):
        self.store = store
        self.groceryitems = []
    
class GroceryItem():
    def __init__(self,item,price,quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

#groceryitem1 = GroceryItem('Apples',10.00,15)

def create_list():
    list_name = input("Enter name of new list or store: ")
    name = List(list_name)
    list_array.append(name)

def edit_list():
    display_list()  
    select_list = ""
    select_list = input("Select list to edit: ")
    item_input = input("Enter item to add to the list: ")
    .groceryitems.append(item_input)

def display_list():
    #list_selection = input("Enter number of the list you wish to view: ")
    # for store1 in range(0,len(list_array)):
    #     task = list_array[store1]
    #     print(f"""{store1 + 1} x {store1.store}""")

    for store in list_array:
        print(f'{list_array.index(store) + 1} - {store.store}')

##############




user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice here: ")
    if user_input == "1":
        create_list()
    elif user_input == "2":
        edit_list()
    elif user_input == "3":
        display_list()
