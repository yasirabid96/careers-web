from flask import Flask,render_template,jsonify
from database import engine,text,load_jobs_from_db

app = Flask(__name__)

# JOBS=[
    
    
#     {
#         'id':1,
#         'title':'Python Developer',
#         'location':'Nairobi',
#         'salary':50000,
#     },
#     {
#         'id':2,
#         'title':'Data Systems Analyst',
#         'location':'Nairobi',
#         'salary':'RS 50000'
#     }
#     ,
#     {
#         'id':3,
#         'title':'Data Scientist',
#         'location':'Nairobi',
#         'salary':'RS 50000'
#     },
#         {
             
#         'id':4,
#         'title':'Data Engineer',
#         'location':'Nairobi',
#         'salary':'RS 50000' 
#         }
    
# ]



   

@app.route('/')
def index():
    
    jobs=load_jobs_from_db()
    
    return render_template('home.html',jobs=jobs,company='Yasir')

@app.route('/api/jobs')
def get_jobs():
    
    return jsonify(load_jobs_from_db())

if __name__ == '__main__':
    app.run(debug=True,port=5002)
    
    
    
    
    
    
    

        
        
        
        
    
    