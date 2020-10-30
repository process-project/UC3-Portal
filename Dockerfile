FROM python:3-buster
ENV DIR="/mnt"
RUN mkdir /home/user
RUN groupadd -g 2222 user
RUN useradd -s /bin/sh -g 2222 -u 3938873  user
RUN chown -R user:user /home/user
RUN git clone https://github.com/process-project/UC3-Portal.git
WORKDIR /UC3-Portal/
RUN python setup.py install
RUN python manage-db.py db init
RUN python manage-db.py db migrate
RUN python manage-db.py db upgrade
RUN chown -R user:user /UC3-Portal
USER user
EXPOSE 8080
CMD python -m browsepy --debug 0.0.0.0 8080 --directory ${DIR}

