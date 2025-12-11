"""
Lecture de données
"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.strip().split(';')
            int_list = [int(x) for x in elements if x.strip()]
            l.append(int_list)
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste de la structure de données.

    Args:
        data (list): la liste de listes (le contenu du fichier)
        k (int): l'indice de la liste à récupérer

    Returns:
        list: la k-ième liste, ou une liste vide si l'indice est hors limites
    """
    l = []
    if 0 <= k < len(data):
        l = data[k]
    return l

def get_first(l):
    """Retourne le premier élément d'une liste.

    Args:
        l (list): la liste d'entiers

    Returns:
        int: le premier élément, ou None si la liste est vide
    """
    if len(l)>0:
        return l[0]
    return None

def get_last(l):
    """Retourne le dernier élément d'une liste.

    Args:
        l (list): la liste d'entiers

    Returns:
        int: le dernier élément, ou None si la liste est vide
    """
    if len(l)>0:
        return l[-1]
    return None

def get_max(l):
    """Retourne le maximum d'une liste.

    Args:
        l (list): la liste d'entiers

    Returns:
        int: la valeur maximale, ou None si la liste est vide
    """
    if len(l)>0:
        return max(l)
    return None

def get_min(l):
    """Retourne le minimum d'une liste.

    Args:
        l (list): la liste d'entiers

    Returns:
        int: la valeur minimale, ou None si la liste est vide
    """
    if len(l)>0:
        return min(l)
    return None

def get_sum(l):
    """Retourne la somme des éléments d'une liste.

    Args:
        l (list): la liste d'entiers

    Returns:
        int: la somme, ou None si la liste est vide
    """
    if len(l) > 0:
        return sum(l)
    return None


#### Fonction principale


def main():
    """Fonction principale pour tester les fonctions secondaires."""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
