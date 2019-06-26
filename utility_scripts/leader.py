#!/usr/bin/env python
import random
import faust
import ssl

ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile='../resources/data-hub-kafka-ca.crt')

app = faust.App(
    'leader-example',
    broker='kafka://kafka.datahub.redhat.com:443',
    broker_credentials=ssl_context,
    value_serializer='raw',
)


@app.timer(2.0, on_leader=True)
async def publish_greetings():
    print('PUBLISHING ON LEADER!')
    await say.send(value=str(random.random()))


@app.agent()
async def say(greetings):
    async for greeting in greetings:
        print(greeting)
