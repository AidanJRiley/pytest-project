def estimate_reading_time(text):
    seconds = round(len(text.split()) /200 * 60)
    if seconds < 60:
        if seconds == 1:    
            return f"{seconds} second"
        return f"{seconds} seconds"
    remainder = seconds % 60
    minutes = round((seconds - remainder)/60)
    if minutes == 1 and remainder > 1:
        return f"{minutes} minute {remainder} seconds"
    if minutes == 1 and remainder == 0:
        return f"{minutes} minute"
    if minutes == 1 and remainder == 1:
        return f"{minutes} minute {remainder} second"
    if minutes > 1 and remainder > 1:
        return f"{minutes} minutes {remainder} seconds"
    if minutes > 1 and remainder == 0:
        return f"{minutes} minutes"
    if minutes > 1 and remainder == 1:
        return f"{minutes} minutes {remainder} second"