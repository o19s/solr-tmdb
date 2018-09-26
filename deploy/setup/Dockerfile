FROM python:3

RUN python3 --version

RUN pip3 install requests
RUN pip3 install pysolr
RUN pip3 install parse
RUN pip3 install jinja2

# Copy files to container
COPY *.py /train/
COPY deploy/setup /train

RUN wget http://es-learn-to-rank.labs.o19s.com/tmdb.json -O /train/tmdb.json

#RUN chown -R elasticsearch:elasticsearch /train

RUN ls /train
WORKDIR /train

#RUN ./prepare.sh

CMD /train/setup.sh
