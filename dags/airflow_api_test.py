from datetime import datetime
from email.policy import default
import json

from re import sub
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator

args = {'owner': 'jovyan', 
        'start_date': days_ago(n=1),
        'description': 'My first tutorial bash DAG'
        }

dag = DAG(dag_id='api_test',
          default_args=args,
          schedule_interval='@daily')

# http://localhost:8080/api/v1/dags
def get_api(base_url, user, pwd, sub_url, **kwargs):
    
    print("===========base_url : ", base_url)
    print("===========sub_url : ", sub_url)
    print("-----------base+sub : ", base_url+sub_url)
    print("===========user : ", user)
    print("===========pwd : ", pwd)
          
    import requests
    rq = requests.session()
    rq.auth = (user, pwd)
    call_url = base_url + sub_url
    rs = rq.get(call_url)
    data = json.loads(rs.text)
    print("===============dat : ", data)
    # print(data["dags"][0]["dag_id"])
    count = 0
    for key in data:
        print("******** key : ", key)
        count+=1
    
    return rs.json()


t1 = PythonOperator(task_id = 'task_1',
                    provide_context=True,
                    python_callable=get_api,
                    op_kwargs={'base_url':'http://localhost:8080', 'user':'test_admin_user', 'pwd':'1234', 'sub_url':'/api/v1/dags'},
                    dag=dag)