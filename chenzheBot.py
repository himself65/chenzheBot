"""
chenzhe Bot 主程序
通过`python run.py`调用
"""
from bot.CZBotWord import CZBotWord

czbot = CZBotWord()
group_name = ['hxr粉丝群', ]


def onQQMessage(bot, contact, member, content):
    if contact.ctype != 'group':
        # 忽略非群消息
        return
    if contact.nick in group_name:
        ans = czbot.getSentence(content)  # 得到回复内容，有可能为空
        if ans == '' or ans is None:
            return
        bot.SendTo(contact, ans)
