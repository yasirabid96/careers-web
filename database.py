import sqlalchemy

print(sqlalchemy.__version__)
from sqlalchemy import create_engine, text

db_string = "mysql+pymysql://o4d117hlppifp60oea8l:pscale_pw_dHNWdFmwMB93ViV5rlaOi6yoIOWXJohGK0Hfgnwz76B@aws.connect.psdb.cloud/yasircareer?charset=utf8mb4"
engine = create_engine(db_string, connect_args={
    "ssl": {
        "ca": "/etc/ssl/cert.pem"
    }
})

with engine.connect() as conn:
    rs = conn.execute(text("SELECT * from jobs"))
    print("Type Result", type(rs))

    results = rs.all()
    print("Type Results All", type(results))

    column_names = rs.keys()  # Get the column names
    print("Column Names:", column_names)

    final_results = [dict(zip(column_names, row)) for row in results] # Convert rows into dictionaries with column names as keys
   
    results_dict=[]
    for row in final_results:
        results_dict.append(dict(row))
   
    # print("Final Results:", type(final_results))
    # print("Final Results:", final_results)
    # dict_result = dict(final_results[0])
    # dict_result_type = type(dict_result)
    # print("Dict Result Type:", dict_result_type)
    # print("Dict Result:", dict_result)
    
    
    print("Results Dict:", type(results_dict))
    print("Results Dict:", results_dict)

