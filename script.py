# -*- coding:utf-8 -*-
import mitmproxy.http

t0 = 'Object.defineProperties(navigator,{webdriver:{get:() => undefined}});'

# 如使用无头浏览器需添加下列参数，根据实际驱动情况修改参数
# t1 = 'window.navigator.chrome = {runtime: {},// etc.};'

# t2 = '''
# Object.defineProperty(navigator, 'languages', {
#       get: () => ['en-US', 'en']
#     });
# '''

# t3 = '''
# Object.defineProperty(navigator, 'plugins', {
#     get: () => [1, 2, 3, 4, 5,6],
#   });
# '''

# t4 = '''
#    Object.defineProperties(navigator,{
#      userAgent:{
#        get: () => Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36;
#      }
#    })
# '''


class Tb(object):
    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 改变selenium特征值
        if '114.js' in flow.request.url or 'um.js' in flow.request.url:
            flow.response.text = t0 + flow.response.text
            # headless 开启
            # flow.response.text = t0 + t1 + t2 + t3 + t4 + flow.response.text

        # 无需验证
        if 'request_nick_check' in flow.request.url:
            flow.response.text = flow.response.text.replace('"needcode":true', '"needcode":false')


addons = [
    Tb()
]