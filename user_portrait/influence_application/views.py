#-*- coding: UTF-8 -*-

import os
import time
import sys
import json
from flask import Blueprint, url_for, render_template, request, abort, flash, session, redirect
from search_user_index_function import search_top_index, search_influence_detail, user_index_range_distribution,\
                                       search_max_single_field, search_portrait_history_active_info
from rank_portrait_in_active_user import search_portrait_user, portrait_user_vary
from search_vary_index_function import query_vary_top_k
from search_tag_in_portrait import search_tag
from user_portrait.global_utils import ES_CLUSTER_FLOW1 as es
from influence_description import influence_description

portrait_index = "copy_user_portrait" # user_portrait_database
portrait_type = "user"

mod = Blueprint('influence_application', __name__, url_prefix='/influence_application')

@mod.route('/search_influence/')
def ajax_search_influence():
    date = request.args.get('date', '') # '2013-09-01'
    number = request.args.get('number', 100) # "100"
    index = request.args.get('index', 1) # 1: influence rank, 2: hot origin weibo retweeted, 3: hot origin weibo comment, 4: hot origin weibo retweeted brust, 5: hot origin weibo comment brust
    domain = request.args.get('domain', 0) # 0: all active rank, 1: portrait active rank

    index_name = str(date).replace('-','')
    number = int(number)
    index = int(index)
    domain = int(domain)

    if not index_name:
        return 0

    if index == 1:
        if domain == 0:
            results = search_top_index(index_name, number)
        else:
            results = search_portrait_user(es, number, index_name, "bci", portrait_index, portrait_type)

    elif index == 2:
        if domain == 0:
            results = search_top_index(index_name, number, "bci", False, "origin_weibo_retweeted_top_number")
        else:
            results = search_max_single_field("origin_weibo_retweeted_top_number", index_name, "bci", number)

    elif index == 3:
        if domain == 0:
            results = search_top_index(index_name, number, "bci", False, "origin_weibo_comment_top_number")
        else:
            results = search_max_single_field("origin_weibo_comment_top_number", index_name, "bci", number)

    elif index == 4:
        if domain == 0:
            results = search_top_index(index_name, number, "bci", False, "origin_weibo_retweeted_brust_average")
        else:
            results = search_portrait_user(es, number, index_name, "bci", portrait_index, portrait_type, field="origin_weibo_retweeted_brust_average")

    elif index == 5:
        if domain == 0:
            results = search_top_index(index_name, number, "bci", False, "origin_weibo_comment_brust_average")
        else:
            results = search_portrait_user(es, number, index_name, "bci", portrait_index, portrait_type, field="origin_weibo_comment_brust_average")

    else:
        results = []

    return json.dumps(results)



@mod.route('/specified_user_active/')
def ajax_specified_user_active():
    date = request.args.get('date', '') # '2013-09-01'
    uid = request.args.get('uid', '') # 123456,123456
    date = str(date)

    results = []

    if date and uid:
        index_name = date.replace('-','')
        list_1 = []
        uid_list = [item for item in uid.split(',')]
        result = search_influence_detail(uid_list, index_name, "bci") 

        description = influence_description(result)
        results.append(result)
        results.append(description)

    return json.dumps(results)



@mod.route('/user_index_distribution/')
def ajax_user_index_distribution():
    date = request.args.get('date', '') # '2013-09-01'
    date = str(date)

    if not date:
        results = []
    else:
        index_name = date.replace('-','')
        results = user_index_range_distribution(index_name, "bci", "user_index")

    return json.dumps(results)

@mod.route('/portrait_user_index_distribution/')
def ajax_portrait_user_index_distribution():
    date = request.args.get('date', '') # '2013-09-01'
    date = str(date)

    if not date:
        results = []
    else:
        date = date.replace('-','')
        results = user_index_range_distribution("copy_user_portrait","user", date)

    return json.dumps(results)

"""
@mod.route('/portrait_user_domain_rank/')
def ajax_portrait_user_domain_rank():
    results = []
    date = request.args.get('date', '')
    domain = request.args.get('domain', '')
    number = request.args.get('number', '')
    if date and domain:
        results = portrait_user_domain_rank(date, domain, number)

    return json.dumps(results)
"""


@mod.route('/portrait_history_active/')
def ajax_portrait_history_active():
    date = request.args.get('date', '')# 2013-09-01
    uid = request.args.get('uid', '')

    if not uid or not date:
        results = []
    else:
        date = str(date).replace('-','')
        results = search_portrait_history_active_info(uid, date)

    return json.dumps(results)

@mod.route('/vary_top_k/')
def ajax_vary_top_k():
    results = []
    number = request.args.get('number', 100) # "100"
    number = int(number)

    results = query_vary_top_k("vary", "bci", number)

    return json.dumps(results)



@mod.route('/portrait_user_in_vary/')
def ajax_portrait_user_in_vary():
    number = request.args.get('number', 100) # "10"
    results = portrait_user_vary(es, number, "vary", "bci", portrait_index, portrait_type, "vary")

    return json.dumps(results)


@mod.route('/portrait_user_tag/')
def ajax_portrait_user_tag():
    number = int(request.args.get('number', 10)) # "10"
    date = request.args.get('date', '') # 2013-09-01
    date = date.replace('-','')

    tag = request.args.get('tag', '') # topic
    tag_value = request.args.get('tag_value', '') # education
    search_dict = {}
    search_dict[tag] = tag_value
    print search_dict

    if date and tag and tag_value:
        results = search_tag(es, number, date, "bci", "user_portrait", "user", search_dict)
        return json.dumps(results)

    results = []
    return json.dumps(results)
