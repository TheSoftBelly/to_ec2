import requests
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
 
BOT_TOKEN='5781904929:AAF6g8rJ2fq6kWsyJExy9WkKI4I3a0cYFeI'
 
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher

 
def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="작업을 중단합니다.")
 
def email_add(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="[{}]를 추가합니다.".format( context.args[0] ))
    file = open('/home/ubuntu/workspace/to_ec2/email_list.txt','a',encoding='UTF-8')
    file.write(context.args[0]+'\n')
    file.close()

def email_del(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="[{}]를 제거합니다.".format( context.args[0] ))
    file = open('/home/ubuntu/workspace/to_ec2/email_list.txt','r',encoding='UTF-8')
    if context.args[0] in file.read():
        new_file_list=file.read().replace(context.args[0]+'\n','')
    file.close()
    file = open('/home/ubuntu/workspace/to_ec2/email_list.txt','w',encoding='UTF-8')
    file.write(new_file_list)
    file.close()
    


def email_show(update, context):
    file = open('/home/ubuntu/workspace/to_ec2/email_list.txt','r',encoding='UTF-8')
    context.bot.send_message(chat_id=update.effective_chat.id, text="[{}] 가 현재 있습니다!".format( file ))
    file.close()

stop_handler = CommandHandler('stop', stop)
email_add_handler = CommandHandler('email_add', email_add)
email_del_handler = CommandHandler('email_del', email_del)
email_show_handler = CommandHandler('email_show', email_show)


dispatcher.add_handler(stop_handler)
dispatcher.add_handler(email_add_handler)
dispatcher.add_handler(email_del_handler)
dispatcher.add_handler(email_show_handler)
 
updater.start_polling()
updater.idle()