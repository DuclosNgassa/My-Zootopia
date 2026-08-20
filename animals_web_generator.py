import json


def load_data(file_path):
    """Load json file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def generate_animals_data_string(animal):
    """
    Extract animal info from dictionary and return it as HTML string
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


def print_html_code():
    """Print HTML code"""
    animals_data = load_data('data/animals_data.json')

    final_output = ""
    for animal in animals_data:
        final_output += generate_animals_data_string(animal)

    print(final_output)


def main():
    print_html_code()

if __name__ == "__main__":
    main()