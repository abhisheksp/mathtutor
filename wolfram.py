import requests


def find_roots(question):
    params = {'exp': question}
    url = 'https://www.wolframcloud.com/objects/e82904b9-7632-481b-9b4d-fab27ddd8639'
    res = requests.get(url, params=params)
    return res.text


def solve(latex_equations):
    questions = list(map(lambda x: x[0], latex_equations))
    roots = list(map(find_roots, questions))
    response = {'correct': True, 'reference_solution': roots}
    return response
