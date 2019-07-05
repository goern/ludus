FROM python
RUN mkdir Ludus
COPY . /Ludus
RUN cd Ludus
RUN apt update
RUN apt install python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "run.py" ]