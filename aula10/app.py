import statistics
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def notas():
    return render_template('index.html')

@app.route('/calculo', methods=['GET','POST'])
def calculo():
    notas = request.form.to_dict()
    nota_media = statistics.mean([int(v) for v in notas.values()])
    return render_template('calculo.html', notas=notas, media=nota_media)

if __name__=="__main__":
    app.run(debug=True)