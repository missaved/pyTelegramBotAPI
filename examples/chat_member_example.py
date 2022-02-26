import json
import logging
import time
from socket import socket

import socks
import telebot
from telebot import types, util

socks.set_default_proxy(socks.SOCKS5, "192.168.5.20", 7893)
socket.socket = socks.socksocket
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = '5219990394:AAGJRCUNmzZvoIxuX0nNyN1DVN-sbfY5FGM'
bot = telebot.TeleBot(TOKEN)
menu_txt = {
    "inline_keyboard": [
        [
            {
                "text": "西安夜生活洗浴指南总汇",
                "url": "https://t.me/xianyuledaquan"
            },

        ],
        [

            {
                "text": "东郊",
                "url": "https://t.me/xian_chengdong"
            },
            {
                "text": "西郊",
                "url": "https://t.me/xian_chengxi"
            },
            {
                "text": "南郊",
                "url": "https://t.me/xian_chengnan"
            },
            {
                "text": "北郊",
                "url": 'https://t.me/xian_chengbei'
            }
        ],

        [
            {
                "text": "好评推荐",
                "url": "https://t.me/sex_zhonglouo"
            },
            {
                "text": "兼职外卖",
                "url": "https://t.me/sex_opodoor"
            }

        ],
        [
            {
                "text": "在线客服1",
                "url": "http://t.me/xx01125"
            },
            {
                "text": "在线客服2",
                "url": "http://t.me/Sexbaby_xian"
            }

        ],

    ]
}
msg1 = """

<B>🔔 ：西安近百家洗浴会所，各种类型应有尽有，全套店.口爆店.莞式店.情景扮演制服丝袜另有兼职妹妹上门服务。</B>

🔔 新         手         步         骤 🔔  
1️⃣: 发你的位置,说出你的预算.
2️⃣: 给你就近推荐安排。全城享受会员Vip最低价格。
3️⃣: 全程无任何费用。（外围高端除外）

<B>了   解   详   情   进   群   咨   询 </B>
⬇️ ➖  ⬇️  ➖   ⬇️ ➖ ⬇️

"""
msg4 = '''
<B>🔔 :西安近百家洗浴会所，各种类型应有尽有，全套店.口爆店.莞式店.情景扮演制服丝袜另有兼职妹妹上门服务。</B>

      <a href='https://t.me/xian_chengdong'>★★★东郊资源大全★★★</a>

<a href='https://telegra.ph/ddxxh-02-19'>02:东郊星海spa  价位:498起 </a>

<a href='https://telegra.ph/5-lukou-02-07'>03:东郊五路口葡京  价位:698起 </a>

<a href='https://telegra.ph/djbq1-02-07'>04:东郊灞桥海选  价位:698起 </a>

<a href='https://telegra.ph/ddjdtgj-02-19'>05:东郊曲江[大唐国际]  价位:998起 </a>

<a href='https://telegra.ph/qjdj-02-25'>06:曲江东郊情景大池【华清池】  价位:1398起 </a>

      <a href='https://t.me/xian_chengnan'>★★★南郊资源大全★★★</a>

<a href='https://telegra.ph/ybl-02-13'>01:南郊迎宾楼  价位:498起 </a>

<a href='https://telegra.ph/djbq1-02-07'>02:南郊高新三星  价位:698起 </a>

<a href='https://telegra.ph/gxzy-02-10'>03:南郊高新紫韵  价位:598起 </a>

<a href='https://telegra.ph/newaom-02-10'>04:南郊高新新澳门  价位:598起 </a>

<a href='https://telegra.ph/jha-02-25'>05:西郊高新【金海岸】  价位:598起 </a>

<a href='https://telegra.ph/%E5%8D%97%E9%83%8A-%E5%8D%97%E4%BA%8C%E7%8E%AF%E6%B0%B8%E6%9D%BESPA-02-07'>06:南郊南二环永松  价位:698起 </a>

<a href='https://telegra.ph/nnjnhzx-02-25'>07:南郊电视台南海之星  价位:798起 </a>

<a href='https://telegra.ph/xzqs-02-07'>08:南郊青舍  价位:898起 </a>

<a href='https://telegra.ph/nnjgx-02-20'>09:南郊太白南路·夜上海  价位:898起 </a>

<a href='https://telegra.ph/dstsst-02-25'>10:南郊电视塔水尚堂  价位:998起 </a>

<a href='https://telegra.ph/nnjzd-02-19'>11:南郊倾城国际  价位:998起 </a>

<a href='https://telegra.ph/xxichengguoji-02-07'>12:南郊高新西城国际  价位:1398起 </a>

<a href='https://telegra.ph/gaoxindongshang-02-07'>13:南郊高新东尚  价位:1498起 </a>

<a href='https://telegra.ph/njyh-02-13'>14:南郊曲江永辉名模  价位:1798起 </a>

<a href='https://telegra.ph/qujiangxingzuou-02-07'>15:南郊曲江星座国际  价位:2498起 </a>


      <a href='https://t.me/xian_chengbei'>★★★北郊资源大全★★★</a>

<a href='https://telegra.ph/bjhh-02-19'>02:北郊凤八[后海]  价位:498起</a>

<a href='https://telegra.ph/bjls-02-19'>03:北郊龙首[皇马]  价位:498起</a>

<a href='https://telegra.ph/bjmannii-02-07'>04:北郊曼尼SPA  价位:598起</a>

<a href='https://telegra.ph/bjfc-02-19'>05:北郊凤城六路天池海选  价位:698起</a>

<a href='https://telegra.ph/bbjbm-02-19'>06:北郊白马庄园  价位:798起</a>

<a href='https://telegra.ph/bjjzklxq-02-25'>07:北郊金樽快乐星球  价位:998起 </a>

<a href='https://telegra.ph/bhwq1-02-07'>08:北郊龙首北海温泉  价位:1398起</a>

<a href='https://telegra.ph/bhwq1-02-07'>09:北郊龙首北海温泉  价位:1398起</a>

<a href='https://telegra.ph/bjxinsj-02-25'>10:北郊·新世界  价位:1498起 </a>

<a href='https://telegra.ph/old-place-02-07'>11:北郊老地方  价位:1498起</a>

<a href='https://telegra.ph/bjkongge-02-25'>12:北郊空格温泉浴池  价位:1798起 </a>

<a href='https://telegra.ph/chenhuim-01-29'>13:北郊吉源T台  价位:1998起</a>

<a href='https://telegra.ph/%E5%B7%A5%E4%BD%9C%E6%80%BB%E7%BB%93-01-29'>14:北郊伯爵  价位:2498起</a>

<a href='https://telegra.ph/zl2-02-19'>01:钟楼城内★西宫海选  价位:598起 </a>

<a href='https://telegra.ph/bdj-02-20'>02:北大街迪奥制服  价位:598起 </a>

<a href='https://telegra.ph/zlxm1-02-07'>03:钟楼西门蜜桃轻奢  价位:698起 </a>

<a href='https://telegra.ph/bdj-02-23'>04:钟楼北大街唐朝汇  价位:798起 </a>

<a href='https://telegra.ph/xxmhdspa-02-25'>05:西关正街洪都SPA  价位:1398起 </a>

<B>了   解   详   情   进   群   咨   询 </B>
⬇️ ➖  ⬇️  ➖   ⬇️ ➖ ⬇️
'''


