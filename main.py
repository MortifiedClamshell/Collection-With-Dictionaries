# Initialize the collection dictionary with at least ten items
collection = {
    "To Kill a Mockingbird": {"author": "Harper Lee", "year_published": 1960, "genre": "Fiction / Classic"},
    "1984": {"author": "George Orwell", "year_published": 1949, "genre": "Dystopian / Science Fiction"},
    "Pride and Prejudice": {"author": "Jane Austen", "year_published": 1813, "genre": "Romance / Classic"},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year_published": 1925, "genre": "Fiction / Classic"},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "year_published": 1951, "genre": "Fiction / Coming-of-Age"},
    "The Hobbit": {"author": "J.R.R. Tolkien", "year_published": 1937, "genre": "Fantasy / Adventure"},
    "Fahrenheit 451": {"author": "Ray Bradbury", "year_published": 1953, "genre": "Dystopian / Science Fiction"},
    "The Book Thief": {"author": "Markus Zusak", "year_published": 2005, "genre": "Historical Fiction"},
    "The Road": {"author": "Cormac McCarthy", "year_published": 2006, "genre": "Post-Apocalyptic / Fiction"},
    "The Hunger Games": {"author": "Suzanne Collins", "year_published": 2008, "genre": "Dystopian / Young Adult"},
}

def add_item(collection):
    # Prompt the user to enter details for a new book
    book_title = input("Enter the book title: ")
    author = input("Enter the author: ")
    # Validate the year published input
    while True:
        try:
            year_published = int(input("Enter the year published: "))
            break
        except ValueError:
            print("Not valid input, try again.")
    genre = input("Enter the genre: ")
    # Add the new book to the collection
    collection[book_title] = {"author": author, "year_published": year_published, "genre": genre}
    print(f"Book '{book_title}' added successfully.")

def update_item(collection):
    # Prompt the user to enter the title of the book to update
    book_title = input("Enter the book title to update: ")
    if book_title in collection:
        # Prompt the user to enter new details for the book
        author = input("Enter the new author: ")
        # Validate the year published input
        while True:
            try:
                year_published = int(input("Enter the new year published: "))
                break
            except ValueError:
                print("Not valid input, try again.")
        genre = input("Enter the new genre: ")
        # Update the book details in the collection
        collection[book_title] = {"author": author, "year_published": year_published, "genre": genre}
        print(f"Book '{book_title}' updated successfully.")
    else:
        print(f"Book '{book_title}' not found.")

def remove_item(collection):
    # Prompt the user to enter the title of the book to remove
    book_title = input("Enter the book title to remove: ")
    if book_title in collection:
        # Remove the book from the collection
        del collection[book_title]
        print(f"Book '{book_title}' removed successfully.")
    else:
        print(f"Book '{book_title}' not found.")

def display_items(collection):
    # Display all books in the collection in a readable format
    for book_title, properties in collection.items():
        print(f"Title: {book_title}")
        for key, value in properties.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")
        print()

def main():
    # Main loop to display the menu and handle user choices
    while True:
        print("Menu:")
        print("1. Add book")
        print("2. Update book")
        print("3. Remove book")
        print("4. Display books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(collection)
        elif choice == "2":
            update_item(collection)
        elif choice == "3":
            remove_item(collection)
        elif choice == "4":
            display_items(collection)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
