##################################################


# django 설정

장고 설치 후 아래 명령어 입력시 장고 프로젝트 폴더 자동생성
django-admin startproject 폴더명

# Django 서버 실행

생성된 폴더 하단 manage.py 파일을 아래 명령어로 실행
python manage.py runserver
다른 포트(8080) 사용시
python manage.py runserver 8080


# Django App - 파이썬 패키지 생성

? Django App 패키지는 그 안에 자신의 모델(model),
뷰(view), 템플릿(template), URL 매핑 등을 독자적으로 가지고 있으며,
일반적으로 하나의 Django 프로젝트는
하나 이상의 Django App으로 구성되어 있다.
규모가 큰 Django 프로젝트는
보통 여러 개의 Django App들을 모듈화하여 구성


- 하단 메세지 실행
./manage.py startapp 폴더명
위 명령을 실행하면 ~ 이라는 서브폴더가 생성되고
그 안에 Django App에 필요한 기본 파일들이 생성됨






##################################################