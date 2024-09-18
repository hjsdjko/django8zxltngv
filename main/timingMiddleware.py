import base64
import time

from main.models import syslog

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    request_list = ['add','save','update','shBatch','delete','alipay','importExcel','compose']

    def __call__(self, request):
        request_url = request.get_raw_uri()
        new_log = False
        for item in self.request_list:
            if item in request_url:
                new_log = True
                break
        if not new_log:
            return self.get_response(request)

        start_time = int(time.time()*1000)
        response = self.get_response(request)
        end_time = int(time.time()*1000)
        try:
            duration = end_time - start_time
            # 获取请求参数
            request_params = request.body.decode('utf-8')
            # 获取请求 IP 地址
            remote_ip = request.META.get('REMOTE_ADDR')
            token = request.META.get('HTTP_TOKEN')
            decode_str = eval(base64.b64decode(token).decode("utf8"))
            username=""
            if decode_str['tablename']=='jiaoshi':
                username = decode_str['params']['jiaoshigonghao']
            elif decode_str['tablename']=='users':
                username = decode_str['params']['username']
            if decode_str['tablename']=='xuesheng':
                username = decode_str['params']['xuehao']
            elif decode_str['tablename']=='users':
                username = decode_str['params']['username']
            dict = {
                'method': request.funname,
                'params': request_params,
                'username': username,
                'time': duration,
                'ip': remote_ip,
                'operation': request.operation,
            }
            syslog.createbyreq(syslog, syslog, dict)
        except:
            pass
        return response
