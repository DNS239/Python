import pandas as pd
from flask import Flask, jsonify



app = Flask(__name__)


@app.route('/')
def online():
    return 'API Esta ON'



@app.route('/totalvalor')
def totalvalor():
    tabela = pd.read_csv('carros.csv')
    total_valor = tabela['VALOR'].sum()
    resposta = {'total_valor': round(total_valor, 2)}
    return jsonify(resposta)




app.run(host='0.0.0.0')











#              tabela com HTML                #


"""import pandas as pd
from flask import Flask

# Inicializa o objeto Flask
app = Flask(__name__)

# Define a rota padrão '/'
@app.route('/')
def online():
    return 'API Esta ON'

# Função para ler o arquivo CSV
def ler_csv():
    tabela = pd.read_csv('carros.csv')
    return tabela

# Rota para acessar os dados do CSV
@app.route('/dados')
def dados():
# Chama a função para ler o arquivo CSV
    tabela = ler_csv()
# Retorna os dados do CSV
    return tabela.to_html()

if __name__ == '__main__':
    app.run(host='0.0.0.0')"""



"""para acessar e ver uma tabela em HTML = http://127.0.0.1:5000/dados"""