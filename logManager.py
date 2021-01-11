from datetime import datetime
def getTimestamp():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time