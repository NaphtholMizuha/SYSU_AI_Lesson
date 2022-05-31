from clause import *

def place_to_str(place: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    """
    To turn place vector into string.
    :param place: A List of 2*(2*2) tensor.
    :return: String like '1a-7b, 12a,42z'
    """
    result = ''
    if len(place) > 0:
        result += '['
        for pairs in place:
            result += str(pairs[0][0] + 1) + chr(ord('a') + pairs[0][1]) + '-' + str(pairs[1][0] + 1) + chr(ord('a') + pairs[1][1]) + ', '
        result = result[:-2] + ']'
    return result

def mgu_to_str(mgu: Mapping):
    res = ''
    if len(mgu) != 0:
        res += '{'
        for k, v in mgu.items():
            res += k + ':=' + v + ', '
        res = res[:-2] + '}'
    return res

class ClauseSet:
    def __init__(self, clauses: List[Clause]):
        self.is_prime = {}
        self.clauses = clauses

        for clause in self.clauses:
            self.is_prime[clause] = False

        self.is_prime[self.clauses[-1]] = True

    def __str__(self):
        result = ''
        i = 1
        for clause in self.clauses:
            result += str(i) + '.'
            result += clause.__str__()
            result += '\n'
            i += 1
        return result[:-1]

    def extend(self, li: List[Clause]):
        for clause in li:
            self.clauses.append(clause)

    def get_places(self, this: Clause, that: Clause, unify_literals: List[Tuple[Literal, Literal]]):
        places = []
        for literal_pair in unify_literals:
            places.append(((self.clauses.index(this), this.literals.index(literal_pair[0])),
                           (self.clauses.index(that), that.literals.index(literal_pair[1]))))
        return places

    def reasoning(self):
        count = len(self.clauses) + 1
        resolved = []
        while True:
            buffer = []  # to store the new clauses because the resolutions are regard as synchronous.
            for this_clause in self.clauses:
                for that_clause in self.clauses:
                    # traversal the cartesian product of the clauses
                    unify_literal_pairs = this_clause.is_resolvable_at(that_clause)
                    if this_clause != that_clause and len(unify_literal_pairs) != 0 and (self.is_prime[this_clause] or self.is_prime[that_clause]) and resolved.count((this_clause, that_clause)) == 0:
                        # The 1st is a new clause, the 2nd is MGU used to make that clause
                        son_clause, mgu = this_clause.resolve(that_clause, unify_literal_pairs)
                        places = place_to_str(self.get_places(this_clause, that_clause, unify_literal_pairs))
                        buffer.append(son_clause)
                        print(str(count) + '. R' + places + mgu_to_str(mgu) + ' = ' + son_clause.__str__())
                        count += 1
                        resolved.append((this_clause, that_clause))
                        resolved.append((that_clause, this_clause))
                        if len(son_clause.literals) == 0:
                            return
            #
            for clause in buffer:
                self.is_prime[clause] = True
            self.extend(buffer)
