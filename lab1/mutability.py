if __name__ == '__main__':
    i = 114514
    print(id(i))
    i += 1
    print(id(i))

    f = 3.14
    print(id(f))
    f *= 2.23
    print(id(f))

    b = True
    print(id(b))
    b = not b
    print(id(b))

    s = 'hello'
    print(id(s))
    s = s.replace('he', 'Fe')
    print(id(s))

    t = (1, 'what', 2.13)
    print(id(t))
    t = (2, 'which', 0.01)
    print(id(t))

    print('\n')

    li = [1, 1, 4, 5, 1, 4]
    print(id(li))
    li.append(7)
    print(id(li))

    d = dict([('this', 'fish'), ('that', 'meat')])
    print(id(d))
    d.clear()
    print(id(d))

    s = {'group', 'ring', 'field'}
    print(id(s))
    s.union({'plus', 'ring'})
    print(id(s))