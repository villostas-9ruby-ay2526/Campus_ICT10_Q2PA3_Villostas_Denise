# Working with Dictionaries
from pyscript import display, document


def fav_game(e):
    document.getElementById('output').innerHTML = ' '
    favorite_game = document.getElementById('dict')

    game_devs = {
                'roblox' : 'David Baszucki',
                 'codm' : 'TiMi Studios',
                 'fnaf' : 'Scott Cawthon',
                 'minecraft' : 'Notch'
            } #specifying dictionaries

    game_check = fav_game in game_devs
    message_display = ('Sorry! Your input is not found in our game list', f'(game_devs) | (fav_game)')


    game_devs['genshin_impact'] = 'Hoyoverse' # adding a new element
    display(game_devs, target='output')

    
    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuples_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']

    display(dict(list_with_tuples), target='output')
    display(dict(tuples_with_strings), target='output')
    display(dict(list_with_strings), target='output')

    keywords = ['say', 'jm', 'jay', 'mace']
    values = ['esguerra', 'piansay', 'estrada', 'panela']

    combine = dict(zip(keywords, values)) #combining after conversion

    display(combine, target='output')

    philadelphia = {
        'c' : 'Joel Embiid',
        'pf' : 'Lebron James',
        'sf' : 'Jalen Brown',
        'sg' : 'VJ Edgecomb',
        'pg' : 'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry' # updating
    del philadelphia['sg']
    display(philadelphia, target='output')

    dict1 = {'x':1, 'y':2, 'z':3}
    dict2 = {'a':4, 'b':5, 'c':6}

    display(dict1 | dict2, target='output')

    merged_dictionary = {**dict1, **dict2}

    display(merged_dictionary, target='output')

    display(len(merged_dictionary), target='output') #countings

    ai = {'tony stark' : 'creator', 
          'J.A.R.V.I.S': 'AI_One',
          'F.R.I.D.A.Y.': 'AI_Two',
          'E.D.I.T.H.' : 'AI_Three',
          'V.I.S.I.O.N.': 'AI_Three',
          }

    display('V.I.S.I.O.N.' in ai, target='output')
    display(ai.get('J.A.R.V.I.S.'), target='output')
    display(ai.keys(), target='output')
    display(ai.values(), target='output')

