from clause import *
from parse import *

if __name__ == '__main__':
    a = parse_clause('P(x, y, z), Q(aa, bb), R(v)')
    b = parse_clause('¬P(aa, bb, cc), ¬Q(u, v), S(x)')
    clause_set = ClauseSet([a, b])
    res = a.is_resolvable_at(b)
    for (s, t) in res:
        print('{}: {}'.format(s, t))
    k, mgu = a.resolve(b, res)
    print(k)
    print(mgu_to_str(mgu))
    places = clause_set.get_places(a, b, res)
    print(place_to_str(places))