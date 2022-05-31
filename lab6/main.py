from climbing import *
from annealing import *
from genetic import Population
from graph import NodeGraph
from time import time
np.set_printoptions(threshold = 10000)
if __name__ == '__main__':
    graph = NodeGraph('data/kroB150.tsp')
    init_state = np.arange(graph.dimension)

    graph.draw(init_state, f'初始状态图 (总权值: {int(graph.weight(init_state))})')
    np.random.shuffle(init_state)
    print(f'we start from {init_state} with weight {graph.weight(init_state)}')

    # direct climbing
    start_time = time()
    result = climb(init_state, graph)
    end_time = time()
    duration = end_time - start_time
    print(f'The best(?) path is:\n{result}\nwith weight {graph.weight(result)} by direct climbing and it takes {duration} secs.')
    graph.draw(result, f'直接登山法结果 (总权值: {int(graph.weight(result))}, 用时: {duration}s)')

    # variable neighbor climing
    start_time = time()
    result = climb_var(init_state, graph)
    end_time = time()
    duration = end_time - start_time
    print(f'The best(?) path is:\n{result}\nwith weight {graph.weight(result)} by variable neighbor climbing and it takes {end_time - start_time} secs.')
    graph.draw(result, f'多邻域登山法结果 (总权值: {int(graph.weight(result))}, 用时: {duration}s)')
    
    # simulate_annealing
    start_time = time()
    result = simulate_annealing(init_state, graph)
    end_time = time()
    duration = end_time - start_time
    graph.draw(result, f'模拟退火算法结果 (总权值: {int(graph.weight(result))}, 用时: {duration}s)')
    print(f'The best(?) path is:\n{result}\nwith weight {graph.weight(result)} by simulate annealing and it takes {end_time - start_time} secs.')

    population = Population(100, 15000, graph)
    start_time = time()
    result = population.evolve()
    end_time = time()
    duration = end_time - start_time
    graph.draw(result, f'遗传算法结果 (总权值: {int(graph.weight(result))}, 用时: {duration}s)')
    print(f'The best(?) path is:\n{result}\nwith weight {graph.weight(result)} by genetic and it takes {end_time - start_time} secs.')


