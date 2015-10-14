from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:port>')
def show_port_protocol(port):
    return 'Post %d' % port

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
