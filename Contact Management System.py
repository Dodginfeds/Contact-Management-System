# ---------------------------------------------
# Contact Management System
# ---------------------------------------------
# This program allows users to:
# 1. Add a new contact with Name, Phone, Email, and Address.
# 2. View all saved contacts.
# 3. Search for a contact by name.
# 4. Delete a contact by ID.
# 5. Update contact information.
# 6. Quit the program.
# ---------------------------------------------

import os  

# File to store contacts
CONTACT_BOOK = "Contact_book.txt"

# Ensure the contact file exists
if not os.path.exists(CONTACT_BOOK):
    with open(CONTACT_BOOK, 'w') as file:
        file.write("ID | Name | Phone | Email | Address\n")
        print("New contact book file created!")

# ---------------------------------------------
# Function to Get Next Contact ID
# ---------------------------------------------

def get_next_id():
    """
    Returns the next available contact ID.
    """
    with open(CONTACT_BOOK, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            return 1
        last_contact = lines[-1].strip().split(" | ")
        return int(last_contact[0]) + 1

# ---------------------------------------------
# Function to Add a New Contact
# ---------------------------------------------

def add_contact():
    """
    Adds a new contact with Name, Phone, Email, and Address.
    """
    try:
        with open(CONTACT_BOOK, 'a') as file:
            name = input("Enter the contact's name: ").strip()
            if not name.isalpha():
                raise ValueError("Name must contain only letters.")

            phone = input("Enter phone number (e.g., 1234567890): ").strip()
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number! Must be 10 digits.")

            email = input("Enter email address: ").strip()
            if "@" not in email or "." not in email:
                raise ValueError("Invalid email format!")

            address = input("Enter address: ").strip()
            contact_id = get_next_id()

            formatted_phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
            file.write(f"{contact_id} | {name} | {formatted_phone} | {email} | {address}\n")

            print(f"Contact '{name}' has been added successfully!")

    except ValueError as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to View All Contacts
# ---------------------------------------------

def view_contacts():
    """
    Displays all stored contacts.
    """
    try:
        with open(CONTACT_BOOK, 'r') as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("\nNo contacts found! Start by adding one.")
            return

        print("\n--- Contact List ---")
        print(f"{'ID':<5} {'Name':<15} {'Phone':<15} {'Email':<30} {'Address'}")
        print("-" * 80)

        for line in lines[1:]:
            parts = line.strip().split(" | ")
            if len(parts) != 5:
                continue

            contact_id, name, phone, email, address = parts
            print(f"{contact_id:<5} {name:<15} {phone:<15} {email:<30} {address}")

        print("-" * 80)

    except FileNotFoundError:
        print("Contact file not found.")
    except Exception as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to Search for a Contact
# ---------------------------------------------

def search_contact():
    """
    Searches for a contact by name.
    """
    try:
        search_name = input("Enter the name to search: ").strip().lower()

        with open(CONTACT_BOOK, 'r') as file:
            lines = file.readlines()

        found = False
        for line in lines[1:]:
            parts = line.strip().split(" | ")
            if len(parts) != 5:
                continue

            contact_name = parts[1].strip().lower()
            if search_name == contact_name:
                print("\nContact Found:")
                print("-" * 40)
                print(line.strip())
                print("-" * 40)
                found = True
                break

        if not found:
            print(f"No contact found with the name '{search_name}'.")

    except Exception as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to Delete a Contact
# ---------------------------------------------

def delete_contact():
    """
    Deletes a contact by its ID.
    """
    try:
        contact_id = int(input("Enter the ID of the contact to delete: ").strip())

        with open(CONTACT_BOOK, "r") as file:
            lines = file.readlines()

        found = False
        updated_lines = [lines[0]]  # Keep header

        for line in lines[1:]:
            parts = line.strip().split(" | ")
            if len(parts) != 5:
                continue

            if int(parts[0]) == contact_id:
                print(f"\nContact '{line.strip()}' deleted successfully!")
                found = True
                continue  # Skip this line to delete

            updated_lines.append(line)

        if not found:
            print(f"No contact with ID {contact_id} found.")
        else:
            with open(CONTACT_BOOK, 'w') as file:
                file.writelines(updated_lines)

    except ValueError:
        print("Invalid input! Please enter a valid numeric ID.")

# ---------------------------------------------
# Function to Update a Contact
# ---------------------------------------------

def update_contact():
    """
    Updates a contact’s details by its ID.
    """
    try:
        contact_id = int(input("Enter the contact ID to update: ").strip())

        with open(CONTACT_BOOK, 'r') as file:
            lines = file.readlines()

        found = False
        updated_lines = [lines[0]]

        for line in lines[1:]:
            parts = line.strip().split(" | ")
            if len(parts) != 5:
                continue

            if int(parts[0]) == contact_id:
                print(f"\nCurrent Contact: {line.strip()}")
                found = True

                print("What would you like to update?")
                print("1. Name\n2. Phone\n3. Email\n4. Address")
                choice = input("Enter your choice (1-4): ").strip()

                if choice == "1":
                    new_name = input("Enter new name: ").strip()
                    parts[1] = new_name
                elif choice == "2":
                    new_phone = input("Enter new phone number (1234567890): ").strip()
                    if not new_phone.isdigit() or len(new_phone) != 10:
                        print("Invalid phone number.")
                        continue
                    parts[2] = f"{new_phone[:3]}-{new_phone[3:6]}-{new_phone[6:]}"
                elif choice == "3":
                    new_email = input("Enter new email: ").strip()
                    if "@" not in new_email or "." not in new_email:
                        print("Invalid email format.")
                        continue
                    parts[3] = new_email
                elif choice == "4":
                    new_address = input("Enter new address: ").strip()
                    parts[4] = new_address
                else:
                    print("Invalid choice.")

                updated_lines.append(" | ".join(parts) + '\n')
            else:
                updated_lines.append(line)

        if not found:
            print(f"No contact with ID {contact_id} found.")
        else:
            with open(CONTACT_BOOK, 'w') as file:
                file.writelines(updated_lines)
            print("Contact updated successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid numeric ID.")

# ---------------------------------------------
# Function to Display Menu
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing contacts.
    """
    while True:
        print("\n--- Contact Manager Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Quit")

        try:
            choice = int(input("Enter your choice (1-6): ").strip())

            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                update_contact()
            elif choice == 6:
                print("Thank you for using the Contact Manager! Goodbye! 👋")
                break
            else:
                print("Invalid option! Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Contact Manager App!")
    menu()
