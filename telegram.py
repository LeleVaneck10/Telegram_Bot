from asyncore import dispatcher
from tokenize import Token
import telegram.ext

Token = "5661598141:AAEnLUzNHjbUdtCxaXuo551E5upOsc1HHnQ"

updater = telegram.ext.updater("5661598141:AAEnLUzNHjbUdtCxaXuo551E5upOsc1HHnQ", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to LeleVaneck Bot engine")
    
def help(update, context):
    update.message.reply-text(
    """
    /start -> Welcome to the channel
    /help -> This paticular message
    /content -> About various Playlist of LeleVaneck
    /Python -> The first video from python playlist
    /SQL -> The first video from Java Playlist
    /contact -> contact information
    """
    )