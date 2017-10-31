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

def random_mdl_color():
    return random.choice(MDL_COLORS)
