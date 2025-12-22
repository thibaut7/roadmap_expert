#Formalize the transportation problem
#Policy evaluation
#Value iteration

#------------------------------------------------#
#                  Transportation Problem
#-------------------------------------------------#
#Street with blocks numbered 1 to n
#Walking from s to s+1 takes 1 minutes
#Taking a magic tram from s to 2s takes 2 minutes.
#How to travel from 1 to n in the least time
#Tram fails with probability 0.5

#-------------------Model
class Transportation:
    def __init__(self, n):
        self.n = n
    
    def start(self):
        return 1

    def isEnd(self, s):
        #Check if in end state n
        return s==self.n
    
    def action(self, s):
        result = []
        if s+1 <= self.n:
            result.append('walk')
        if s*2 <= self.n:
            result.append('tram')
        return result

    def successor(self, s, action):
        # For a state s and action find the successor
        # prob = T(s, a, s'), reward = R(s, a, s')
        # result=(T, R, s')
        result = []
        if action == 'walk':
            result.append((1, -1, s+1))
        elif action== 'tram':
            result.append((0.5, -2, s*2))
            result.append((0.5, -2, s))
        return result
    def discount(self):
        return 1

def valueIteration(MDP, s):
    def expected(s, a):
        return sum(t*(r + MDP.discount()*valueIteration(MDP, newState)) for t,r ,newState in MDP.successor(s, a))
    if MDP.isEnd(s):
        return 0
    else:
        return max(expected(s,a) for a in MDP.action(s))

MDP = Transportation(6)
print(MDP.action(2))
print(MDP.successor(2, 'walk'))
print(MDP.successor(2, 'tram'))
print(valueIteration(MDP, 1))
