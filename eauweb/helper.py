import random

MDL_COLORS = [
    'mdl-color--red',
    'mdl-color--red-900',
    'mdl-color--red-A400',
    'mdl-color--pink',
    'mdl-color--pink-200',
    'mdl-color--purple',
    'mdl-color--purple-A200',
    'mdl-color--indigo',
    'mdl-color--blue',
    'mdl-color--light-blue',
    'mdl-color--light-blue-A400',
    'mdl-color--teal',
    'mdl-color--green',
    'mdl-color--light-green',
    'mdl-color--lime',
    'mdl-color--amber',
    'mdl-color--orange',
    'mdl-color--blue-grey'
]

OFFICER_POSITIONS = { 
        'President' : 1,
        'Vice President' : 2,
        'Finance Chair': 3,
        'Performance Chair' : 4,
        'Marketing Chair': 5,
        'Social Chair': 6,
        'Technology Chair': 7,
        'Event Chair': 8,
        'Finance Chair Intern' : 9,
        'Performance Chair Intern' : 10,
        'Marketing Chair Intern' : 11,
        'Social Chair Intern': 12,
        'Technology Chair Intern' : 13, 
        'Event Chair Intern' : 14, 
        'Dinosaur' : 15, 
        'Senior Advisor' : 15
    }

def random_mdl_color():
    return random.choice(MDL_COLORS)

def officer_sort_order(position):
    return OFFICER_POSITIONS.get(position, 999)
