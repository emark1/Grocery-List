#Grocery List, with Classes and Objects


def show_menu():
    print("""Press 1 to create a new shopping list.
Press 2 to edit an existing list.
Press 3 to select a list to display.
Press Q to quit.""")

list_array = []

class List:
    def __init__(self,store):
        self.store = store
        self.items_array = []

    
class GroceryItem():
    def __init__(self,item,price,quantity):
        self.item = item
        self.price = price
        self.quantity = quantity


def create_list():
    list_name = input("Enter name of new list or store: ")
    name = List(list_name)
    list_array.append(name)


def edit_list():
    try:
        display_list()  
        select_list = int(input("Select list to edit: "))
        item_input = input("Enter item name to add to the list: ")
        price_input = float(input("Enter the price of the item: "))
        quantity_input = int(input("Enter the quantity of the item: "))
        new_item = GroceryItem(item_input,price_input,quantity_input)
        list_array[select_list-1].items_array.append(new_item)
    except IndexError:
        print("This selection was not in the list.")

def display_list():
    #list_selection = input("Enter number of the list you wish to view: ")
    # for store1 in range(0,len(list_array)):
    #     task = list_array[store1]
    #     print(f"""{store1 + 1} x {store1.store}""")

    for store in list_array:
        print(f'{list_array.index(store) + 1} - {store.store}')


def display_full():
    for index in range(0,len(list_array)):
        lists = list_array[index]
        print(f'{index + 1} - {lists.store}')
        sum = 0 
        for item in lists.items_array:
            print(f"{item.item} - ${item.price} - Quantity:{item.quantity}")
            sum += (item.price * item.quantity)
        print(f'Total price: ${sum}')
    return sum


user_input = ""
try:
    while user_input != "q":
        show_menu()
        user_input = input("Enter your choice here: ")
        if user_input == "1":
            create_list()
        elif user_input == "2":
            try:
                edit_list()
            except IndexError:
                print("Not a valid list")
        elif user_input == "3":
            display_full()
except (ValueError):
    print("Error: Enter a number for selection, or Q to quit.")
