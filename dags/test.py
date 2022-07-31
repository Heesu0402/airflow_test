from datetime import datetime
from email.policy import default
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
# test
# default_args = {
#     'start_date': datetime(2022, 7, 24),
#     'owner': 'airflow11'
# }


args = {'owner': 'jovyan',
        'start_date': days_ago(n=1),
        'description': 'My first tutorial bash DAG'
        }

dag  = DAG(dag_id='my_first_dag',
           default_args=args,
           schedule_interval='@daily')

t1 = BashOperator(task_id='print_date',
                #   bash_command='date',
                  bash_command='echo "hello world"',
                  dag=dag)

t2 = BashOperator(task_id='sleep',
                  bash_command='sleep 3',
                  dag=dag)

t3 = BashOperator(task_id='print_whoami',
                  bash_command='whoami',
                  dag=dag)

t1 >> t2 >> t3
