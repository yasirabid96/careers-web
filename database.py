import sqlalchemy

print(sqlalchemy.__version__)
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine, text
# get the datbase connection from env
import os
print(os.getenv("DB_CONNECTION"))

db_string =os.getenv("DB_CONNECTION")
engine = create_engine(db_string, connect_args={
    "ssl": {
         "ssl_cert": "/etc/ssl/cert.pem"
    }
})



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
        
    