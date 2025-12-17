class Transportation:
    def __init__(self, N):
        self.N = N
    def StartState(self):
        return 1
    def EndState(self, end):
        return end==self.N
    def SuccAction(self, state):
        result = []
        if state + 1 <= self.N:
            result.append(('walk', state+1))
        if state*2 <= self.N:
            result.append(('tram', state*2))
        return result
#problem = Transportation(N=4)
#print(problem.SuccAction(1))
#Main
def Backtracking(problem):
        ## potential state
        best_cost = float('inf')
        best_path = []
        def backtrack(state, current_path, current_cost):
            nonlocal best_cost, best_path
            if problem.EndState(state):
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_path = list(current_path)
                print(current_path)
                current_path = []
                return
            result = problem.SuccAction(state)
            current_cost = current_cost + 1
            for action, state in result:
                current_path.append((action,state))
                backtrack(state, current_path, current_cost)
                current_path.pop()
            return best_cost, best_path
        print(backtrack(problem.StartState(), current_path=[], current_cost=0))
print(Backtracking(Transportation(10)))
