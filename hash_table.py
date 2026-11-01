
# Contact Management System Using a Hash Table


# Step 1: Create the Contact class
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


# Step 2: Create the Node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Step 3: Create the HashTable class
class HashTable:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Hash table size must be positive.")

        self.size = size
        self.data = [None] * size

    # Convert a contact name into an array index
    def hash_function(self, key):
        total = 0

        for char in key:
            total += ord(char)

        return total % self.size

    # Insert a new contact or update an existing one
    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.data[index]

        # Search the linked list for an existing contact
        while current is not None:
            if current.key == key:
                current.value.number = value
                print(f"Updated contact: {key}")
                return

            current = current.next

        # Create a new contact and node
        new_contact = Contact(key, value)
        new_node = Node(key, new_contact)

        # Insert at the beginning of the linked list
        new_node.next = self.data[index]
        self.data[index] = new_node

        print(f"Added contact: {key}")

    # Search for a contact by name
    def search(self, key):
        index = self.hash_function(key)

        current = self.data[index]

        # Traverse the linked list
        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    # Print the entire hash table
    def print_table(self):
        print("\nContact Hash Table:")

        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
            else:
                contacts = []

                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {index}: - " + " - ".join(contacts))


# Step 4: Test the program
def main():

    # Create a hash table with 10 slots
    table = HashTable(10)

    print("\n--- Empty Hash Table ---")
    table.print_table()

    # Add contacts
    print("\n--- Adding Contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    table.print_table()

    # Search for a contact
    print("\n--- Searching for John ---")
    contact = table.search("John")
    print("Search result:", contact)

    # Test hash collisions
    print("\n--- Testing Collisions ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    table.print_table()

    # Test duplicate contacts
    print("\n--- Testing Duplicate Contacts ---")
    table.insert("Rebecca", "999-444-9999")

    table.print_table()

    # Search for a missing contact
    print("\n--- Searching for Missing Contact ---")
    print("Search result:", table.search("Chris"))


# Run the program
if __name__ == "__main__":
    main()
