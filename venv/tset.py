#!/user/bin/env python
#-*- coding: utf-8 -*-
#author:spirit
#datetime:2019/8/4


import telegram
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
# 初始化 update_id
update_id = None
# 定义主函数
def main():
    global update_id
    ## 创建Bot类的对象，下方填入自己的TOKEN
    bot = telegram.Bot('903338968:AAHD4VGBXJI0e463WlbzM6pocZUuRkGCnf8')

    # 获取第一个挂起的update_id，这样我们可以跳过它以防万一
    # 得到一个 "Unauthorized" 异常.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    # 记录日志
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 主函数功能
    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # 用户已屏蔽或取消了与机器人对话时
            update_id += 1
# 定义复读机（雾
def echo(bot):
    global update_id
    # 在最后一个update_id之后请求更新
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # 如果Bot收到消息
            # 回复同样的消息给用户
            update.message.reply_text(update.message.text)
# 定义程序的入口
if __name__ == '__main__':
    main()