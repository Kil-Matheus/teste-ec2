from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/somar', methods=['POST'])
def somar():
    try:
        valor1 = float(request.form['valor1'])
        valor2 = float(request.form['valor2'])
        resultado = valor1 + valor2
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'error': 'Erro ao somar valores'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
