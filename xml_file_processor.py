import xml.etree.ElementTree as ET

class FileProcessor:
    def read_file(self, filename):
        tree = ET.parse(filename)
        return tree.getroot()

    def add_record(self, filename, person_data):
        tree = ET.parse(filename)
        root = tree.getroot()

        person = ET.SubElement(root, 'person')
        ET.SubElement(person, 'name').text = person_data.get('name', '')
        ET.SubElement(person, 'age').text = str(person_data.get('age', ''))
        address = ET.SubElement(person, 'address')
        ET.SubElement(address, 'street').text = person_data.get('address', {}).get('street', '')
        ET.SubElement(address, 'city').text = person_data.get('address', {}).get('city', '')
        ET.SubElement(address, 'state').text = person_data.get('address', {}).get('state', '')
        ET.SubElement(address, 'zip').text = person_data.get('address', {}).get('zip', '')

        tree.write(filename)

    def delete_record(self, filename, name):
        tree = ET.parse(filename)
        root = tree.getroot()
        for person in root.findall("./person[name='{}']".format(name)):
            root.remove(person)
        tree.write(filename)

    def update_record(self, filename, name, new_data):
        self.delete_record(filename, name)
        self.add_record(filename, new_data)

    def display_records(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for person in root:
            print("Person:")
            for element in person:
                if element.tag != 'address':
                    print(f"  {element.tag.title()}: {element.text}")
                else:
                    print("  Address:")
                    for addr_elem in element:
                        print(f"    {addr_elem.tag.title()}: {addr_elem.text}")
