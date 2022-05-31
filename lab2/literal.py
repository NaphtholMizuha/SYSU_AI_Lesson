from typing import *


def is_variable(x: str):
    return len(x) == 1


class Literal:  # Literal have 3 attributes: name, args and neg
    # exp: ¬P(x, y) for name 'P', args '[x, y]' and neg 'True'.
    def __init__(self, name: str, neg: bool, args: List[str]):
        self.name = name
        self.args = args
        self.neg = neg

    def __str__(self):
        res = ""
        if self.neg:
            res += "¬"
        res += self.name
        if len(self.args) != 0:
            res += "("
            for item in self.args:
                res += item
                if item != self.args[-1]:
                    res += ", "
            res += ")"
        return res

    def is_unifiable_with(self, other):
        """
        To test whether the two literals can be unified together
        :param other: another literal
        :return: a boolean value
        """
        if self.name == other.name and self.neg != other.neg:
            for this, that in zip(self.args, other.args):
                if not (is_variable(this) or is_variable(that) or this == that):
                    break
            else:  # it means that all the arguments pair are unifiable
                return True
        return False

    def same(self: Literal, other: Literal):
        """
        Judge whether the two Literal are the same(careless about identity).
        :param other:
        :return:
        """
        if self.name == other.name and self.neg == other.neg:
            for this, that in zip(self.args, other.args):
                if this != that:
                    break
            else:
                return True
        return False
