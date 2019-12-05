from flask import Flask, escape, url_for, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'post'
    else:
        return "get"


if __name__ == '__main__':
    app.run()
