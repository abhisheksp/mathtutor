import re

import requests
import uuid


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


def to_image(formula, file_name=None):
    file_name = file_name or 'img/{}.png'.format(str(uuid.uuid4()))
    r = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \huge %s' % formula)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    return file_name


def format_integrals(latex_responses):
    result = []
    for response in latex_responses:
        if '\\int' in response:
            response = response \
                .replace('d x', '\\, d x') \
                .replace('dx', '\\, dx')
        result.append(response)
    return result
