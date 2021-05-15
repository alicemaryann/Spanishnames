# This program will convert your English name to Spanish
def main():
    print('Welcome to the Name Converter!')
    print('Your name will be converted into its Spanish equivalent!')
    keep_going = 'y'
    while keep_going.lower() == 'y':
        name = input('Please enter your first name: ')
        while name.isdigit() and name.isalnum():
            name = input('ERROR! Names can not contain any numbers! Please enter new name: ')
        keep_going = convert_name(name)


def convert_name(name):
    name_dictionary = {'George': 'Jorge', 'John': 'Juan', 'William': 'Guillermo', 'Edward': 'Eduardo',
                       'Charles': 'Carlos', 'Patrick': 'Patricio', 'Joseph': 'Jose', 'James': 'Jaime',
                       'Fredrick': 'Federico', 'Alfred': 'Alfredo', 'Ronald':'Ronaldo', 'Stephen': 'Esteban',
                       'Albert': 'Alberto', 'Julian': 'Juliano', 'Richard': 'Ricardo', 'Louis': 'Luis',
                       'Michael': 'Miguel', 'Leopold': 'Leopoldo', 'Henry': 'Enrique', 'Frank': 'Franco',
                       'Katherine': 'Catalina', 'Catherine': 'Catalina', 'Alice': 'Alicia', 'Anne': 'Ana',
                       'Juliet': 'Julieta', 'Mary': 'Maria', 'Marianne': 'Anna Maria', 'Charlotte': 'Carlotta',
                       'Susan': 'Susanna', 'Jane': 'Juana', 'Eleanor': 'Leonor', 'Alexander': 'Alejandro',
                       'Alexandra': 'Alejandra', 'Blanche': 'Blanca', 'Philip': 'Felipe', 'Margaret': 'Margarita',
                       'Josephine': 'Josefina', 'Cecily': 'Cecilia', 'Andrew': 'Andres', 'Hope': 'Esperanza',
                       'Marcus': 'Marcos', 'Arthur': 'Arturo', 'Leonard': 'Leonardo', 'Christian': 'Cristiano',
                       'Isabelle': 'Isabella', 'Rose': 'Rosa', 'Thomas': 'Tomas', 'Paul': 'Pablo',
                       'Xavier': 'Javier', 'Dominic': 'Domingo', 'Rosemary': 'Rosa Maria',
                       'Madeleine': 'Magdalena', 'Sophia': 'Sofia', 'Lucy': 'Lucia', 'Danielle': 'Daniela',
                       'Natalie': 'Natalia', 'Valerie': 'Valeria', 'Gabrielle': 'Gabriella', 'Marian': 'Mariana',
                       'Emerald': 'Esmeralda', 'Vivian': 'Viviana', 'Caroline': 'Carolina', 'April': 'Abril',
                       'June': 'Junio', 'Summer': 'Verano'}
    if name in name_dictionary:
        print('Your Spanish name is:', name_dictionary[name])
    else:
        print('Sorry, your name was not found in the database.')
    keep_going = input('Would you like to enter another name? Y/N: ')
    if keep_going not in ['Y', 'y', 'N', 'n']:
        keep_going = input('ERROR! Please enter Y/N: ')
    return keep_going


main()