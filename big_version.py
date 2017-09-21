#!/usr/bin/env python
# encoding: utf-8

import sys
from collections import OrderedDict

from pyquery import PyQuery as pq
from workflow import Workflow

log = None


def get_version(url):
    # 获得文档对象
    doc = pq(url)
    # 创建版本列表
    version_dict = OrderedDict([])
    tbodys = doc('.versions').find('tbody')
    for tbody in tbodys.items():
        trs = tbody('tr')
        sm_list = []
        # 转成list
        v_list = list(trs.items())
        # 判断是否有一个版本
        is_only_one = len(v_list) == 1
        for i, tr in enumerate(v_list):
            if i != 0 or is_only_one:
                sm_list.append(tr('a:first').text())
        version_dict[tbody('tr:first').find('b').text() + '.x'] = str(sm_list)
    return version_dict


def main(wf):
    # 获得参数
    params = wf.args[0]
    # params = "http://mvnrepository.com/artifact/com.jayway.restassured/spring-mock-mvc"
    # 获得project
    versions = get_version(params)
    for version in versions.keys():
        # match = re.match(r'^http://mvnrepository.com/artifact/(.+)(/.+)$', params)
        # group = match.group(1)
        sm_v = str(versions[version])
        wf.add_item(title=version, subtitle=sm_v, arg=params + ":-:" + sm_v, valid=True, icon='icon/version.png')

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
