from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': '',
    'database': 'sgcta_db'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abastecer', methods=['POST'])
def abastecer():
    conn = None
    cursor = None
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Obter dados do formulário
        dados = request.form
        numero_requisicao = dados.get('numeroRequisicao')

        # Verificar se o número de requisição já existe
        cursor.execute("SELECT COUNT(*) FROM abastecimentos WHERE numero_requisicao = %s", (numero_requisicao,))
        (count,) = cursor.fetchone()
        if count > 0:
            return jsonify({'message': 'Número de requisição já está em uso'}), 400


        # Obter dados do formulário
        dados = request.form
        numero_requisicao = dados.get('numeroRequisicao')
        nome_motorista = dados.get('nomeMotorista')
        modelo_carro = dados.get('modeloCarro')
        placa_carro = dados.get('placaCarro')
        combustivel = dados.get('combustivel')
        quantidade_abastecida = dados.get('quantidadeAbastecida')
        valor_total = dados.get('valorTotal')

        # Inserir dados no banco de dados
        query = """
        INSERT INTO abastecimentos (numero_requisicao, nome_motorista, modelo_carro, placa_carro, combustivel, quantidade_abastecida, valor_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (numero_requisicao, nome_motorista, modelo_carro, placa_carro, combustivel, quantidade_abastecida, valor_total))
        conn.commit()

        return jsonify({'message': 'Registro adicionado com sucesso'})
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
        return jsonify({'message': 'Erro ao processar a requisição'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/get-requisitions', methods=['GET'])
def get_requisitions():
    conn = None
    cursor = None
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Obter todas as requisições de abastecimento
        cursor.execute("SELECT * FROM abastecimentos")
        requisitions = cursor.fetchall()

        # Convertendo para um formato que possa ser enviado como JSON
        requisitions_list = []
        for requisition in requisitions:
            requisitions_list.append({
                "numero_requisicao": requisition[1],
                "nome_motorista": requisition[2],
                "modelo_carro": requisition[3],
                "placa_carro": requisition[4],
                "combustivel": requisition[5],
                "quantidade_abastecida": requisition[6],
                "valor_total": requisition[7]
            })

        return jsonify(requisitions_list)
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
        return jsonify({'message': 'Erro ao processar a requisição'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
