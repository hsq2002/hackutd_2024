from flask import Flask

app = Flask(__chatbot__)

@app.route("/")
def home():
    return "Hello, flask"

if __name__ == "__main__":
    app.run(debug=True)
