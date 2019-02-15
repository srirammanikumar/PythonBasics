from flask import Flask, render_template, request, redirect
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
        print(req, res, file=log)


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log', 'r') as log:
        contents = log.read() # .read() method will read the entire file
    return contents



# @app.route('/')    # you coulld also do this instead of redirect from hello(). this will be less number of requests.
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters web')


if __name__ == '__main__':
    app.run(debug=True)
