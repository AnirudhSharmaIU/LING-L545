import sys
def max_match_algorithm(sent, dictionary):
    start = ''
    remainder = ''
    if sent == '':
        return list()
    for i in range(len(sent), 1, -1):
        start = sent[0:i]
        remainder = sent[i:]
        if start in dictionary:
            return [start] + max_match_algorithm(remainder, dictionary)
    start = sent[0:1]
    remainder = sent[1:]
    return [start] + max_match_algorithm(remainder, dictionary)

line = sys.stdin.readline()
readfile = open(sys.argv[1], "r")
dictionary = readfile.read()
dictionary_list = dictionary.split("\n")
while line != '':
    print(max_match_algorithm(line.replace(' ',''), dictionary_list))
    line = sys.stdin.readline()
dictionary_file.close()