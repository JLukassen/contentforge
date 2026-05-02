def normalize_hashtags(raw_hashtags):
    """
    Turn a loose hashtag string into clean hashtag formatting.

    Example:
    "kpop illit music" -> "#kpop #illit #music"
    """
    if not raw_hashtags:
        return ""

    tags = raw_hashtags.replace(",", " ").split()
    cleaned_tags = []

    for tag in tags:
        tag = tag.strip()

        if not tag:
            continue

        if not tag.startswith("#"):
            tag = f"#{tag}"

        cleaned_tags.append(tag)

    return " ".join(cleaned_tags)
