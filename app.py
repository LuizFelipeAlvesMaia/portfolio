from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/projeto/<projeto_id>')
def projeto(projeto_id):
    return render_template('projeto.html', projeto_id=projeto_id)

@app.route('/case/<case_id>')
def case(case_id):
    return render_template('case.html', case_id=case_id)

if __name__ == '__main__':
    app.run(debug=True)
