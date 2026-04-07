def read_data(file):
    curr_best = ["", -1]
    id = ""
    seq_count = 0
    seq_len = 0

    def check():
        nonlocal curr_best
        if seq_len > 0:
            content = seq_count / seq_len * 100
            if content > curr_best[1]:
                curr_best = [id, content]
    for line in file:
        line = line.strip()
        if not line: continue
        if (line[0] == '>'):
            check()
            id = line[1:]
            seq_count = 0
            seq_len = 0
        else:
            seq_len += len(line)
            seq_count += line.count('C') + line.count('G')
    check()
    return curr_best

with open("rosalind_gc.txt", 'r') as data:
    print(*read_data(data), sep = '\n')
    
    

