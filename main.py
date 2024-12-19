"""
exercice lecture de données
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
        return [   [  int(elt)   for elt in l.strip().split(';')    ]     for l in f.readlines()  ]
    #     l = f.readlines()
    #     # l += f.readlines()
    #     # for elt in l[i]:
    #     #     l[elt].split(",")
    #     # i+=1
    # data = []
    # for s in l:
    #     lc = [  int(elt)       for elt in s.strip().split(';')       ]
    #     data.append(lc)
    #     # d = s.strip().split(';')
    #     # print(lc)
    # return data




def get_list_k(data, k):
    """
    gets list k
    """
    return data[k]

def get_first(l):
    """
    get first
    """
    return l[0]

def get_last(l):
    """
    get last
    """
    return l[-1]

def get_max(l):
    """
    get max
    """
    return max(l)

def get_min(l):
    """
    get min
    """
    return min(l)

def get_sum(l):
    """
    get sum
    """
    n = len(l)
    i=0
    result = 0
    while i < n:
        result += l[i]
        i+=1
    return result


#### Fonction principale


def main():
    """
    main
    """
    data = read_data(FILENAME)
    print(data)
    for i, l in enumerate(data):
        print(i,l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
