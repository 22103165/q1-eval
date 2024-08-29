class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        if item not in self.items:
            self.items.append(item)
            print(f"Item '{item}' added to the list.")
        else:
            print(f"Item '{item}' is already in the list.")

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from the list.")
        else:
            print(f"Item '{item}' not found in the list.")

    def search_item(self, item: str) -> bool:
        return item in self.items

    def display_list(self):
        if not self.items:
            print("The shopping list is currently empty.")
        else:
            print("Current shopping list:")
            for item in self.items:
                print(f"- {item}")


if __name__ == "__main__":
    shopping_list = ShoppingList()

    
    shopping_list.add_item("Milk")
    shopping_list.add_item("Eggs")
    shopping_list.add_item("Bread")

    
    shopping_list.display_list()

    
    item_to_search = "Eggs"
    if shopping_list.search_item(item_to_search):
        print(f"Item '{item_to_search}' is on the list.")
    else:
        print(f"Item '{item_to_search}' is not on the list.")
    shopping_list.remove_item("Bread")
    shopping_list.remove_item("Butter") 
    shopping_list.display_list()
