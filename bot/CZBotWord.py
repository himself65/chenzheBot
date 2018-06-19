

class CZBotWord:
    """
    chenzhe机器人语句部分
    """

    @staticmethod
    def loadFromJson(path='./json/cz_list.json'):
        """
        """
        import json
        with open(path) as f:
            data = json.load(f)
        return data if data else {}

    def __init__(self, *args, **kwargs):
        """
        初始化CZBotWord
        """
        self.__czDic = dict()

        # 初始化czDic
        data = self.loadFromJson()
        for (key, items) in data.items():
            if isinstance(items, list):
                for item in items:
                    self.__czDic[item] = key
            elif isinstance(items, str):
                self.__czDic[items] = key

    def setWord(self, key, value, save=True):
        """
        设置chenzhe的语录

        params:
            key 键
            value 值
            save 是否保存到本地，以便下次运行时调用
        """
        if not isinstance(key, (str)) or not isinstance(value, (str)):
            raise ValueError
        self.__czDic[key] = value

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
        seg_list = jieba.lcut(sentence)
        first = seg_list[0]  # 头
        if str.lower(first) == 'chenzhe':
            # chenzhe匹配模式：查找chenzhe开头的字串
            for item in seg_list[1:]:
                key = first+item
                try:
                    ans = self.__czDic[key]
                except KeyError:
                    continue
                return ans
        elif len(seg_list) == 1:
            # 当只有一个元素的时候
            try:
                ans = self.__czDic[seg_list[0]]
            except KeyError:
                return None
            return ans
        else:
            # 普通匹配模式：查找每一个分词
            for item in seg_list:
                try:
                    ans = self.__czDic[first+item]
                except KeyError:
                    first = item
                    continue
                # 如果还是找不到最后试一试全匹配
                return ans if not ans else self.__czDic[''.join(seg_list)]
