from xml.etree import ElementTree

import requests


def get_roots(polynomial_equation):
    roots = []
    params = {'appid': 'QU7434-QE6KPPYTAX', 'input': polynomial_equation}
    url = "http://api.wolframalpha.com/v2/query"
    res = requests.get(url, params)
    tree = ElementTree.fromstring(res.content)
    for child in tree:
        if child.attrib['title'] == "Solutions" or child.attrib['title'] == "Solution":
            for subPod in child:
                for text in subPod:
                    if text.text is not None:
                        roots.append(text.text.replace(' ', ''))
    return roots


def solve(latex_string):
    return latex_string
