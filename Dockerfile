FROM python:3-buster
ENV DIR="/browsepy"
COPY ./ /browsepy/
WORKDIR /browsepy/
RUN python setup.py install
RUN python manage-db.py db init
RUN python manage-db.py db migrate
RUN python manage-db.py db upgrade
#RUN python translateCountryCodes.py ${DIR}
EXPOSE 8080
CMD python -m browsepy --debug 0.0.0.0 8080 --directory ${DIR}

