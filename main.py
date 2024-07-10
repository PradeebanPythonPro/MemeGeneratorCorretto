# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # ottenere l'immagine selezionata
        selected_image = request.form.get('image-selector')

        # Consegna #2. Ricevere il testo
        textTop = request.form.get("textTop")
        textBottom = request.form.get("textBottom")

        # Consegna #3. Ricezione del posizionamento del testo
        textTop_y = request.form.get("textTop_y")
        textBottom_y = request.form.get("textBottom_y")

        # Consegna #3. Ricezione del colore del testo
        selected_color = request.form.get("color-selector")

        return render_template('index.html', 
                               # Visualizzazione dell'immagine selezionata
                               selected_image=selected_image, 

                               # Consegna #2. Visualizzazione del testo
                               textTop=textTop,
                               textBottom=textBottom,

                               # Consegna #3. Visualizzazione del colore 
                               selected_color=selected_color,
                               
                               # Consegna #3. Visualizzazione del posizionamento del testo
                               textTop_y=textTop_y,
                               textBottom_y=textBottom_y

                               )
    else:
        # Visualizzazione predefinita della prima immagine
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
