import funcs
import copy

def local_search(s):
    a = copy.deepcopy(s)
    count = 0
    while True:
        # funcs.scramble(a)
        funcs.swap(a)
        funcs.swap_2(a)
        # funcs.inversion(a)
        if a.get_distance() < s.get_distance() or count > 1000:
            print(f'{a}, count: {count}')
            s = copy.copy(a)
            break
        count += 1


