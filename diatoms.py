class C:


class Si:


class H:
    orbitals = [[1, 1, 1]]  # [n, s orbital, # of electrons]


class F:
    orbitals = [[2, 1, 2], [2, 2, 5]]

# orbital energy: 1,1< 2,1< 2,2< 3,1< 3,2< 4,1< 3,3< 4,2< 5,1< 4,3< 5,2< 6,1< 4,4< 5,3< 6,2< 7,1< 5,4< 6,3< 7,5


def how_orbitals_fill(atom_1, atom_2):
    MO = list
    MO.append(fill_s(atom_1, atom_2))


def fill_s(atom_1, atom_2):
    MO = list
    if atom_1 == atom_2 and not is_exception(atom_1):
        for item in atom_2.orbitals:
            if item[1] == 1 and item[2] == 2:
                x = item
                x.append('b')
                MO.append(item)
                x = item
                x.append('a')
                MO.append()
            else:
                
    else:

def is_exception(atom):
    exceptions = [C, Si]
    for atoms in exceptions:
        if atom == atoms:
            return True
    return False

def most_energy(atom_1, atom_2):  # this will specify energy differences for hetero-diatoms
    if atom_1.orbitals[-1][0] > atom_2.orbitals[-1][0]:
        return atom_1
    elif atom_1.orbitals[-1][0] < atom_2.orbitals[-1][0]:
        return atom_2
    else:
        if atom_1.orbitals[-1][1] > atom_2.orbitals[-1][1]:
            return atom_1
        elif atom_1.orbitals[-1][1] < atom_2.orbitals[-1][1]:
            return atom_2
        else:
            return 'Homo-diatom'


print(most_energy(H, H))
