from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    # Aqui você pode adicionar código para processar a mensagem, como enviar um email
    return f'Mensagem recebida de {nome} ({email}): {mensagem}'

if __name__ == '__main__':
    app.run(debug=True)
