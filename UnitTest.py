import json


def CZBotWordTest():
    from bot.CZBotWord import CZBotWord

    def display(s):
        print(bot.getSentence(s))
    bot = CZBotWord()
    CZBotWord.initRedis()
    display("chenzhe好强啊")
    display("chenzhe为什么这么强")
    display("will爷")
    display("chenzhe强")
    display("基础知识")
    display("人类的本质是什么")
    display("啥？")
    # display("...")


def QQBotTest():
    from qqbot import _bot as bot
    qqID = '761282619'       # QQ号
    group_name = 'hxr粉丝群'  # 监听的群s
    bot.Login(['-q', qqID])
    group = bot.List('group', group_name)[0]
    bot.SendTo(group, '测试一下Bot')


if __name__ == '__main__':
    CZBotWordTest()
