from collections import Counter
from wuerfel_data import wuerfel
from wuerfel_liste import erste_versuch, wuerfel_waehlen


def is_consistent(list1, list2):
    return Counter(list1) <= Counter(list2)


def anzahl_punkte(solution, spiel, list_, sol):
    if spiel == "Kniffel":
        solution.append(50)
    elif spiel == "Grosse Strasse":
        solution.append(40)
    elif spiel == "Kleine Strasse":
        solution.append(30)
    elif spiel == "Full House":
        solution.append(25)
    elif spiel in ["Viererpasch", "Dreierpasch"]:
        solution.append(sum(sol))
    elif spiel in [f"{i}er" for i in range(6, 0, -1)]:
        solution.append(sum(list_))
    return solution


def spiel_bestaetigen(wuerfel_data, my_sol, all_games):
    found = False
    max_punkte = {}
    found_spiel = ""
    found_list = []
    er_max = 0
    for spiel, possib in wuerfel_data.items():
        for lists in possib:
            if spiel not in all_games:
                if is_consistent(lists, my_sol[0]):
                    if spiel not in [f"{i}er" for i in range(6, 0, -1)]:
                        found_spiel = spiel
                        found_list = lists
                        found = True
                        break
                    else:
                        if spiel not in list(max_punkte.keys()):
                            max_punkte[spiel] = lists
                elif spiel == 'Chance':
                    max_punkte[spiel] = my_sol[0]
        if found:
            break
    else:
        if len(list(max_punkte.keys())) >= 1:
            if "Chance" in all_games:
                input("ACHTUNG! Du hast schon die 'Chance' benutzt.")
            bevorzugte_spiel = input(f"\nGeben Sie bitte ein, "
                                     f"welche Spiel moechten Sie in der Tabelle eintragen."
                                     f"\nOptionen: {list(max_punkte.keys())}: ")
            for spiel, er_item in max_punkte.items():
                if spiel == bevorzugte_spiel.capitalize():
                    found_spiel = spiel
                    found_list = er_item
                    er_max = sum(er_item)
    if found:
        found_sol = [found_spiel, found_list, my_sol[0]]
        # print(found_sol)
        return anzahl_punkte(found_sol, found_sol[0], found_sol[1], found_sol[2])
    else:
        found_sol = [found_spiel, found_list, my_sol[0], er_max]
        # print(found_sol)
        return found_sol


def final_results(all_games):
    wuerfel_list = erste_versuch()
    wuerfel_verarbeiten = input("Möchten Sie einige Wuerfeln verarbeiten (ja / nein)? ").lower()
    if wuerfel_verarbeiten == 'ja':
        final_wuerfel_list = wuerfel_waehlen(wuerfel_list)
        punkte = spiel_bestaetigen(wuerfel, final_wuerfel_list, all_games)
        print(f"{punkte[0:2]}. Result: {punkte[3]}")
        return [punkte, wuerfel_verarbeiten, final_wuerfel_list[1]]
    else:
        punkte = spiel_bestaetigen(wuerfel, wuerfel_list, all_games)
        print(f"{punkte[0:2]}. Result: {punkte[3]}")
        return [punkte, wuerfel_verarbeiten, ""]

