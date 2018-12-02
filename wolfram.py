import requests


def find_roots(question):
    params = {'exp': question}
    url = 'https://www.wolframcloud.com/objects/e82904b9-7632-481b-9b4d-fab27ddd8639'
    res = requests.get(url, params=params)
    return res.text


def analyze(zip_step):
    question, steps = zip_step
    url = 'https://www.wolframcloud.com/objects/b269a111-9f38-42b3-8b11-bc01b2564be4'
    step_num = None
    for i, step in enumerate(steps):
        params = {'exp1': question, 'exp2': step}
        res = requests.get(url, params=params)
        is_correct = res.text == 'True'
        if not is_correct:
            step_num = i
            print('{} != {}'.format(question, step))
            break
    if step_num is None:
        response = {'correct': True}
    else:
        response = {'correct': False, 'error': step_num}
    return response


def solve(latex_equations):
    questions = list(map(lambda x: x[0], latex_equations))
    # roots = list(map(find_roots, questions))
    analysis_responses = list(map(analyze, zip(questions, latex_equations)))
    response = {'correct': True, 'reference_solution': '', 'analysis': analysis_responses}
    return response
