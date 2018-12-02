import re

# TODO: copy pasta, fix
def format_response(latex_responses):
    formatted_responses = []
    for string in latex_responses:
        save = []
        string2 = string.split(r'\\')
        for s in string2:
            s1 = s.split(' ')
            s1 = [s2 for s2 in s1 if s2 not in [r"\left.", r"\begin{array}", r"\end{array}", r"\right."]]
            temp = ' '.join(s1)
            temp = temp.replace(' ', '')
            if temp[:3] == "{l}":
                temp = temp[3:]
            temp1 = temp.replace("\\\\", "")
            save.append(temp1)
        for item in save:
            temp1 = item.replace("\\\\", "|")
            match = re.search(r"\\", temp1)
            if match:
                temp1 = temp1[:match.span()[0]] + temp1[match.span()[1]:]
                tmp = temp1
                save.append(tmp)
        formatted_responses.append(save)
    return formatted_responses