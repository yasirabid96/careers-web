from flask import Flask,render_template,jsonify


app = Flask(__name__)

@app.route('/')
def index():
    
   # return jsonify({"name":"yasuir"})
    return render_template('home.html')



    


if __name__ == '__main__':
    app.run(debug=True) 
    
    