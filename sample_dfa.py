import graphviz

# Create a DFA for L = (111 + 11111)*
dfa = graphviz.Digraph(format='png')
dfa.attr(rankdir='LR')

# States
states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
for state in states:
    if state == 'q0' or state == 'q3' or state == 'q5':
        dfa.attr('node', shape='doublecircle')
    else:
        dfa.attr('node', shape='circle')
    dfa.node(state)

# Transitions
dfa.edge('q0', 'q1', label='1')
dfa.edge('q1', 'q2', label='1')
dfa.edge('q2', 'q3', label='1')
dfa.edge('q3', 'q4', label='1')
dfa.edge('q4', 'q5', label='1')

# Loop back from accepting states
dfa.edge('q3', 'q1', label='1')
dfa.edge('q5', 'q1', label='1')

# Initial state arrow
dfa.attr('node', shape='none')
dfa.node('')
dfa.edge('', 'q0')

dfa.render('/mnt/data/dfa_111_11111')
'/mnt/data/dfa_111_11111.png'
