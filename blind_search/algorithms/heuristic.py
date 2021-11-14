def heuristic_manhattan(state):
    res = 0
    goal = state.get_goal()
    
    for i in range(state.size * state.size):
        x, y = state.table(i)
        x_t, y_t = state.table( goal.index( state.state[i] ) )  
        res += abs(x - x_t) + abs(y - y_t)
    
    return res


def heuristic_default(state):
    return state.cost + 1
