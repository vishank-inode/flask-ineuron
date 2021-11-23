from flask import Flask

app = Flask(__name__)

# create a route for the root of the site
@app.route('/',methods=['GET','POST'])
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
