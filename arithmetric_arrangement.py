def arithmetic_arranger(problems, converter=False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    if len(problems) > 5:
        return 'Error: Too many problems'
    for problem in problems:
        val = problem.split()
        indent = abs(len(val[0]) - len(val[2])) + 1
        dash = max(len(val[0]), len(val[2])) + 2
        if not val[0].isdigit() or not val[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(val[0]) > 4 or len(val[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if val[1] != '+' and val[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if len(val[0]) <= len(val[2]):
            line1 += ' ' + (indent * ' ') + val[0] + (4 * ' ')
            line2 += val[1] + ' ' + val[2] + (4 * ' ')
            line3 += dash * '-' + (4 * ' ')
        else:
            line1 += (2 * ' ') + val[0] + (4 * ' ')
            line2 += val[1] + (indent * ' ') + val[2] + (4 * ' ')
            line3 += dash * '-' + (4 * ' ')
        if converter:
            answer = helper(val)
            ans_indent = dash - len(answer)
            line4 += (ans_indent * ' ') + answer + (4 * ' ')
    if line4 != '':
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    return line1 + '\n' + line2 + '\n' + line3


def helper(problem):
    "It calculates the answer to the problem."
    if problem[1] == '+':
        answer = str(int(problem[0]) + int(problem[2]))
    else:
        answer = str(int(problem[0]) - int(problem[2]))
    return answer

#Note: The function has to be called inside a print() statement in order to work properly.
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
