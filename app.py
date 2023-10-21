from flask import Flask,render_template,jsonify
from database import engine,text

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



   
def load_jobs_from_db():
    with engine.connect() as conn:
        rs = conn.execute(text("SELECT * from jobs"))
        #print("Type Result", type(rs))

        results = rs.all()
        #print("Type Results All", type(results))

        column_names = rs.keys()  # Get the column names
        #print("Column Names:", column_names) 

        final_results = [dict(zip(column_names, row)) for row in results] # Convert rows into dictionaries with column names as keys
        print(final_results)
        return final_results
        # results_dict=[]
        # for row in fina l_results:
        #     results_dict.append(dict(row))
    
        # print("Final Results:", type(final_results))
        # print("Final Results:", final_results)
        # dict_result = dict(final_results[0])
        # dict_result_type = type(dict_result)
        # print("Dict Result Type:", dict_result_type)
        # print("Dict Result:", dict_result)
        
        
        #print("Results Dict:", type(results_dict))
        #print("Results Dict:", results_dict)
        
    
@app.route('/')
def index():
    
    jobs=load_jobs_from_db()
    
    return render_template('home.html',jobs=jobs,company='Yasir')

@app.route('/api/jobs')
def get_jobs():
    
    return jsonify(load_jobs_from_db())

if __name__ == '__main__':
    app.run(debug=True,port=5002)
    
    
    
    
    
    
    

        
        
        
        
    
    