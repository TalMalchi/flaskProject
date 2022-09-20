from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    #return the html file
    return render_template('./index.html')





if __name__ == '__main__':
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000)
    app.run()
