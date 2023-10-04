import json
from model.deepdives import DeepDives, Type, Variant
from service.drg import DRGService
from util.date import prettify_datetime
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes

#TOKEN = Final = '>token here<'
#BOT_USERNAME: Final = '>telegram @ bot user handle<'

# Starting service
drgService = DRGService()

# Functions
def getNormalDD() -> str:
    deep_dives: DeepDives = drgService.get_deepdives()
    answ: str = prettify_datetime(deep_dives.startTime) + " - " + prettify_datetime(deep_dives.endTime) + "\n"
    answ += deep_dives.variants[0].__str__()

    dd: Variant = deep_dives.get_variant(Type.DEEP_DIVE)
    for i in range(3):
        answ += '\nStage ' + str(dd.stages[i].id) + '\n'
        answ += str(dd.stages[i])

    return answ

def getEliteDD() -> str:
    deep_dives: DeepDives = drgService.get_deepdives()
    answ: str = prettify_datetime(deep_dives.startTime) + " - " + prettify_datetime(deep_dives.endTime) + "\n"
    answ += deep_dives.variants[1].__str__()
    
    dd: Variant = deep_dives.get_variant(Type.ELITE_DEEP_DIVE)
    for i in range(3):
        answ += '\nStage ' + str(dd.stages[i].id) + '\n'
        answ += str(dd.stages[i])

    return answ

def getRockAndStone() -> str:
    salute: str = drgService.get_salutes().get_random_salute()
    return salute

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown_v2('*Hello\!* I can provide details on weekly deep dives\.')

async def dd_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getNormalDD())

async def edd_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getEliteDD())

async def salute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getRockAndStone())


if __name__ == "__main__":
    print('Bot starting...')
    #app = Application.builder().token(TOKEN).build()
    
    # Commands
    #app.add_handler(CommandHandler('start', start_command))
    #app.add_handler(CommandHandler('dd', dd_command))
    #app.add_handler(CommandHandler('edd', edd_command))
    #app.add_handler(CommandHandler('salute', salute_command))
   
    # Poll
    print('Polling...')
    #app.run_polling(poll_interval=5)

    