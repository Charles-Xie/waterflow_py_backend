from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import codecs
from .settings import BASE_DIR

from .utils import filters

my_filter = filters.SensitiveFilter(BASE_DIR + "/PipeTest/utils/sensitive.txt")

class Message:
    msg = ""

    def __init__(self):
        print("msg init")

    @classmethod
    def append_msg(cls, msg):
        cls.msg += msg
        return cls.msg

    @classmethod
    def get_msg(cls):
        res = cls.msg
        cls.msg = ""
        return res


@csrf_exempt
def hello(request):
    if request.method == 'GET':
        msg = request.GET['msg']

        if my_filter.test(msg):
            res = {"rmsg": "failed"}
        else:
            print("received: " + msg)
            # print(Message.append_msg(msg))
            with codecs.open("message.txt", 'a', 'utf-8') as file:
                file.write(msg)
            res = {"rmsg": "success"}
    else:
        res = {"rmsg": "ignore GET method"}
    return JsonResponse(res)


@csrf_exempt
def get_msg(request):
    # res = {"msg": Message.get_msg()}
    return HttpResponse(Message.get_msg())