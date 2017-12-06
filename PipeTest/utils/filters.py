import re

class SensitiveFilter(object):
    """sensitive word filter"""

    def __init__(self, fname):
        # file name
        self.f_name = fname
        f_obj = open(self.f_name, 'r', encoding='utf8')
        f_cont = f_obj.read()
        re_cont = f_cont.replace('\n', '|')
        if re_cont[-1] == '|':
            re_cont = re_cont[0:-1]
        # reg exp content
        self.re_cont = re_cont
        # reg exp
        self.re_rule = re.compile(re_cont)

    def test(self, message):
        """test if any sensitive words exist in the given message"""
        if self.re_rule.search(message):
            # 敏感词
            # return "Big brother is watching you!"
            print(self.re_rule.search(message))
            return True
        else:
            # 非敏感词
            # return "发送成功！"
            return False


    
