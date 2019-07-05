FROM python
RUN git clone https://github.com/akhil-rane/Ludus.git
RUN pip3 install -r Ludus/requirements.txt
EXPOSE 8080
RUN chmod 777 Ludus
WORKDIR Ludus
RUN mkdir resources
RUN echo -e $ludus_secret > resources/data-hub-kafka-ca.crt
CMD ["python3" ,"run.py"]
#CMD ["faust" ,"-A", "awarder" ,"worker"]