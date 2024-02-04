from os import system, name
from tabulate import tabulate


def clear():
    if name == 'nt':
        _ = system('cls')


def table_print(**kwargs):
    kwargs["spiel_extract"].append(kwargs["spiel"])
    kwargs["data"].at[kwargs["spielen_list"].index(kwargs["spiel"]), kwargs["name"]] = kwargs["punkte"]
    kwargs["data"].to_csv('score.csv', index=False)
    print(tabulate(kwargs["data"], showindex=False, headers=kwargs["headers"], tablefmt="heavy_grid"))
    return
