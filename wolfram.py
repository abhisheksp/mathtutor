import json

import requests

import image
import latex


def find_roots(question):
    params = {'exp': question}
    url = 'https://www.wolframcloud.com/objects/e82904b9-7632-481b-9b4d-fab27ddd8639'
    res = requests.get(url, params=params)
    return res.text


def full_results(latex_exp):
    params = {'exp': latex_exp}
    full_form_url = 'https://www.wolframcloud.com/objects/b6228cee-58da-43d0-9c98-077a390614b5'
    res = requests.get(full_form_url, params=params)
    input_exp = 'solve {}'.format(res.text)
    full_results_url = 'http://api.wolframalpha.com/v2/query?appid=QU7434-QE6KPPYTAX&podstate=Result__Step-by-step%20solution&output=json&input=' + input_exp
    res = requests.get(full_results_url)
    data = json.loads(res.text)
    for pod in data['queryresult']['pods']:
        if pod['id'] == 'Result':
            for subpod in pod['subpods']:
                if subpod['title'] == 'Possible intermediate steps':
                    solution_string = subpod['img']['src']
    return solution_string


def analyze(question, steps):
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
        result = full_results(question)
        response = {'correct': True, 'reference_solution': result}
    else:
        response = {'correct': False, 'error': step_num}
    return response


def solve(latex_equations):
    questions = list(map(lambda x: x[0], latex_equations))
    responses = []
    for question, steps in zip(questions, latex_equations):
        analysis = analyze(question, steps)
        student_solution = steps
        question_img = expression_to_img(question)
        student_solution_img = expressions_to_img(student_solution)
        response = {'question': question_img, 'analysis': analysis, 'student_solution': student_solution_img}
        responses.append(response)
    return responses


def expressions_to_img(expressions):
    return list(map(lambda x: image.upload(latex.to_image(x)), expressions))


def expression_to_img(expression):
    return image.upload(latex.to_image(expression))
