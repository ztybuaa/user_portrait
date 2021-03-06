# -*- coding: utf-8 -*-

import os
from flask import Flask

REDIS_CLUSTER_HOST_FLOW1 = '219.224.135.93'
REDIS_CLUSTER_HOST_FLOW1_LIST = ["219.224.135.91", "219.224.135.92", "219.224.135.93"]
REDIS_CLUSTER_PORT_FLOW1 = '6379'
REDIS_CLUSTER_PORT_FLOW1_LIST = ["6379", "6380"]
REDIS_CLUSTER_HOST_FLOW2 = '219.224.135.94'
REDIS_CLUSTER_PORT_FLOW2 = '6379'
REDIS_HOST = '219.224.135.97'
REDIS_PORT = '6380'

USER_ES_HOST = '219.224.135.97'
ES_CLUSTER_HOST_FLOW1 = ["219.224.135.93", "219.224.135.94"]

ZMQ_VENT_PORT_FLOW1 = '6387'
ZMQ_CTRL_VENT_PORT_FLOW1 = '5585'
ZMQ_VENT_HOST_FLOW1 = '219.224.135.93'
ZMQ_CTRL_HOST_FLOW1 = '219.224.135.93'

ZMQ_VENT_PORT_FLOW2 = '6388'
ZMQ_CTRL_VENT_PORT_FLOW2 = '5586'

ZMQ_VENT_PORT_FLOW3 = '6389'
ZMQ_CTRL_VENT_PORT_FLOW3 = '5587'

# csv file path
'''
BIN_FILE_PATH = '/home/ubuntu8/yuankun/data' # '219.224.135.93:/home/ubuntu8/yuankun'
'''
BIN_FILE_PATH = '/home/ubuntu8/data1309/20130902'

# sensitive words path
SENSITIVE_WORDS_PATH = '/home/ubuntu8/huxiaoqian/user_portrait/user_portrait/cron/flow4/sensitive_words.txt'

# need three ES identification 
USER_PROFILE_ES_HOST = ['219.224.135.96:9208','219.224.135.97:9208','219.224.135.98:9208']
USER_PROFILE_ES_PORT = 9208
USER_PORTRAIT_ES_HOST = ['219.224.135.93:9200', '219.224.135.94:9200']
USER_PORTRAIT_ES_PORT = 9200

# use to identify the db number of redis-97
R_BEGIN_TIME = '2013-09-01'

# use to recommentation
RECOMMENTATION_FILE_PATH = '/home/ubuntu8/huxiaoqian/user_portrait/recommentaion_file'
RECOMMENTATION_TOPK = 10000

# all weibo database
WEIBO_API_HOST = ''
WEIBO_API_PORT = ''

