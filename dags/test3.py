from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import time
from pprint import pprint

args = {'owner': 'testJang',
        'start_date': days_ago(n=1)}

dag = DAG(dag_id='my_python_dag',
          default_args=args,
          schedule_interval='@daily')

def print_fruit(fruit_name, **kwargs):
    print('=' * 100)
    print('fruit_name111:', fruit_name)
    print('=' * 100)
    print(kwargs)
    print('=' * 100)
    for key, value in kwargs.items():
        print("------ {0} || {1} -------".format(key, value))
    print('=' * 100)
    return 'ptrin complete ~ !!'

def sleep_seconds(seconds, **kwargs):
    print('=' * 100)
    print('seconds:', str(seconds))
    print('=' * 100)
    print(kwargs)
    print('=' * 100)
    time.sleep(seconds)
    return 'sleep well ~ !!'
    
t1 = PythonOperator(task_id = 'task_1',
                    provide_context=True,
                    python_callable=print_fruit,
                    op_kwargs={'fruit_name': 'apple'},
                    dag=dag)
t2 = PythonOperator(task_id = 'task_2',
                    provide_context=True,
                    python_callable=print_fruit,
                    op_kwargs={'fruit_name': 'banana'},
                    dag=dag)
t3 = PythonOperator(task_id = 'task_3',
                    provide_context=True,
                    python_callable=sleep_seconds,
                    op_kwargs={'seconds': 10},
                    dag=dag)
t4 = PythonOperator(task_id = 'task_4',
                    provide_context=True,
                    python_callable=print_fruit,
                    op_kwargs={'fruit_name': 'cherry'},
                    dag=dag)

t1 >> [t2, t3]
[t2, t3] >> t4