You are given a string S  and width w.
Your task is to wrap the string into a paragraph of width W.
Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
String string: a long string
int max_width: the width to wrap to
Returns
string: a single string with newline characters ('\n') where the breaks should be





import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result = string[i:i+max_width]
        if len(result) == max_width:
            print(result)
        else:
            return(result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
