from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde el puerto 3003!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 3003))  # Heroku pondrá el puerto en PORT
    app.run(host='0.0.0.0', port=port)
