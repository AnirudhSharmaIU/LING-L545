import fileinput
import sys
    
def segmentorMethod(file_data):
    return file_data.replace(". ", ".\n")

if __name__ == "__main__":
    input_str = ''
    with fileinput.input() as lines:
        for line in lines:
            input_str += line
            
    print(segmentorMethod(input_str))