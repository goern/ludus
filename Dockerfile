FROM python
RUN git clone https://github.com/akhil-rane/Ludus.git
RUN pip3 install -r Ludus/requirements.txt
WORKDIR Ludus
#CMD ["faust" ,"-A", "awarder" ,"worker"]