import statistics
from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    response = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['cookie']
        response.set_cookie('testeCookie', dados)
    return response

@app.route('/getcookie')
def getcookie():
    cookieName = request.cookies.get('testeCookie')
    return render_template('getcookie.html', cookieName=cookieName)


if __name__=="__main__":
    app.run(debug=True)