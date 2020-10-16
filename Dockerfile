FROM python:3-buster
ENV DIR="/UC3-Portal"
RUN git clone https://github.com/process-project/UC3-Portal.git
WORKDIR /UC3-Portal/
RUN python setup.py install
RUN python manage-db.py db init
RUN python manage-db.py db migrate
RUN python manage-db.py db upgrade
EXPOSE 8080
CMD python -m browsepy --debug 0.0.0.0 8080 --directory ${DIR}

