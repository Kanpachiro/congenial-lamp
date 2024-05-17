import cmath

# Note complex no. is stored as its own data type inside (), it is not a tuple and does not behave like one. The resemblence is in the notation only.

def matrix_multiplication(A:list,B:list):

    C = []
    for i in range(len(A)):
        row = []
        for s in range(len(B[0])):
            row.append(0+0j)
        C.append(row)

    for i in range(len(A)):
        for s in range(len(B[0])):
            for k in range(len(B)):
                C[i][s] = complex(C[i][s]) + complex(A[i][k]) * complex(B[k][s])
    return C


def ket_maker(bra:list):

    # Take bra and return ket

    ket = []
    for i in range (len(bra[0])):
        x = []
        conjugate_brai = bra[0][i].real - bra[0][i].imag * 1j
        x.append(conjugate_brai)
        ket.append(x)
    return bra, ket

#print(ket_maker([[2+3j, 4-2j, 5-9j]]))


def bra_maker(ket:list):

    # Take ket and return bra

    bra = []
    row = []
    for i in range (len(ket)):
        conjugate_keti = ket[i][0].real - ket[i][0].imag * 1j
        row.append(conjugate_keti)
    bra.append(row)
    
    return bra, ket

#print(bra_maker([[(2-3j)], [(4+2j)], [(5+9j)]]))


def bra_taker(n:int):

    # Take ket values and make a ket & bra
    #n = int(input('Give no. of components in psi \n'))
    print('Give components of bra psi seprated by Enter')
    bra_state = [[]]

    for i in range(n):
        bra_state_in = complex(input())
        bra_state[0].append(bra_state_in)

    ket_state = ket_maker(bra_state)

    print(bra_state, ket_state)

    return bra_state, ket_state


def ket_taker(n:int):

    # Take bra values and make a bra & ket
    #n = int(input('Give no. of components in psi \n'))
    print('Give components of bra psi seprated by Enter')
    ket_state = []

    for i in range(n):
        ket_state_in = complex(input())
        ket_state.append([ket_state_in])

    bra_state = bra_maker(ket_state)

    print(bra_state, ket_state)

    return bra_state, ket_state

# print(ket_maker([[1+1j, 3+2j]]))
# print(bra_maker([[1+0j], [3+2j]]))


def identifier(state:list):

    state_type = 'null'
    list_count = 0
    for i in range(len(state)):
        if type(state[i]) is list:
            list_count += 1
    
    if list_count == len(state) and len(state) > 1:
        state_type = 'ket'
    elif list_count == len(state) and len(state) == 1 and len(state[0]) > 1:
        state_type = 'bra'

    if state_type == 'null':
        print('IDENTIFIER FN ERROR')
    
    return state_type

#print(identifier([[1+0j], [4+2j]]))


def inner_product(psi:list, chi:list):

    if identifier(psi) == 'bra':
        bra_psi = ket_maker(psi)[0]
        ket_psi = ket_maker(psi)[1]
    elif identifier(psi) == 'ket':
        bra_psi = bra_maker(psi)[0]
        ket_psi = bra_maker(psi)[1]
    print('bra = ', bra_psi,'\nket = ', ket_psi)
    

    if identifier(chi) == 'bra':
        bra_chi = ket_maker(chi)[0]
        ket_chi = ket_maker(chi)[1]
    elif identifier(psi) == 'ket':
        bra_chi = bra_maker(chi)[0]
        ket_chi = bra_maker(chi)[1]
    print('bra = ', bra_chi,'\nket = ', ket_chi)

    z = matrix_multiplication(bra_chi,ket_psi)
    c = matrix_multiplication(bra_psi,ket_chi)

    print(z,'\n',c)

    return z

#inner_product([[1+0j, 4+2j]],[[1+0j, 4+3j]])


def outer_product(psi:list, chi:list):

    if identifier(psi) == 'bra':
        bra_psi = ket_maker(psi)[0]
        ket_psi = ket_maker(psi)[1]
    elif identifier(psi) == 'ket':
        bra_psi = bra_maker(psi)[0]
        ket_psi = bra_maker(psi)[1]
    print('bra = ', bra_psi,'\nket = ', ket_psi)
    

    if identifier(chi) == 'bra':
        bra_chi = ket_maker(chi)[0]
        ket_chi = ket_maker(chi)[1]
    elif identifier(psi) == 'ket':
        bra_chi = bra_maker(chi)[0]
        ket_chi = bra_maker(chi)[1]
    print('bra = ', bra_chi,'\nket = ', ket_chi)

    z = matrix_multiplication(ket_chi,bra_psi)
    c = matrix_multiplication(ket_psi,bra_chi)

    print('ket chi X bra psi',z,'\nket psi X bra chi',c)

    return z,c

#outer_product([[1+0j, 4+2j]],[[1+0j, 4+0j]])


def dagger(matrix:list):

    cct = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(0)
        cct.append(row)

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            cct[i][j] = matrix[j][i].real - matrix[j][i].imag * 1j
    
    return cct

#print(dagger([[1-1j],[2],[0+2j]]))


def check_hermitian(operator:list):

    return operator == dagger(operator)

def check_anti_hermitian(operator:list):

    return operator == -1 * dagger(operator)

def check_projection(operator:list):

    return operator == matrix_multiplication(operator,operator) and check_hermitian(operator)


def operation_ket(operator:list, ket:list):
    
    return matrix_multiplication(operator, ket)

def operation_bra(operator:list, bra:list):

    daggered_operator = dagger(operator)
    
    return matrix_multiplication(bra, daggered_operator)


def full_dirac(psi, operator, chi):

    if identifier(psi) == 'bra':
        bra_psi = ket_maker(psi)[0]
        ket_psi = ket_maker(psi)[1]
    elif identifier(psi) == 'ket':
        bra_psi = bra_maker(psi)[0]
        ket_psi = bra_maker(psi)[1]
    print('bra = ', bra_psi,'\nket = ', ket_psi)
    

    if identifier(chi) == 'bra':
        bra_chi = ket_maker(chi)[0]
        ket_chi = ket_maker(chi)[1]
    elif identifier(psi) == 'ket':
        bra_chi = bra_maker(chi)[0]
        ket_chi = bra_maker(chi)[1]
    print('bra = ', bra_chi,'\nket = ', ket_chi)

    operated_ket = operation_ket(operator, ket_chi)

    return matrix_multiplication(bra_psi, operated_ket)


def expectation_value(operator, state):
    
    exp = full_dirac(state, operator, state) / inner_product(state, state)

    return exp


