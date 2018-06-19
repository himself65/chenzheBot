import json


def CZBotWordTest():
    from bot.CZBotWord import CZBotWord

    def display(s):
        print(bot.getSentence(s))
    bot = CZBotWord()
    display("chenzhe好强啊")
    display("chenzhe为什么这么强")
    display("chenzhe强")
    display("...")


if __name__ == '__main__':
    CZBotWordTest()
