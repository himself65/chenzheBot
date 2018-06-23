"""
chenzhe Bot 主程序
通过`python run.py`调用
"""
from bot.CZBotWord import CZBotWord

czbot = CZBotWord()
group_name = ['hxr粉丝群', ]
message_list = []

def onQQMessage(bot, contact, member, content):
    if len(message_list) > 10:
        message_list.clear()
    if contact.ctype != 'group':
        # 忽略非群消息
        return
    if contact.nick in group_name:
        ans = czbot.getSentence(content)  # 得到回复内容，有可能为空
        if ans == '' or ans is None:
            return
        if ans not in message_list:
            bot.SendTo(contact, ans)
            message_list.append(ans)
        
