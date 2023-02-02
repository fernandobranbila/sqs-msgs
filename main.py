#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import boto3


def send_messages():
    messages = []
    print("Connecting to AWS: ")
    sqs_client = boto3.client('sqs')

    for message in messages:
        print("Sending message: ", message)
        sent_message = sqs_client.send_message(
            QueueUrl="SQS URL",
            MessageBody=json.dumps(message)
        )
        print(sent_message)


if __name__ == '__main__':
    send_messages()
