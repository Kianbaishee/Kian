from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# وظيفة لحظر المجموعات أو القنوات
async def ban_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.type in ["supergroup", "channel"]:
        chat_id = update.message.chat.id
        await context.bot.leave_chat(chat_id)
        await update.message.reply_text("تم حظر هذه المجموعة أو القناة.")

# وظيفة الرد على الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("مرحباً! سأقوم بحظر القنوات أو المجموعات عند إضافتي.")

def main():
    # ضع التوكن الخاص بك هنا
    TOKEN = "7539418866:AAEmm-CelA3NQFEoSvcuIrTvKVvIXr1-y1Y"
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, ban_group))

    application.run_polling()

if __name__ == "__main__":
    main()
