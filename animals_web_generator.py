import json


def load_data(file_path):
    """Load json file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def display_animal(animal):
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: {animal['locations']}")
    animal_type = animal['characteristics'].get('type', "Unknown")
    if animal_type != "Unknown":
        print(f"Type: {animal_type}")

animals_data = load_data('data/animals_data.json')


for animal in animals_data:
    display_animal(animal)
    print()
