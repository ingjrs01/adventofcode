def load(filename):
    lines = [l.strip() for l in open(filename,'r').readlines()]
    pattern = lines [0] # first line is pattern

    rules = {}
    for line in lines[2:]:
        a,b = line.split(" -> ")
        rules[a] = b

    return pattern,rules


def step(input,rules):
    output = ""
    positions = {}
    inc = 1
    for i in range(len(input)-1):
        word = input[i:i+2]

        if (word in rules):
            positions[i+inc]=rules[word]
            inc += 1

    t = len(input) + len(positions)
    pos_input = 0
    for i in range(t):
        if (i in positions.keys()):
            output += positions[i]
        else:
            output += input[pos_input]
            pos_input += 1

    return output

def count_letters(input,data):
    counts = {}
    for i in range(len(input)):
        if (input[i] not in counts.keys()):
            counts[input[i]] = data.count(input[i])
    for c in rules.values():
        if c not in counts.keys():
            counts[c] = data.count(c)

    print(counts)
    print(max(counts.values()) - min(counts.values()))



data, rules = load('real')
original = data

print(data)
print(rules)
for i in range(1,41):
    print(f"After step {i}: ")
    data = step(data,rules)
count_letters(original,data)
