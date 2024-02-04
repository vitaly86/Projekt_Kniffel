from tabulate import tabulate
from kniffel_art import logo, spiel_beenden_logo
from wuerfel_data import *
from tabelle_ausfuellen import *
from tabelle_berechnen import *
from display_table import clear
import time

contor = 1
for index in range(len(spielen_list) - 5):
    # for index in range(5):
    for name in namen_list:
        print(
            f"Runde {contor}: {name}, du bist dran" if contor < 13 else f"ACHTUNG!\nLetzte Runde: {name}, du bist dran")
        input("Druecken Sie die Taste Enter, wenn Sie bereit sind der Spiel anzufangen...")
        insert_punkte_in_tabelle(name)
    if contor < 13:
        end_game = input(f"Nach "
                         f"{keys_runden[values_runden.index(contor)].upper() if contor < 13 else None} "
                         f"Runde moechten Sie schon das Spiel beenden? "
                         f"Drueken Sie 'q' wenn 'ja':\n ").lower()
        clear()
        if end_game == "q":
            print(spiel_beenden_logo)
            print("\n\n\nEs tut uns so leid, wir koennen die finale Ergebnisse in der Tabelle nicht eintragen.")
            break
        else:
            print(f"-----------------------Runde {contor}------------------------")
            print(tabulate(data, showindex=False, headers=new_header, tablefmt="heavy_grid"))
    contor += 1
else:
    print("\nVielen Dank fuer Ihre Teilnahme. Das Spiel ist beendet.")
    time.sleep(3)
    clear()
    print(logo)

    oberer_teil = sum_oberer_teil(namen_list, data, spielen_list)
    unterer_teil = sum_unterer_teil(namen_list, data, spielen_list)
    endsumme_dict = sum_gesamt(oberer_teil, unterer_teil, data, spielen_list)

    print(tabulate(data, showindex=False, headers=new_header, tablefmt="heavy_grid"))
    data.to_csv('score.csv', index=False)

    time.sleep(5)
    gewinners = []
    gewinner_values = sorted(list(endsumme_dict.values()), reverse=True)
    count_max_punkte = gewinner_values.count(gewinner_values[0])

    platz = 1
    table_header = ['Platz', "Spieler", "Punkten"]
    for punkte in gewinner_values:
        for name, namen_punkt in endsumme_dict.items():
            if punkte == namen_punkt and name not in gewinners:
                gewinners.append(name)
                rang_tabelle["Platz"].append(platz)
                rang_tabelle["Spieler"].append(name)
                rang_tabelle["Punkten"].append(punkte)

        last_table = pd.DataFrame.from_dict(rang_tabelle, orient='index')
        last_table = last_table.transpose()
        clear()
        print(logo)
        print("Rangliste der Teilnehmern:\n\n")
        print(tabulate(last_table, showindex=False, headers=table_header, tablefmt="heavy_grid"))
        time.sleep(0.7)
        if gewinner_values.count(punkte) > 1:
            for _ in range(1, gewinner_values.count(punkte)):
                gewinner_values.remove(punkte)
        platz += 1

    print("\n\n\nHerzlichen Glückwunsch", end=" ")
    for number_gewinners in range(count_max_punkte):
        print(gewinners[number_gewinners].upper(), end=", ")
    print(f"{'Sie haben gewonnen!' if count_max_punkte > 1 else 'du hast gewonnen!'}")


