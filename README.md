mac airflow
# 필요패키지 설치
brew services list
brew insatll cask
brew install postgres
brew services start postgresql
pip install psycpog2-binary

# psql 접속하여 계정 및 db 생성
psql postgres
create database airflow_db;
create user airflow_user with password 'airflow_password';
exit

# airflow.cfg 파일 postgres 로 변경
cd Users/jangheesu/airflow
vim airflow.cfg // cfg 파일 내용 변경

# airflow db 접속 및 db 초기화 확인
airflow db init
psql -U airflow_user -d airflow_db
\list
exit

# airflow 계정 생성
airflow users create --username test_admin_user --firstname harry --lastname potter --role Admin --password 1234 --email harry@naver.com
airflow users create --username test_role_user --firstname hermione --lastname granger --role User --password test_password --email hermione@naver.com
psql -U airflow_user -d airflow_db
select * from ab_user;

# airflow 실행
airflow webserver --port 8080
airflow scheduler

# airflow dag list 조회
airflow dags list

# 실행 중인 프로세스 확인 및 종료
lsof -PiTCP -sTCP:LISTEN
lsof -i :8793
kill -9 pid번호

# api 접속테스트
airflow.cfg 파일에서 api 옵션 변경
auth_backend = airflow.api.auth.backend.basic_auth

curl 'http://localhost:8080/api/v1/dags' -H 'content-type: application/json' --user test_admin_user:1234




