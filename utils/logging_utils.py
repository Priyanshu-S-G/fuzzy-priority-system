import datetime

def log(message: str, level: str = "INFO") -> None:
    """
    Print timestamped log message.

    Args:
        message: text to log
        level:   INFO / WARNING / ERROR
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [{level}] {message}")