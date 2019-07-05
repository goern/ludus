FROM python
RUN git clone https://github.com/akhil-rane/Ludus.git
RUN cd Ludus
RUN pip3 install -r Ludus/requirements.txt
EXPOSE 8080
WORKDIR /Ludus
#CMD [ "python3", "ru.py" ]
ENTRYPOINT ["faust" ,"-A", "awarder" ,"worker"]