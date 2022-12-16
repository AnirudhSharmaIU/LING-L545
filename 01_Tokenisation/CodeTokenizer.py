import sys
import fileinput

def tokenizerMethod(strings):
    return strings.replace(" ", "\n").replace(".", "").replace(",", "").replace(":", "").replace("(", "").replace(")", "")


if __name__ == "__main__":
    input_str = ''
    with fileinput.input() as lines:
        for line in lines:
            input_str += line
            
    print(tokenizerMethod(input_str))