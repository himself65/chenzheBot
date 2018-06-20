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

    @staticmethod
    def __loadToRedis(data):
        redis = Redis()
        for (key, items) in data.items():
            if isinstance(items, list):
                for item in items:
                    if redis.get(item) is None:
                        redis.set(item, key)
            elif isinstance(items, str):
                if redis.get(items) is None:
                    redis.set(items, key)

    @staticmethod
    def loadJsonToRedis(path):
        """
        从Json中加载数据到Redis
        """
        data = CZBotWord.loadFromJson(path=path)
        CZBotWord.__loadToRedis(data)

    @staticmethod
    def initRedis():
        """
        加载数据到redis
        """
        data = CZBotWord.loadFromJson()
        CZBotWord.__loadToRedis(data)

    def __init__(self, *args, **kwargs):
        """
        初始化CZBotWord
        """
        self.redis = Redis()

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
        """
        得到关键字的目标语录

        params:
            key 键

        returns:
            如果找不到，返回None，否则返回类型为bytes
        """
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
            >>> "我是蒟蒻"
        """
        if sentence == '':
            return ''
        import jieba

        def decode(s):
            """
            convert bytes to str (utf-8)

            param:
                s bytes

            returns:
                str()
            """
            if s is None:
                return ''
            return s.decode('utf-8')
        ans = self.redis.get(sentence)
        if ans is not None:
            return decode(ans)
        seg_list = jieba.lcut(sentence)
        first = seg_list[0]  # 头
        chenzhe = ['chenzhe', 'chen_zhe', 'cz']
        if str.lower(first) in chenzhe:
            # chenzhe匹配模式：查找chenzhe开头的字串
            for item in seg_list[1:]:
                key = first+item
                ans = self.redis.get(key)
                if ans is not None:
                    return decode(ans)
        elif len(seg_list) == 1:
            # 当只有一个元素的时候
            ans = self.redis.get(seg_list[0])
            return decode(ans)
        else:
            # 普通匹配模式：查找每一个分词
            for item in seg_list:
                ans = self.redis.get(first+item)
                if ans is not None:
                    return decode(ans)
        return None
