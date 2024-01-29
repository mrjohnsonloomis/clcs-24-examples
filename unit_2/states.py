with open('states.txt') as file:
    states = [x.strip() for x in file.readlines()]

a_states = []
for state in states:
    if state.endswith('a'):
        a_states.append(state)
print(len(a_states))

new_file = open('a_states.txt', 'w')

for state in a_states:
    new_file.write(state + '\n')

new_file.close()