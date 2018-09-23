FROM python:3.6.0 as backend

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install  -i https://mirrors.aliyun.com/pypi/simple --upgrade pip  pipenv ; pipenv install --pypi-mirror https://mirrors.aliyun.com/pypi/simple


COPY . /usr/src/app
COPY contrib/pyinstaller_conf/*.spec /usr/src/app/

RUN pipenv run pyinstaller --upx-dir=/usr/src/app/contrib/deploy --onefile csp_controller.spec
RUN pipenv run pyinstaller --upx-dir=/usr/src/app/contrib/deploy --onefile csp_worker.spec
RUN pipenv run pyinstaller --upx-dir=/usr/src/app/contrib/deploy --onefile servicebroker_adapter.spec
RUN pipenv run pyinstaller --upx-dir=/usr/src/app/contrib/deploy --onefile app_broker.spec
