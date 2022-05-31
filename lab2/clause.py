from literal import *
import copy


def replace(literal: Literal, mgu):
    new_args = [mgu.get(arg, arg) for arg in literal.args]
    return Literal(name=literal.name, neg=literal.neg, args=new_args)


def include(li: List[Tuple[Literal, Literal]], x: Literal):
    for item in li:
        if item[0] == x or item[1] == x:
            return True
    return False

def is_in(li: List[Literal], x: Literal):
    for literal in li:
        if x.same(literal):
            return True
    return False


def find_mgu(li: List[Tuple[Literal, Literal]]):
    mgu = {}
    for this, that in li:
        for this_arg, that_arg in zip(this.args, that.args):
            if is_variable(this_arg) and mgu.get(that_arg, that_arg) != this_arg:
                mgu[this_arg] = that_arg
            elif is_variable(that_arg) and mgu.get(this_arg, this_arg) != that_arg:
                mgu[that_arg] = this_arg
    return mgu


class Clause:

    def __init__(self, literals: List[Literal]):
        self.literals = literals

    def __str__(self):
        result = ''
        if len(self.literals) > 0:
            if len(self.literals) > 1:
                result += '('
            for literal in self.literals:
                result += literal.__str__()
                if len(self.literals) > 1 and literal != self.literals[-1]:
                    result += ', '
            if len(self.literals) > 1:
                result += ')'
        else:
            result += 'NIL'
        return result

    def is_resolvable_at(self, other):
        """
        To test whether the two clauses can be resolved together
        :param other: another clause
        :return: a boolean value
        """
        result = []
        for this in self.literals:
            for that in other.literals:
                if this.is_unifiable_with(that) and result.count((that, this)) == 0:
                    result.append((this, that))
        return result

    def resolve(self, other, unify_literals: List[Tuple[Literal, Literal]]):
        """
        Main process of resolution reasoning
        :param unify_literals: Literal pairs found by function 'is_resolvable_at()'
        :param other: another clause
        :return: 1.new clause spanned by resolution, 2.MGU, 3.Coordinates of unified literals
        """
        new_literals = []
        deduplicated_literals = []
        for literal in self.literals:
            if not include(unify_literals, literal):
                new_literals.append(copy.deepcopy(literal))

        for literal in other.literals:
            if not include(unify_literals, literal):
                new_literals.append(copy.deepcopy(literal))

        mgu = find_mgu(unify_literals)
        # replace the variables, following MGU.
        for i in range(len(new_literals)):
            new_literals[i] = replace(new_literals[i], mgu)

        # filter out the duplicated literals.
        for item in new_literals:
            for jtem in deduplicated_literals:
                if item.same(jtem):
                    break
            else:
                deduplicated_literals.append(item)

        return Clause(deduplicated_literals), mgu
