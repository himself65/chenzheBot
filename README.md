# chenzheBot

他改变了中国，chenzhe改变了OI

## 运行方法

1. 登陆QQBot，扫描二维码

    ```bash

    pip install qqbot

    qqbot
    ```

2. 将全部文件复制到 ~/.qqbot-tmp//plugins/ 下

3. 启动另一个控制台

    ```bash
    pip install redis

    redis-server /usr/local/etc/redis.conf

    qq plug chenzheBot
    ```

## 扩展词典

在 json/cz_list.json 中编写