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
    return render_template('results.html',
                           the_title='The results',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


# @app.route('/')    # you coulld also do this insteadd of redirect from hello(). this will be less number of requests.
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to serch4letters web')


if __name__ == '__main__':
    app.run(debug=True)
