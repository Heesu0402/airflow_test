from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

# airflow argument test 용
# airflow 에서는 kwargs 를 넘겨받으면 기본적인 dag 정보를 가지고 있는 것 같다.
def my_func(**kwargs):
    print('=' * 100)
    count = 0
    for key, value in kwargs.items():
        print("@@@ kwargs count : ", count, "------ {0} || {1} -------".format(key, value))
        count = count + 1
    print('=' * 100)
    return "hello " + kwargs['name']


dag = DAG(
    dag_id='print_test',
    schedule_interval='0 12 * * *',
    start_date=datetime(2021, 8, 4),
    catchup=False
)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

print_operator = PythonOperator(
    task_id='python_task',
    python_callable=my_func,
    op_kwargs={"name": "Patrick", "City": "Vienna", "ID": "Qwalk_123"},
    dag=dag
)

dummy_operator >> print_operator