"""
初始化chenzheBot相关代码

之前请确保Redis服务开启，具体操作请到README.md

- Redis加载

"""
from bot.CZBotWord import CZBotWord

if __name__ == '__main__':
    CZBotWord.initRedis()
    
