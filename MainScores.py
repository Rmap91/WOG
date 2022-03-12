from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    with open("Scores.txt", "r") as f:
        Score = f.read()
        print(Score)
    with app.app_context():
        template = render_template('scorehtml.html', Score=Score)
    return template


if __name__ == "__main__":
    app.run(debug=True)
