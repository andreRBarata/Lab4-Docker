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

@app.route("/multiples/<int:end>")
def multiples(end):
  total = 0
  number = 0

  #Count to 1000
  while (number < end):
    #Increment if it is a multiple of 5 or 3
    if (number % 5 == 0 or number % 3 == 0):
      #Add to total
      total += number

    #Increment number
    number+=1

  return(str(total))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
