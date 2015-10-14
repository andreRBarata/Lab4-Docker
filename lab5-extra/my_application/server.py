from flask import Flask
app = Flask(__name__)

@app.route("/paledrome/<word>")
def paledrome(word):
    return (str(word[::-1] == word))

@app.route("/fibonacci")
def fibonacci():
    total = 0

    old = 1
    new = 1

    while (old < 4000000 ):
        next = old + new

        if (next % 2 == 0):
            total += next

        old = new
        new = next

    return (str(total))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
