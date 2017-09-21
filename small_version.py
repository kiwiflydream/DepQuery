#!/usr/bin/env python
# encoding: utf-8

import re
import sys
from collections import OrderedDict

from workflow import Workflow

log = None


def get_version(params):
    # 参数数组
    params_arr = str(params).split(":-:")
    url = params_arr[0]
    # 过滤字符
    sub = re.sub(r'[\[\]"\'\s]', '', params_arr[1])
    v_list = list(sub.split(','))
    version = OrderedDict([])
    for v in v_list:
        get_url = url + "/" + v
        # doc = pq(get_url)
        # dependency = doc('#maven-a').text()
        version[v] = get_url

    return version


def main(wf):
    # 获得参数
    params = wf.args[0]
    # params = "http://mvnrepository.com/artifact/org.springframework/spring-context:-:['5.0.0.RC2', '5.0.0.RC1', '5.0.0.M5', '5.0.0.M4', '5.0.0.M3', '5.0.0.M2', '5.0.0.M1']"
    # 获得project
    versions = get_version(params)
    for version in versions.keys():
        url = versions[version]
        # match = re.match(r'^http://mvnrepository.com/artifact/(.+)(/.+)$', url)
        # group = match.group(1)
        wf.add_item(title=version, subtitle=version, arg=url, valid=True, icon='icon/version.png')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
