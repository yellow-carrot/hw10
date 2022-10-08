import json

link = 'candidates.json'


def load_candidates(link):
    with open(link, encoding='utf-8') as file:
        data = file.read()
        content = json.loads(data)
    return content


def get_all():
    candidates_list = load_candidates(link)
    result = ''
    for candidate in candidates_list:
        name = candidate['name']
        position = candidate['position']
        skills = candidate['skills']
        result += name + '\n' + position + '\n' + skills + '\n'
        result += '\n'
    return result


def get_by_pk(pk):
    candidates_list = load_candidates(link)
    for candidate in candidates_list:
        if candidate['pk'] == pk:
            result = ''
            name = candidate['name']
            position = candidate['position']
            skills = candidate['skills']
            result += name + '\n' + position + '\n' + skills
            return result


def get_by_skill(skill_name):
    fit_candidates = []
    candidates_list = load_candidates(link)
    for candidate in candidates_list:
        for skill in candidate['skills'].split(', '):
            if skill == skill_name:
                fit_candidates.append(candidate)
    return fit_candidates
