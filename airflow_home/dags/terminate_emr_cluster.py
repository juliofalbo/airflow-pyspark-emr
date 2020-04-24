from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from aws_utils.emr_deployment import terminate_stale_clusters

dag = DAG(dag_id='terminate_emr_clusters', description='Simple tutorial DAG',
          schedule_interval='@hourly',
          start_date=datetime(2017, 3, 20), catchup=False)

terminate_clusters = PythonOperator(task_id='terminate_emr_clusters',
                                    python_callable=terminate_stale_clusters,
                                    dag=dag
                                    )
