from xml_file_processor import FileProcessor

def main_menu():
    print("\nXML File Processor")
    print("1. Display Records")
    print("2. Add Record")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def get_person_data():
    name = input("Enter name: ")
    age = input("Enter age: ")
    street = input("Enter street: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    return {
        'name': name,
        'age': age,
        'address': {
            'street': street,
            'city': city,
            'state': state,
            'zip': zip_code
        }
    }

def main():
    processor = FileProcessor()
    filename = "test.xml"

    while True:
        choice = main_menu()

        if choice == '1':
            processor.display_records(filename)
        elif choice == '2':
            person_data = get_person_data()
            processor.add_record(filename, person_data)
        elif choice == '3':
            name = input("Enter the name of the person to update: ")
            new_data = get_person_data()
            processor.update_record(filename, name, new_data)
        elif choice == '4':
            name = input("Enter the name of the person to delete: ")
            processor.delete_record(filename, name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
