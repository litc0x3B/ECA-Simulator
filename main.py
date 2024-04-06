import random

#--------------FUNCTIONS-------------------------------------
CELL_CHARS = ['░', '█']

def get_neighborhood(state: list, start: int, end: int):
    result = []
    for i in range(start, end + 1):
        result.append(state[i % len(state)])
    return result

def int_to_bin_list(num: int, length=None):
    res = list(map(int, bin(num).replace('0b', '')))
    if length is not None:
        res = [0] * (length - len(res)) + res
    return res

def calc_state(rule: int, neighborhood: list):
    rule_bin = int_to_bin_list(rule, length=2**len(neighborhood))
    rule_bin.reverse()
    neighborhood_int = int('0b' + ''.join(map(str, neighborhood)), base=2)
    return rule_bin[neighborhood_int]
    
def simulate(initial_state: list, rule: int, neighborhood_size: int, turns: int):
    cur_state = initial_state.copy()
    for i in range(turns):
        print(''.join(CELL_CHARS[el] for el in cur_state))
        prev_state = cur_state.copy()
        for i in range(len(cur_state)):
            neighborhood = get_neighborhood(prev_state, i - neighborhood_size // 2, i + neighborhood_size // 2)
            cur_state[i] = calc_state(rule, neighborhood)

def show_rules(rule: int, neighborhood_size: int):
    for i in reversed(range(2**neighborhood_size)):
        neighborhood = int_to_bin_list(i, length=neighborhood_size)
        print(''.join(CELL_CHARS[el] for el in neighborhood), end=' ')
    print()
    
    for i in reversed(range(2**neighborhood_size)):
        neighborhood = int_to_bin_list(i, length=neighborhood_size)
        print((neighborhood_size // 2) * ' ' + CELL_CHARS[calc_state(rule, neighborhood)] + (neighborhood_size // 2) * ' ', end=' ')      
    print()
#----------------------------------------------------------------------


#-------------------------------------CONSTANTS------------------------
# random.seed(10)
SIZE = 1000
N = 30
NEIGHBORHOOD_SIZE = 3
TURNS = 1000
# RULE = random.randint(0, 2**(2**NEIGHBORHOOD_SIZE))
RULE = 90
STATE = [random.randint(0, 1) for i in range(SIZE // 2 - N + 1, SIZE // 2 + N)]
STATE = [0] * (SIZE // 2 - N) + STATE + [0] * (SIZE // 2 - N)
#-----------------------------------------------------------------------

#--------------------------------MAIN BODY---------------------------------
print('rule:', RULE)
show_rules(RULE, NEIGHBORHOOD_SIZE)
print()
simulate(initial_state=STATE, rule=RULE, neighborhood_size=NEIGHBORHOOD_SIZE, turns=TURNS)   
#---------------------------------------------------------------------------