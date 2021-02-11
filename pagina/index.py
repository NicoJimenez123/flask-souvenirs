from flask import Flask, render_template, request, url_for, redirect, flash
import json

app = Flask(__name__)

@app.route('/')
def index():
    f = open('./imagenes.json', encoding='utf8') 
    listaImagenes = json.load(f)
    return render_template("index.html", lista=listaImagenes['lista'])
    
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search', methods=["POST"])
def search():
    if request.method == 'POST':
        busqueda = request.form['input']
        f = open('./imagenes.json', encoding='utf8')
        listaImagenes = json.load(f)
        imgBuscada = []
        for img in listaImagenes["lista"]:
            if busqueda.lower() in img['tags']:
                imgBuscada.append(img)
        

        return render_template('index.html', lista=imgBuscada)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')