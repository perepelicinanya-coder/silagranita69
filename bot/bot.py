import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

SITE_URL = "http://silagranita-69.ru"
KITCHENS_URL = f"{SITE_URL}/kuhni/"
MEMORIALS_URL = f"{SITE_URL}/pamyatniki/"
VK_URL = "https://vk.com/id1073057068"
PHONE_PRIMARY = "+7 920 155-79-71"
PHONE_SECONDARY = "+7 996 940-33-80"


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📐 Рассчитать заказ", callback_data="calc"),
                InlineKeyboardButton("🧱 Каталог изделий", callback_data="catalog"),
            ],
            [
                InlineKeyboardButton("🍽 Кухонные столешницы", callback_data="kitchens"),
                InlineKeyboardButton("🪦 Памятники", callback_data="memorials"),
            ],
            [
                InlineKeyboardButton("📘 Гайд по выбору камня", callback_data="guide"),
            ],
            [
                InlineKeyboardButton("🌐 Открыть сайт", url=SITE_URL),
                InlineKeyboardButton("📞 Связаться с мастером", callback_data="contacts"),
            ],
        ]
    )


def back_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
            [InlineKeyboardButton("🌐 Открыть сайт", url=SITE_URL)],
        ]
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    source = context.args[0] if context.args else ""
    intro = "Здравствуйте! Я помощник «Сила Гранита»."

    if source == "stone_guide":
        intro = (
            "Здравствуйте! Вы перешли по QR-коду «Сила Гранита».\n\n"
            "Помогу посмотреть изделия, выбрать камень или быстро подготовить расчёт."
        )

    await update.message.reply_text(
        f"{intro}\n\nЧто хотите сделать?",
        reply_markup=main_menu(),
    )


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "menu":
        await query.edit_message_text("Что хотите сделать?", reply_markup=main_menu())
        return

    if data == "catalog":
        await query.edit_message_text(
            "🧱 Каталог изделий «Сила Гранита»\n\n"
            "Мы изготавливаем изделия из натурального камня, кварца и акрила:\n"
            "• кухонные столешницы;\n"
            "• подоконники, ступени и плитку;\n"
            "• памятники и мемориальные комплексы;\n"
            "• индивидуальные изделия по эскизу.\n\n"
            "Откройте сайт, чтобы посмотреть основные направления.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🌐 Смотреть сайт", url=SITE_URL)],
                    [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
                ]
            ),
        )
        return

    if data == "calc":
        await query.edit_message_text(
            "📐 Предварительный расчёт\n\n"
            "Чтобы мы быстро посчитали стоимость, отправьте в этот чат:\n"
            "1. Что нужно изготовить: столешница, памятник, ступени, подоконник и т.д.\n"
            "2. Примерные размеры.\n"
            "3. Фото, эскиз или пример, если есть.\n"
            "4. Ваш город и удобный телефон для связи.\n\n"
            "Мастер посмотрит задачу и подскажет ориентир по цене и срокам.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📞 Контакты мастера", callback_data="contacts")],
                    [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
                ]
            ),
        )
        return

    if data == "guide":
        await query.edit_message_text(
            "📘 Короткий гайд по выбору камня\n\n"
            "Натуральный гранит — прочный, долговечный, хорошо подходит для памятников, ступеней, подоконников и фасадных элементов.\n\n"
            "Кварцевый агломерат — практичный вариант для кухонных столешниц: устойчив к влаге, пятнам и ежедневной нагрузке.\n\n"
            "Акриловый камень — подходит для сложных форм, бесшовных решений и современных интерьеров.\n\n"
            "Если сомневаетесь — отправьте фото задачи, и мы подскажем лучший материал.",
            reply_markup=back_menu(),
        )
        return

    if data == "kitchens":
        await query.edit_message_text(
            "🍽 Кухонные столешницы\n\n"
            "Столешницы от производителя на 20–30% дешевле, чем в салонах.\n"
            "Из кварца, акрила или натурального камня — от 11 500 ₽/м².\n\n"
            "Можно отправить размеры кухни прямо сюда — подготовим предварительный расчёт.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🍽 Открыть страницу столешниц", url=KITCHENS_URL)],
                    [InlineKeyboardButton("📐 Рассчитать заказ", callback_data="calc")],
                    [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
                ]
            ),
        )
        return

    if data == "memorials":
        await query.edit_message_text(
            "🪦 Памятники и мемориальные изделия\n\n"
            "Изготавливаем памятники из натурального гранита, мемориальные комплексы и индивидуальные решения.\n\n"
            "Также можем обсудить уникальный памятник из эпоксидной смолы с наполнением: букетом, памятными вещами или индивидуальной композицией.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🪦 Открыть страницу памятников", url=MEMORIALS_URL)],
                    [InlineKeyboardButton("📐 Получить эскиз/расчёт", callback_data="calc")],
                    [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
                ]
            ),
        )
        return

    if data == "contacts":
        await query.edit_message_text(
            "📞 Контакты «Сила Гранита»\n\n"
            f"Телефон 1: {PHONE_PRIMARY}\n"
            f"Телефон 2: {PHONE_SECONDARY}\n"
            f"ВКонтакте: {VK_URL}\n\n"
            "Можете написать сюда в бот: что нужно сделать, размеры и фото. Мы вернёмся с расчётом.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("VK", url=VK_URL)],
                    [InlineKeyboardButton("🌐 Открыть сайт", url=SITE_URL)],
                    [InlineKeyboardButton("⬅️ В меню", callback_data="menu")],
                ]
            ),
        )
        return


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Я получил сообщение. Чтобы выбрать действие, нажмите кнопку меню ниже.",
        reply_markup=main_menu(),
    )


def run() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN environment variable")

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_menu))

    logger.info("Bot started")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    run()
