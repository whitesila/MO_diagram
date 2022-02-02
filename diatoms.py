class H:
    orbitals = [[1, 1, 1]]  # [n, s orbital, # of electrons]
    valence = 1
    max_electrons = 2

class F:
    orbitals = [[2, 1, 2], [2, 2, 5]]
    valence = 7
    max_electrons = 8

# orbital energy: 1,1< 2,1< 2,2< 3,1< 3,2< 4,1< 3,3< 4,2< 5,1< 4,3< 5,2< 6,1< 4,4< 5,3< 6,2< 7,1< 5,4< 6,3< 7,5


def how_orbitals_fill(atom_1, atom_2):
    orbitals = [0]
    least = least_energy(atom_1, atom_2)
    if atom_1 == atom_2:
        orbitals *= atom_2.max_electrons
    else:
        orbitals *= least.max_electrons
    print(orbitals)


def is_exception(atom):
    exceptions = [C, Si]
    for atoms in exceptions:
        if atom == atoms:
            return True
    return False


def least_energy(atom_1, atom_2):  # this will specify energy differences for hetero-diatoms
    if atom_1.orbitals[-1][0] > atom_2.orbitals[-1][0]:
        return atom_1
    elif atom_1.orbitals[-1][0] < atom_2.orbitals[-1][0]:
        return atom_2
    else:
        if atom_1.orbitals[-1][1] > atom_2.orbitals[-1][1]:
            return atom_1
        else:
            return atom_2


how_orbitals_fill(F, H)
