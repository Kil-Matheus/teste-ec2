from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def somar():
    try:
        numero1 = float(request.args.get('numero1', 0))  # Use 0 como valor padrão se não for fornecido
        numero2 = float(request.args.get('numero2', 0))  # Use 0 como valor padrão se não for fornecido
        resultado = numero1 + numero2

        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': 'Erro na operação de soma'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
