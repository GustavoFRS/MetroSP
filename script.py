from lines import *
from graph import *
from graph_search import bfs, dfs


def welcome():
    print('Hello and Welcome to Metro Navigator 3000!, we\'ll help you navigate through the São Paulo chaos!')


def get_origin():
    print('Our app currently have the following lines:\n')
    for i in range(1,6):
        print(f'Line {i}')
    line_number = int(input('\nWhich one are you coming from? type only the number: \n'))
    
    stations_to_print = {}
    if line_number in range(1,6):
        print(f'These are Line {line_number} stations:\n')
        for i in range(len(lines[line_number])):
            stations_to_print[i] = lines[line_number][i]
        print(stations_to_print)
        while True:
            try:
                line_key = int(input('Pick the corresponding number to the nearest station from you. \n'))
                if line_key not in stations_to_print.keys():
                    raise ValueError
                break
            except ValueError:
                print('\n Invalid input. please enter a number from the options presented')       
    else:
        print('It looks like that isn\'t a valid input, let\'s try again.')
        get_origin()
    return lines[line_number][line_key]



def get_destination():
    print('Our app currently have the following lines:\n')
    for i in lines.keys():
        print(f'Line {i}')
    line_number = int(input('\nWhich one are you going to? type only the number: \n'))
    
    stations_to_print = {}
    if line_number in lines.keys():
        print(f'These are Line {line_number} stations:\n')
        for i in range(len(lines[line_number])):
            stations_to_print[i] = lines[line_number][i]
        print(stations_to_print)
        while True:
            try:
                line_key = int(input('\nPick the corresponding number to your station of destiny.\n'))
                if line_key not in stations_to_print.keys():
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. please enter a number from the options presented')       
    else:
        print('It looks like that isn\'t a valid input, let\'s try again.')
        get_destination()
    return lines[line_number][line_key];


def metro_navigator_3000():
    welcome()
    route = get_route()
    print('\nThe shortest route between the two selected stations is:\n')
    for station in route[:-1]:
        print(f'{station} --->')
    print(route[-1])
    goodbye()


def get_route():
    origin = get_origin()
    destination = get_destination()
    bfs_route = bfs(graph, origin, destination)
    dfs_route = dfs(graph, origin, destination)

    if len(bfs_route) <= len(dfs_route):
        return bfs_route
    return dfs_route



def goodbye():
    print('\nThanks for using Metro Navigator 3000! We wish you a safe trip.')



metro_navigator_3000()