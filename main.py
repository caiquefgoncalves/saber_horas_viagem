from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculo_viagem', methods=['POST'])
def calculo_viagem():
    try:
        distancia = float(request.form['distancia'])
        velocidade_media = float(request.form['velocidade_media'])

        calculo_tempo = round(distancia / velocidade_media, 2)
        tempo_s = int(calculo_tempo * 3600)
        horas = int(tempo_s / 3600)
        tempo_s = int(tempo_s % 3600)
        minutos = int(tempo_s / 60)

        return render_template('index.html', horas=horas, minutos=minutos)
    except Exception as e:
        distancia = f'Ocorreu um erro inesperado {e}'
        velocidade_media = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html', horas=horas, minutos=minutos)

if __name__ == '__main__':
    app.run(debug=True)
