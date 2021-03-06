from flask import Flask, request, render_template

app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def parse_upload():
    img = request.get()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc', debug=True)
