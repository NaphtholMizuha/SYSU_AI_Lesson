from dijkstra import dijkstra

if __name__ == '__main__':
    edges = []
    vertices = []
    v_dict = dict()
    file = open("Romania.txt", "r")
    v_size, e_size = file.readline().split()
    v_size = int(v_size)
    e_size = int(e_size)
    print("The size of vertices is {} and one of edges is {}".format(v_size, e_size))

    # input a graph
    for i in range(e_size):
        start, end, weight = file.readline().split()

        # process for capital insensitivity
        start = start.lower()
        end = end.lower()

        if vertices.count(start) == 0:
            vertices.append(start.lower())
            v_dict[start[0]] = start  # for searching by first letter
        if vertices.count(end) == 0:
            vertices.append(end.lower())
            v_dict[end[0]] = end  # for searching by first letter

        weight = int(weight)
        edges.append((start, end, weight))
        edges.append((end, start, weight))  # because all edges are undirected

    file.close()
    # it's time for the user
    while True:
        st = input("Please type your start city(type 'quit' to quit this program): ").lower()
        if st == 'quit':
            break
        elif len(st) == 1:
            st = v_dict.get(st)
            if st is None:  # error detect
                print("There is no such city!!!! Type again please.")
                continue
        elif vertices.count(st) == 0:  # error detect
            print("There is no such city!!!! Type again please.")
            continue

        ed = input("Please type your end city(type 'quit' to quit this program): ").lower()
        if ed == 'quit':
            break
        elif len(ed) == 1:
            ed = v_dict.get(ed)
            if ed is None:  # error detect
                print("There is no such city!!!! Type again please.")
                continue
        elif vertices.count(ed) == 0:  # error detect
            print("There is no such city!!!! Type again please.")
            continue

        print("start is \'{}\' and end is \'{}\'".format(st, ed))
        path, length = dijkstra(vertices, edges, st.lower(), ed.lower())
        log = open("log.txt", "a")
        if length != -1:
            print("The shortest path is {} and its length is {}.".format(path, length))  # put results
            log.write("{} to {}\npath: {}\nlength: {}\n\n".format(st, ed, path, length))  # logging
        else:
            print("These two vertices are not connected.")  # put results
            log.write("{} to {}\nfailed\n\n".format(st, ed))  # logging
        log.close()
