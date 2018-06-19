"""
chenzhe Bot 主程序
通过`python run.py`调用
"""
from qqbot import _bot as bot

qqbot_dir = '~/.qqbot-tmp/'
qq_plugins_dir = qqbot_dir + 'plugins'

qqID = '761282619'       # QQ号
group_name = 'hxr粉丝群'  # 监听的群

if __name__:
    bot.Login(['-q', qqID])
    group = bot.List('group', 'hxr粉丝群')[0]
    bot.SendTo(group, '测试一下Bot')
