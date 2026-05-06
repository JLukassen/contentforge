def format_for_x(master_text):
    """
    Create a short X-style version of the master post.
    """
    max_length = 280

    if len(master_text) <= max_length:
        return master_text

    return master_text[:277].rstrip() + "..."


def format_for_reddit(title, master_text):
    """
    Create a Reddit title/body pair.
    """
    reddit_title = title[:300]
    reddit_body = master_text

    return reddit_title, reddit_body


def format_for_instagram(master_text, hashtags=""):
    """
    Create an Instagram caption with optional hashtags.
    """
    caption = master_text.strip()

    if hashtags:
        caption += "\n\n" + hashtags.strip()

    return caption


def format_for_telegram(master_text, hashtags=""):
    """
    Create a Telegram message with optional hashtags.

    Telegram messages support longer text than X, but this keeps the output
    inside Telegram's 4096 character message limit.
    """
    max_length = 4096
    message = master_text.strip()

    if hashtags:
        message += "\n\n" + hashtags.strip()

    if len(message) <= max_length:
        return message

    return message[:4093].rstrip() + "..."
