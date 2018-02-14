#!/usr/bin/python
# -*- coding: utf-8 -*-

#�Q�l�T�C�g
#https://qiita.com/egplnt/items/e9af5d5abeab08f5a455

import logging
import os
import os.path
import sys
import codecs
import time
import paho.mqtt.client as mqtt
import json
import threading
import random

broker = ""
i = 0

#�F�ؕ���
username = "use-token-auth"

#�g�DID
organization = "hn7pp2"     # 6���́u�g�DID�v���w�肵�܂�

#�f�o�C�X�^�C�v
deviceType = "temperature" # �u�f�o�C�X�E�^�C�v�v�Ƃ��ēo�^�����l���w�肵�܂�

#�f�o�C�XID
deviceSerial = "temperature" # �u�f�o�C�XID�v�Ƃ��ēo�^�����l���w�肵�܂�

#�g�[�N���p�X���[�h
password = "i?1t2KZ&&L-Dyls1Xc" # �p����18���́u�F�؃g�[�N���v���w�肵�܂�

#�g�s�b�N
topic = "iot-2/evt/update/fmt/json"

#�N���C�A���g�h�c
clientID = "d:" + organization + ":" + deviceType + ":" + deviceSerial

#�u���b�J�[
broker = organization + ".messaging.internetofthings.ibmcloud.com"

#�u���[�J�[�ւ̐ڑ����ݒ肷��B
mqttc = mqtt.Client(clientID)

if username is not "":
    #�ڑ���̃��[�U�ƃp�X���[�h��ݒ肷��B
    mqttc.username_pw_set(username, password=password)

    try:
        #�ڑ�����B
        mqttc.connect(host=broker, port=1883, keepalive=60)
    except Exception as e:
        print "Exception at connect"
        print e

#�l�b�g���[�N���[�v���J�n����B
mqttc.loop_start()

#mqttc.loop()�����I�Ɏ��s���邱�Ƃɂ���āA�ڑ���Ƃ̐ڑ���ێ�����B
while mqttc.loop() == 0:

    #���M���鉷�x����ю��x���Z�o����B
    temp = random.randrange(-10,40)
    humidity = random.randrange(20,99)
    print "temp = " + str(temp) + ", humidity = " + str(humidity)
    msg = " {\"d\": {\"temp\": " + str(temp) +",\"humidity\": " + str(humidity) + "} }";

    try:
        #���M���鉷�x����ю��x���Z���T�[�ɑ��M����B
        mqttc.publish(topic, payload=msg, qos=0, retain=True)
        print "message published"
        # print raw_input("[Enter] to send another request")
    except Exception as e:
        print "Exception at publish"
        print e

    time.sleep(10)
    #���[�v�񐔂��P�O��𒴂���ƁA���[�v�𔲂���B
    if i > 10:
      break

    i = i +1
    pass
