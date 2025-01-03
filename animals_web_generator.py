import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serializes a single animal object to HTML format."""
    output = '<li class="cards__item">\n'
    if "name" in animal:
        output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += "<div class='card__text'>\n"
    output += "<div class='taxonomy-box'><h3>Taxonomy</h3><ul class='taxonomy-list'>\n"
    if "taxonomy" in animal:
        for key, value in animal["taxonomy"].items():
            output += f"<li class='taxonomy-item'><strong>{key.capitalize()}:</strong> {value}</li>\n"
    output += "</ul></div>\n"
    output += "<div class='characteristics-box'><h3>Characteristics</h3><ul class='characteristics-list'>\n"
    if "characteristics" in animal:
        for key, value in animal["characteristics"].items():
            output += f"<li class='characteristics-item'><strong>{key.replace('_', ' ').capitalize()}:</strong> {value}</li>\n"
    output += "</ul></div>\n"
    if "locations" in animal and animal["locations"]:
        output += f"<div class='locations-box'><h3>Locations</h3><ul class='locations-list'><li class='locations-item'>{', '.join(animal['locations'])}</li></ul></div>\n"
    output += "</div></li>\n"
    return output


def generate_animal_info(animals_data):
    """Generates a string with the animal information in HTML format."""
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    # Load the animals data
    animals_data = load_data('animals_data.json')

    # Generate the animal information string
    animals_info = generate_animal_info(animals_data)

    # Read the template content
    with open('animals_template.html', 'r') as file:
        template_content = file.read()

    # Replace the placeholder with the animal information
    html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as file:
        file.write(html_content)

    print("HTML file generated successfully.")


if __name__ == "__main__":
    main()
