# Creating a shopping list project that allows users to add, remove, and view items in their shopping list.
shopping_list = []

# In the loop, we will display a menu of options for the user to choose from. The user can add an item, remove an item, view the shopping list, or exit the program.
shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        item = input("Enter the item to add: ").strip().title()
        shopping_list.append(item)
        print(f"'{item}' added to your shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ").strip().title()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your shopping list.")
        else:
            print(f"'{item}' is not in your shopping list.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    