import utils
from flask import Flask

link = 'candidates.json'

app = Flask(__name__)


@app.route('/')
def page_index():
    response = utils.get_all()
    return f'<pre>{response}</pre>'


@app.route('/candidates/<int:uid>')
def page_candidate(uid):
    response = utils.get_by_pk(uid)
    pic_url = 'http://mypictures.me/' + str(uid)
    return f'''
    <img src='({pic_url})'>
    <pre>{response}</pre>
    '''

@app.route('/skills/<s_id>')
def page_skills(s_id):
    fit_list = utils.get_by_skill(s_id)
    result = ''
    for candidate in fit_list:
        name = candidate['name']
        position = candidate['position']
        skills = candidate['skills']
        result += name + '\n' + position + '\n' + skills + '\n'
        result += '\n'
    return f'<pre>{result}</pre>'


app.run()
