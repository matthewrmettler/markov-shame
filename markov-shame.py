from flask import Flask, render_template, request
from chain import getChainForPolitician
app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    result = getChainForPolitician(request.form['politician'])
    return render_template('results.html', text=result)

if __name__ == '__main__':
    app.run()
