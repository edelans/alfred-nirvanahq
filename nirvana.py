#!/usr/bin/env python3
# encoding: utf-8

import sys
import requests
import uuid
import time
import json


# Variables
requestid = str(uuid.uuid4())
clienttime1 = str(int(time.time()))
clienttime0 = str(int(time.time())-9)


def main(args):
    
    # configure the task to post
    auth_token = args[-1]
    api_endpoint = "https://focus.nirvanahq.com/api/?api=json&requestid=" + requestid + "&clienttime=" + clienttime1 + "&authtoken=" + auth_token + "&appid=n2desktop&appversion=1637094776"
    task = args[1]  # 1st arg is script name, last one is the auth_token, middle one is {query}
    if "--" in task:
        task_title, note = task.split("--")
    else:
        task_title = task
        note = ""
    print(task_title)  # for printing it in the notification post
    tags = ","

    # data to be sent to api
    headers = {
        'Content-type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://focus.nirvanahq.com',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = [{
        "method": "task.save",
        "id": str(uuid.uuid4()),
        "type": "0",
        "_type": clienttime0,
        "parentid": "",
        "_parentid": clienttime0,
        "waitingfor": "",
        "_waitingfor": clienttime0,
        "state": 0,
        "_state": clienttime1,
        "completed": "0",
        "_completed": clienttime0,
        "cancelled": "0",
        "_cancelled": clienttime0,
        "seq": 0,
        "_seq": clienttime1,
        "seqt": 0,
        "_seqt": clienttime0,
        "seqp": "0",
        "_seqp": clienttime0,
        "name": task_title,
        "_name": clienttime1,
        "tags": tags,
        "_tags": clienttime1,
        "note": note,
        "_note": clienttime0,
        "ps": "0",
        "_ps": clienttime0,
        "etime": "0",
        "_etime": clienttime0,
        "energy": "0",
        "_energy": clienttime0,
        "startdate": "",
        "_startdate": clienttime0,
        "duedate": "",
        "_duedate": clienttime0,
        "recurring": "",
        "_recurring": clienttime0
        }]
        # seq is the index in the list -> seq of 0 will appear at the top of the list
        # set at time to seqt to star the task
        # print data

    # sending post request and saving response as response object
    r = requests.post(url=api_endpoint, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        print("is added to inbox !")


if __name__ == u"__main__":
     main(sys.argv)