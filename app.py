from flask import Flask,render_template,jsonify


app = Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Python Developer',
        'location':'Nairobi',
        'salary':50000,
    },
    {
        'id':2,
        'title':'Data Systems Analyst',
        'location':'Nairobi',
        'salary':'RS 50000'
    }
    ,
    {
        'id':3,
        'title':'Data Scientist',
        'location':'Nairobi',
        'salary':'RS 50000'
    },
        {
             
        'id':4,
        'title':'Data Engineer',
        'location':'Nairobi',
        'salary':'RS 50000' 
        }
    
]
@app.route('/')
def index():
    """
    This function renders the home page of the web application.
    """
    return render_template('home.html',jobs=JOBS,company='Yasir')

@app.route('/api/jobs')
def get_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True,port=5002)
    
    
    
    
    
    
    

        
        
        
        
    
    