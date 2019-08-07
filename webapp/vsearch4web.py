from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> '302':  # redirect to entry
    return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':  # accept form's i/p, hence POST
    letters = request.form['letters']
    phrase = request.form['phrase']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title='The results',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log)
        # asn alternate to above 4 lines - use sep
        # print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', "Results")
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


# @app.route('/')    # you could also do this instead of redirect from hello(). this will be less number of requests.
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters web')


if __name__ == '__main__':
    app.run(debug=True)
