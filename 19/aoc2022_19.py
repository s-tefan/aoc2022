filename = 'test.txt'
blueprints = {}
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        wordlist = line.strip().split()
        n = int(wordlist[1].strip(':'))
        k = 2
        blueprint = {}
        while k < len(wordlist):
            if wordlist[k] == 'Each':
                robot_type = wordlist[k+1]
                cost = {}
                k += 3
                while k < len(wordlist) and wordlist[k] in {'costs', 'and'}:
                   cost[wordlist[k+2].strip('.')] = wordlist[k+1]
                   k += 3
            else: 
                raise Exception('ajabaja')
            blueprint[robot_type] = cost 

        blueprints[n] = blueprint
print(blueprints)
