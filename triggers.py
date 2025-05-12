def load_blacklist(path="blacklist.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Файл {path} не найден.")
        return []

def is_triggered(text, blacklist):
    text = text.lower()
    return any(word in text for word in blacklist)
