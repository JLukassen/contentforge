import json
import os
import urllib.error
import urllib.parse
import urllib.request


class TelegramPublishError(Exception):
    """Raised when Telegram publishing cannot complete."""


def publish_to_telegram(text, chat_id=None):
    """
    Publish text to Telegram using the Bot API.

    Required environment variables:
    - TELEGRAM_BOT_TOKEN
    - TELEGRAM_DEFAULT_CHAT_ID, unless chat_id is passed directly
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    target_chat_id = (chat_id or os.getenv("TELEGRAM_DEFAULT_CHAT_ID", "")).strip()

    if not bot_token:
        raise TelegramPublishError("Missing TELEGRAM_BOT_TOKEN in your .env file.")

    if not target_chat_id:
        raise TelegramPublishError("Missing TELEGRAM_DEFAULT_CHAT_ID in your .env file.")

    if not text.strip():
        raise TelegramPublishError("Telegram message text is empty.")

    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = urllib.parse.urlencode(
        {
            "chat_id": target_chat_id,
            "text": text,
            "disable_web_page_preview": "false",
        }
    ).encode("utf-8")

    request = urllib.request.Request(api_url, data=payload, method="POST")

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            raw_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise TelegramPublishError(f"Telegram API error: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise TelegramPublishError(f"Could not connect to Telegram: {exc.reason}") from exc

    data = json.loads(raw_body)

    if not data.get("ok"):
        raise TelegramPublishError(f"Telegram rejected the message: {data}")

    result = data.get("result", {})
    chat = result.get("chat", {})

    return {
        "message_id": str(result.get("message_id", "")),
        "chat_id": str(chat.get("id", target_chat_id)),
    }
