from flask import Flask,redirect,render_template,Response
app = Flask(__name__)
app.secret_key = ""

# app.config["TEMPLATES_AUTO_RELOAD"] = True
# in 45 seconds see how much distance the user will cover and we will get rpm

i = 0
@app.route("/")
def home():  
    return render_template("index.html")

@app.route('/time_feed')
def time_feed():
    def generate():
        global i
        i += 1
        return str(i)  
    return Response(generate(), mimetype='text') 
if __name__ == "__main__":
    app.run(debug=True)