# chat_member_handler. When status changes, telegram gives update. check status from old_chat_member and new_chat_member.
@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        r = bot.send_message(message.chat.id, "欢迎 {name}!".format(name=new.user.first_name) + msg1, parse_mode='html',
                             disable_web_page_preview=True,
                             reply_markup=json.dumps(menu_txt))  # Welcome message
        # global welcom_id
        # welcom_id = r.message_id
        print(r.message_id)
        time.sleep(5)
        bot.delete_message(message.chat.id, r.message_id)


# if bot is added to group, this handler will work
@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id, "Somebody added me to group")  # Welcome message, if bot was added to group
        bot.leave_chat(message.chat.id)


# content_Type_service is:
# 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created',
# 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message',
# 'proximity_alert_triggered', 'voice_chat_scheduled', 'voice_chat_started', 'voice_chat_ended',
# 'voice_chat_participants_invited', 'message_auto_delete_timer_changed'
# this handler deletes service messages

@bot.message_handler(content_types=util.content_type_service)
def delall(message: types.Message, ):
    # time.sleep(10)
    # print('Del it')
    bot.delete_message(message.chat.id, message.message_id)
    # time.sleep(60)
    # bot.delete_message(message.chat.id, message.message_id+1)


bot.infinity_polling(allowed_updates=util.update_types)
