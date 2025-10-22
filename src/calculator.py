from .utils import add, sub, mul, div


def calculator():
    while True:
        try:
            x = float(input("Entrez le premier nombre : "))
            y = float(input("Entrez le deuxième nombre : "))
            menu = input("Choisis une opération : 1 = multiplication, 2 = soustraction, 3 = division, 4 = addition : ")

            if menu == "1":
                print("Résultat :", mul(x, y))
            elif menu == "2":
                print("Résultat :", sub(x, y))
            elif menu == "3":
                if y == 0:
                    raise ZeroDivisionError("Division par zéro interdite.")
                print("Résultat :", div(x, y))
            elif menu == "4":
                print("Résultat :", add(x, y))
            else:
                print("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")
        except ZeroDivisionError as e:
            print("Erreur :", e)

        again = input("Souhaitez-vous faire un autre calcul ? (o/n) : ").lower()
        if again != "o":
            print("À bientôt !")
            break


# exemple d'utilisation
if __name__ == "__main__":
    calculator()
