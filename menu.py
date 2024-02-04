from tabulate import tabulate
import pandas as pd
from kniffel_art import logo
from display_table import clear
from wuerfel_data import *


def display_menu():
    print(logo)
    print("Herzlich Willkommen zum Kniffels Welt !!!\n\n\n")
    users_number = int(input("Geben Sie bitte der Anzahl des Spielers ein (2 / 8): "))
    namen_list = []
    for index in range(1, users_number + 1):
        name = input(f"Geben Sie bitte der {index} name des Spielers ein: ").capitalize()
        tabelle_data[name] = [x[1] for x in data_dict.values()]
        namen_list.append(name)

    data = pd.DataFrame.from_dict(tabelle_data, orient='index')
    data = data.transpose()

    new_header = ['Games'] + namen_list
    print(tabulate(data, showindex=False, headers=new_header, tablefmt="heavy_grid"))
    data.to_csv('score.csv', index=False)
    input("Sind Sie bereit? /Enter/ ")
    clear()
    spiel_extract = {}
    for name in namen_list:
        spiel_extract[name] = [[], 0]

    spielen_list = list(data_dict.keys())
    keys_runden = list(spiel_runden.keys())
    values_runden = list(spiel_runden.values())

    return namen_list, new_header, data, spiel_extract, spielen_list, keys_runden, values_runden


