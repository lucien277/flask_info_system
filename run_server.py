from app.router import app

app.secret_key = 'this is secret key'

app.run(host='127.0.0.1', port=8080, debug=True)