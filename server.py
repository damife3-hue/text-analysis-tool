from flask import Flask

app = Flask(__name__)

@app.route('/health')
def healthCheck():
    return 'Flask server is up and running!'

@app.route('/analyze-stock')
def analyzeStock():
    return {'data': 'Analysis comming soon'}

if __name__ == '__main__':
    app.run()