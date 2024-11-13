from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '7581765909:AAFSMJAZ_kvLTLGhjhZiF23A48Y_QkRpTBw'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("ciao sono pelosetto... il bot del gruppo just furry... sono felice di aiutarti in qualunque modo")

def regole(update: Update, context: CallbackContext):
    regole_testo = """Queste sono le regole del gruppo:

1. niente spam, è un gruppo per chiacchierare e non vogliamo persone che publicano 100 messaggi al secondo.
2. niente contenuti nsfw, cè gente ancora minorenne perfavore.
3. il black humor e consentito senza esagerazione e comunque usato solo per scherzare non per mancare di rispetto ai componenti del gruppo.
4. appena entrate nel gruppo vi chiedo di presentarvi con *nome furrsona, età, e da quanto sei nel fandom*.

questo gruppo non bannera mai persone, ma se non rispettate le regole vi possiamo limitare"""
    
    update.message.reply_text(regole_testo, parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("regole", regole))

    print("Bot avviato con successo!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()