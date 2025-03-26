# function for different colors, for practice
def bar_colour(subjects_df):
    colour_huvudman = {
        'Skolverket': 'purple',
        'Kommunal': 'green',
        'Enskild': 'blue',
        'Samtliga': 'orange'
    }
    return [colour_huvudman.get(huvudman, 'black') for huvudman in subjects_df["Huvudman"]]