from flask import Flask,render_template,jsonify


app = Flask(__name__)

@app.route('/')
def index():
    """
    This function renders the home page of the web application.
    """
    return render_template('home.html')

def create():
    """
    This function creates a new item in the web application.
    """
    pass

if __name__ == '__main__':
    app.run(debug=True)
    
    
    

        
        
        
        
    
    