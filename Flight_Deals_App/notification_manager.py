from telegram import Bot

class NotificationManager:
    """
    A class that handles sending notifications using the Telegram API.

    Args:
        telegram_api (str): The API token for the Telegram bot.
        chat_id (int): The ID of the chat where the notifications will be sent.

    Attributes:
        bot (Bot): An instance of the Telegram Bot class.
        chat_id (int): The ID of the chat where the notifications will be sent.
    """

    class NotificationManager:
        def __init__(self, telegram_api, chat_id):
            """
            Initializes a new instance of the NotificationManager class.

            Args:
                telegram_api (str): The API token for the Telegram bot.
                chat_id (int): The ID of the chat where notifications will be sent.
            """
            self.bot = Bot(token=telegram_api)
            self.chat_id = chat_id

    async def send_message(self, message):
        """
        Sends a message to the specified chat.

        Args:
            message (str): The message to be sent.

        Returns:
            None
        """
        await self.bot.send_message(chat_id=self.chat_id, text=message)
    