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
#problem = Transportation(N=6)
#print(problem.SuccAction(1))
#Main
def Backtracking(problem):
        ## potential state
        history = {}
        def backtrack(state):
            #print(state)
            result = problem.SuccAction(state)
            history[state] = result
            print(result)
            if problem.EndState(state):
                print('fin')
                return
            for state in result:
                print(state)
                backtrack(state[1])
        backtrack(problem.StartState())
print(Backtracking(Transportation(6)))
