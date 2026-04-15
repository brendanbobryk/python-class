# Book class definition
class Book:
    def __init__(self, title="", author="", pages=0, is_read=False):
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Read: {self.is_read}\n")

    # Method to mark the book as read
    def mark_as_read(self):
        self.is_read = True
        print(f"'{self.title}' has been marked as read.")

    # Method to check if book is long
    def is_long_book(self):
        return self.pages > 300

    # Method to check pages remaining (assumes not started if unread) (Bonus point)
    def pages_remaining(self):
        if self.is_read:
            return 0
        return self.pages

# Create multiple Book objects
book1 = Book("Python Basics", "Jane Rogers", 250, False)
book2 = Book("C# Basics", "Daniel Brown", 320, False)
book3 = Book("C++ Basics", "Brendan Bobryk", 500, True)

# Display info for each book
print("Initial Book Information:")
print("-" * 40)
book1.display_info()
book2.display_info()
book3.display_info()

# Mark one book as read
print("Marking a 'Python Basics' as read")
print("-" * 40)
book1.mark_as_read()

# Display updated info
print("\nUpdated Book Information:")
print("-" * 40)
book1.display_info()

# Display if each book is long
print("Checking if books are long:")
print("-" * 40)
print(f"{book1.title} is long: {book1.is_long_book()}")
print(f"{book2.title} is long: {book2.is_long_book()}")
print(f"{book3.title} is long: {book3.is_long_book()}")

# Display pages remaining (Bonus point)
print("\nChecking pages remaining:")
print("-" * 40)
print(f"{book1.title} pages remaining: {book1.pages_remaining()}")
print(f"{book2.title} pages remaining: {book2.pages_remaining()}")
print(f"{book3.title} pages remaining: {book3.pages_remaining()}")