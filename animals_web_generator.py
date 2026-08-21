import json

TO_REPLACE = "__REPLACE_ANIMALS_INFO__"

def load_data(file_path):
    """Load json file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def generate_animals_card_item(animal):
    """
    Extract animal info from dictionary and return an HTML card item
    :param animal:
    :return: str
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal['name']}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul>\n'
    output +=f"      <li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
    output +=f"      <li><strong>Location:</strong> {animal['locations']}</li>\n"
    animal_type = animal['characteristics'].get('type', "Unknown")
    if animal_type != "Unknown":
        output +=f"      <li><strong>Type:</strong> {animal_type}</li>\n"
    output += f'    </ul>\n'
    output += f"</li>\n"
    return output


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def generate_html_code():
    """Generate animal cards HTML"""
    animals_data = load_data('data/animals_data.json')

    animal_cards = ""
    for animal in animals_data:
        animal_cards += generate_animals_card_item(animal)

    return animal_cards


def main():
    animal_cards = generate_html_code()
    html_template = read_from_file('animals_template.html')

    html_content = html_template.replace(TO_REPLACE, animal_cards)
    write_to_file('animals.html', html_content)

    print(html_content)


if __name__ == "__main__":
    main()