import telegram.ext

Token = "5661598141:AAEnLUzNHjbUdtCxaXuo551E5upOsc1HHnQ"

updater = telegram.ext.updater("5661598141:AAEnLUzNHjbUdtCxaXuo551E5upOsc1HHnQ", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to LeleVaneck Bot engine")
    
def help(update, context):
    update.message.reply_text(
    """
    /start -> Welcome to the channel
    /help -> This paticular message
    /content -> About various Playlist of Programming with Mosh
    /Python -> The first video from python playlist
    /Java -> The first video from Java Playlist
    /Html -> The first video from Java Playlist
    /contact -> contact information
    """
    )
    
def content(update, context):
    update.message.reply_text("We have various playlists and articles available")
    
def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/_uQrJ0TkZlc")
     
def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/eIrMbAQSU34")
    
def Html(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/qz0aGYrrlhU")
    
def contact(update, context):
    update.message.reply_text("You can contact on the registered mail provided on the website")
    
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('Java', Java))
dispatcher.add_handler(telegram.ext.CommandHandler('Html', Html))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()