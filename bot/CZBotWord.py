# coding:utf8
from redis import Redis  # 实现持久化存储


class CZBotWord:
    """
    chenzhe机器人自然语言处理部分

    **NOTICE**: 使用前请开启redis, host='localhost', port=6379
    """

    @staticmethod
    def loadFromJson(path='./json/cz_list.json'):
        """
        从JSON中加载语录
        """
        import json
        with open(path) as f:
            data = json.load(f)
        return data if data else {}

    def __init__(self, *args, **kwargs):
        """
        初始化CZBotWord
        """
        self.redis = Redis()
        data = self.loadFromJson()
        for (key, items) in data.items():
            if isinstance(items, list):
                for item in items:
                    if self.redis.get(item) is None:
                        self.redis.set(item, key)
            elif isinstance(items, str):
                if self.redis.get(items) is None:
                    self.redis.set(items, key)

    def setWord(self, key, value):
        """
        设置chenzhe的语录，将会持久化保存

        params:
            key 键
            value 值
        """
        if not isinstance(key, (str)) or not isinstance(value, (str)):
            raise ValueError("key或value必须为str类型")
        self.redis.set(key, value)

    def getWord(self, key):
        if not isinstance(key, (str)):
            raise ValueError("key必须为str类型")
        return self.redis.get(key)

    def getSentence(self, sentence):
        """
        cz_list 将转化为 dictionary 的 value 部分

        returns: str

        examples:
            根据传入的字符串返回适合的chenzhe语句
            >>> getWord("chenzhe大佬")
            我是蒟蒻
        """
        if sentence == '':
            return ''
        import jieba

        def decode(s):
            """
            convert bytes to str (utf-8)

            param:
                s bytes
            """
            if s is None:
                return ''
            return s.decode('utf-8')
        seg_list = jieba.lcut(sentence)
        first = seg_list[0]  # 头
        chenzhe = ['chenzhe', 'chen_zhe']
        if str.lower(first) in chenzhe:
            # chenzhe匹配模式：查找chenzhe开头的字串
            for item in seg_list[1:]:
                key = first+item
                ans = self.redis.get(key)
                if ans is not None:
                    return decode(ans) if ans else ''
        elif len(seg_list) == 1:
            # 当只有一个元素的时候
            ans = self.redis.get(seg_list[0])
            return decode(ans) if not ans else ''
        else:
            # 普通匹配模式：查找每一个分词
            for item in seg_list:
                ans = self.redis.get(first+item)
                if ans is not None:
                    return decode(ans) if ans else ''
