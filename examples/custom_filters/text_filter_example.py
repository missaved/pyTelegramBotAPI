import logging
from socket import socket

import socks
import telebot
from telebot import custom_filters

socks.set_default_proxy(socks.SOCKS5, "192.168.5.20", 7893)
socket.socket = socks.socksocket
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)
TOKEN = '5219990394:AAGJRCUNmzZvoIxuX0nNyN1DVN-sbfY5FGM'
bot = telebot.TeleBot(TOKEN)
msg0 = '''
<B>🔔 ：西安近百家洗浴会所，各种类型应有尽有，全套店.口爆店.莞式店.情景扮演制服丝袜另有兼职妹妹上门服务。

🔔  新         手         步         骤  🔔  
1️⃣: 发你的位置,说出你的预算.
2️⃣: 给你就近推荐安排。全城享受会员Vip最低价格。
3️⃣: 全程无任何费用。（外围高端除外）

老板你好。问我吧。很简单。
直接输入即可。比如你在东郊。那你直接输入‘东郊’ 二字即可。
还有什么不懂的可以直接问<a href='http://t.me/xx01125'>客服咨询。</a></B>



'''
msg1 = '''
      <a href='https://t.me/xian_chengdong'>★★★东郊资源大全★★★</a>

<a href='https://telegra.ph/ddjdh-02-19'>01:东郊东海  价位:398起 </a>

<a href='https://telegra.ph/ddxxh-02-19'>02:东郊星海spa  价位:498起 </a>

<a href='https://telegra.ph/5-lukou-02-07'>03:东郊五路口葡京  价位:698起 </a>

<a href='https://telegra.ph/djbq1-02-07'>04:东郊灞桥海选  价位:698起 </a>

<a href='https://telegra.ph/ddjdtgj-02-19'>05:东郊曲江[大唐国际]  价位:998起 </a>

<a href='https://telegra.ph/qjdj-02-25'>06:曲江东郊情景大池【华清池】  价位:1398起 </a>
'''
msg2 = '''
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
'''
msg3 = '''
西郊资源少啊。可以考虑高新或者咸阳资源！
'''
msg4 = '''
      <a href='https://t.me/xian_chengbei'>★★★北郊资源大全★★★</a>

<a href='https://telegra.ph/bjlcg-02-19'>01:北郊玉祥门老城根[龙湖]  价位:398起</a>

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

'''
msg5 = '''
<a href='https://t.me/auto_fb'>★★★城内资源大全★★★</a>

<a href='https://telegra.ph/zl2-02-19'>01:钟楼城内★西宫海选  价位:598起 </a>

<a href='https://telegra.ph/bdj-02-20'>02:北大街迪奥制服  价位:598起 </a>

<a href='https://telegra.ph/zlxm1-02-07'>03:钟楼西门蜜桃轻奢  价位:698起 </a>

<a href='https://telegra.ph/bdj-02-23'>04:钟楼北大街唐朝汇  价位:798起 </a>

<a href='https://telegra.ph/xxmhdspa-02-25'>05:西关正街洪都SPA  价位:1398起 </a>
'''
msg6 = '''
      <a href='https://t.me/xian_chengbei'>★★★咸阳资源大全★★★</a>
      
<a href='https://telegra.ph/xxjsqhg-02-20'>01:西郊三桥后宫  价位:298起 </a>

<a href='https://telegra.ph/xy1-02-13'>02:咸阳世纪大道[凤求凰]  价位:398起</a>

<a href='https://telegra.ph/xy2-02-13'>03:咸阳大富豪、月光、温柔乡、国色天香   价位:698起</a>

<a href='https://telegra.ph/tokyo-hot-02-25'>04:三桥后卫寨【东京热】  价位:1398起 </a>
'''
msg7 = '''

<B>这个需求需要单独联系：<a href='http://t.me/xx01125'>客服</a></B>
     
<B>「需要时请提供酒店定位跟房卡照片 」
在岗信息需要时时重新整理 为避免浪费彼此时间 请确定需要时联系 望理解

1.需预付定金一百 作为路费  看不上可以免费 换一次人 三环外需+路费100
2.见面满意付尾款 开始服务 诚信为本 本质服务 不会跑路
3.女娃私下要路费不要发 定金已包含在总费用</B>
'''


#
@bot.message_handler(text=['帮助', '资源', '新手', '导航', '价格'])
def start_filter(message):
    bot.send_message(message.chat.id, msg0, parse_mode='html', disable_web_page_preview=True)


# Check if message starts with @admin tag
@bot.message_handler(text=['东', '东郊'])
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg1, parse_mode='html', disable_web_page_preview=True)


@bot.message_handler(text=['南郊', '高新', '南'])
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg2, parse_mode='html', disable_web_page_preview=True)


@bot.message_handler(text_startswith="西郊")
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg3, parse_mode='html', disable_web_page_preview=True)
    # Check if text is hi or hello


#
@bot.message_handler(text_startswith="北郊")
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg4, parse_mode='html', disable_web_page_preview=True)


#
@bot.message_handler(text_startswith="城内")
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg5, parse_mode='html', disable_web_page_preview=True)


#
@bot.message_handler(text=['咸阳', '三桥'])
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg6, parse_mode='html', disable_web_page_preview=True)


#
@bot.message_handler(text=['外围', '上门', '外围上门', '价格'])
def start_filter(message):
    bot.send_message(message.chat.id, '老板来了。这里就是你要的哦。' + '\n' + msg7, parse_mode='html', disable_web_page_preview=True)


# @bot.message_handler(text_contains=['你','我'])
# def text_filter(message):
#     bot.send_message(message.chat.id, "Hi, {name}!".format(name=message.from_user.first_name))


# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())
# bot.add_custom_filter(custom_filters.TextContainsFilter())

bot.infinity_polling()
