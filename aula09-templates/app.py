from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    x = 5
    y = 10
    usuarios = {        
        'George P. Chausse':'713-718-2082',
        'Livia Ribeiro Barros':'(81) 2753-2153',
        'Rebeca Costa Oliveira':'(81) 8183-5958',
        'Júlio Barbosa Sousa':'(31) 2110-9877',
        'Mariana Alves Costa':'(11) 9306-2119'
    }
    return render_template('template.html', x=x, y=y, usuarios=usuarios)

if __name__=="__main__":
    app.run(debug=True)