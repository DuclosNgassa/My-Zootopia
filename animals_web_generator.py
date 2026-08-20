import json


def load_data(file_path):
    """Load json file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def display_animal(animal):
    """
    Display one animal
    :param animal:
    :return: None
    """
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: {animal['locations']}")
    animal_type = animal['characteristics'].get('type', "Unknown")
    if animal_type != "Unknown":
        print(f"Type: {animal_type}")
    print()


def generate_animals_data_string(animal):
    """
    Extract animal info from dictionary and return it as string
    :param animal:
    :return: str
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal['name']}</div>\n'
    output += '  <p class="card__text">\n'
    output +=f"    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output +=f"    <strong>Location:</strong> {animal['locations']}<br/>\n"
    animal_type = animal['characteristics'].get('type', "Unknown")
    if animal_type != "Unknown":
        output +=f"    <strong>Type:</strong> {animal_type}<br/>\n"

    output += f"  </p>\n"
    output += f"</li>\n"
    print(output)
    return output


def test():
    animals_data = load_data('data/animals_data.json')

    for animal in animals_data:
        #display_animal(animal)
        generate_animals_data_string(animal)

if __name__ == "__main__":
    test()
