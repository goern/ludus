FROM python
RUN git clone $github_url
RUN pip3 install -r ludus/requirements.txt
EXPOSE 5000
RUN chmod 777 ludus
WORKDIR ludus
RUN mkdir resources
RUN echo -e $ludus_secret > resources/data-hub-kafka-ca.crt
CMD ["faust" ,"-A", "awarder" ,"worker"]