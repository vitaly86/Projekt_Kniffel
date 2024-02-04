import pandas as pd


def sum_oberer_teil(namen_list, data, spielen_list):
    oberer_teil = {}
    for index, name in enumerate(namen_list, 1):
        final_data = pd.read_csv('score.csv', usecols=[index], nrows=6)
        lists = final_data.fillna(0).values.astype(int).tolist()
        suma = 0
        for list_ in lists:
            suma += list_[0]
        oberer_teil[name] = suma
        bonus = 35 if suma >= 63 else 0
        data.at[spielen_list.index("Gesamtpunktzahl"), name] = suma
        data.at[spielen_list.index("Bonus (bei 63+)"), name] = bonus
        data.at[spielen_list.index("Gesamt (Oberer Teil)"), name] = suma + bonus
    return oberer_teil


def sum_unterer_teil(namen_list, data, spielen_list):
    unterer_teil = {}
    for index, name in enumerate(namen_list, 1):
        final_data = pd.read_csv('score.csv', usecols=[index], nrows=16, skiprows=9)
        lists = final_data.fillna(0).values.astype(int).tolist()
        suma = 0
        for list_ in lists:
            suma += list_[0]
        unterer_teil[name] = suma
        data.at[spielen_list.index("Gesamt (Unterer Teil)"), name] = suma
    return unterer_teil


def sum_gesamt(oberer_teil, unterer_teil, data, spielen_list):
    endsumme_dict = {}
    for name in oberer_teil.keys():
        endsumme = oberer_teil[name] + unterer_teil[name]
        endsumme_dict[name] = endsumme
        data.at[spielen_list.index("Endsumme"), name] = endsumme
    return endsumme_dict
