from clause_set import *


def parse_literal(ipt: str):
    neg = False
    if ipt[0] == '¬':
        neg = True
        ipt = ipt[1:]
    left_bracket = ipt.index('(')
    right_bracket = ipt.index(')')
    name = ipt[:left_bracket]
    args = ipt[left_bracket + 1:right_bracket].split(', ')
    return Literal(name, neg, args)


def parse_clause(ipt: str):
    if ipt[0] == '(' and ipt[-1] == ')':
        ipt = ipt[1:-1]
    ipt = list(ipt)
    level = 0
    for i in range(len(ipt)):
        if ipt[i] == '(':
            level += 1
        elif ipt[i] == ')':
            level -= 1
        elif ipt[i] == ',' and level == 0:
            ipt[i] = ';'
    clauses = ''.join(ipt)
    clauses = clauses.split('; ')
    clause_list = []
    for clause in clauses:
        clause_list.append(parse_literal(clause))
    return Clause(clause_list)


def parse_clause_set(ipt: List[str]):
    clauses = []
    for item in ipt:
        clauses.append(parse_clause(item))
    return ClauseSet(clauses)

