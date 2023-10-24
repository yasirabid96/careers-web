from flask import Flask,render_template,jsonify
from database import engine, load_jobs_from_db,text,load_job_by_id

app = Flask(__name__)
jobs=load_jobs_from_db()
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
    
   
    
    return render_template('home.html',jobs=jobs,company='Yasir')

@app.route('/api/jobs')
def get_jobs():
    
    return jsonify(load_jobs_from_db())

@app.route('/job/<int:job_id>')
def get_job(job_id):
    # The method below in sorting the jobs by id using python but we should use sql where clause to do this
    # job=[job for job in jobs if job['id']==job_id]
    # # job=None
    # # for j in jobs:
    # #     if j['id']==job_id:
    # #         job=j
    job=load_job_by_id(job_id)
    if not job:
        return {'error':'Job not found'},404
  
    return render_template('jobpage.html',job=job,company='Yasir')
   


    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    
   

    
    

        
        
        
        
    
    