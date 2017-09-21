#!/usr/bin/env python
# encoding: utf-8

import os
import re
import sys

from pyquery import PyQuery as pq
from workflow import Workflow, web

log = None

# 基础地址
BASE_URL = 'http://mvnrepository.com'


def get_url(key, page=1):
    return BASE_URL + "/search?q=" + key + "&p=" + str(page)


def get_projects(key, page=1):
    # 获得整个文档
    doc = pq(get_url(key, page))
    # 获得主内容
    main_content = doc('#maincontent')
    # 获得总结果数
    counts = main_content('h2:first').find('b').text()
    # print(counts)
    # 项目列表
    projects = []
    for im in main_content('.im').items():
        title = im('.im-header').find('h2.im-title').find('a[class!=\'im-usage\']')
        if title:
            name = title.text()
            url = title.attr('href')
            img = im('picture').find('img')
            logo = img.attr('src')
            subtitle = im('.im-header').find('p.im-subtitle')
            group = subtitle('a:first').text()
            # print(name + "-" + url + "-" + logo + " - " + group)
            projects.append({'name': name, 'url': BASE_URL + url, 'logo': logo, 'group': group})

    # 分页计算
    counts = int(counts)
    pages = counts // 10
    if counts % 10 != 0:
        pages = pages + 1

    if 0 < counts < 10:
        pages = 1

    return {'projects': projects, 'pages': pages, 'counts': counts}


def main(wf):
    # 获得参数
    params = wf.args[0]
    # params = '\'sp\': x'
    params_arr = re.split(r'\s*:\s*', params)
    # 获取页数
    key = params_arr[0]

    count = key.count('\'')
    if count == 0 or count == 2:
        page = 1
        if len(params_arr) == 2 and params_arr[1]:
            try:
                page = int(params_arr[1])
            except ValueError:
                pass
        # 获得project
        url_ = re.sub(r'\s+', '+', key)
        page = get_projects(url_, page)
        projects = page['projects']
        for project in projects:
            name_ = project['name']
            group_ = project['group']
            png = 'icon/' + group_ + '.png'
            if not os.path.exists(png):
                if not os.path.exists('icon/'):
                    os.mkdir('icon/')
                web.get(project['logo']).save_to_path(png)
            wf.add_item(title=name_, subtitle=group_, arg=project['url'], valid=True, icon=png)
    else:
        wf.add_item(title=u'请继续输入...', subtitle=u'请继续输入...')

    # valid=True 告诉alfred把arg传递给下一个动作
    # 把结果转成xml发给alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
