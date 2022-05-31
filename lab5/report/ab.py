history_map = {}
# 此处初始化history
def history_get(x):
    if not history_map[x]:
        history_map[x] = 0
    return history_map[x]

def history_renew(x, depth):
    history_map[x] += 2 << depth

def alpha_beta(state, alpha, beta, depth):
    if depth == 0:
        return evaluate(state)
    camp = 'r' if depth % 2 == 0 else 'b' # 深度决定行动方
    steps = generate_possbile_steps(state, camp)
    steps.sort(key=history_get)
    next_states = [make_nxt_state(state, src, dst) for src, dst in steps]
    target = None
    for i, next_state in enumerate(next_states):
        temp = alpha_beta(next_state, -beta, -alpha, depth - 1)
        if temp > alpha:
            alpha = temp
            target = steps[i]
        if alpha >= beta:
            break

    if target is not None:
        history_renew(target, depth)
    return alpha
