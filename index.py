from flask import Flask, render_template
from PIL import Image

#aca se obtiene el objeto del flask
app=Flask(__name__, template_folder='templates')

#para la url del principio
@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
