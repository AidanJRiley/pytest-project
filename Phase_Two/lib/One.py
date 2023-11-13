def estimate_reading_time(text):
    seconds = int(len(text.split()) /200 * 60)
    if seconds < 60:
        if seconds == 1:    
            return f"{seconds} second"
        return f"{seconds} seconds"
    remainder = seconds % 60
    minutes = int((seconds - remainder)/60)
    if minutes == 1 and remainder >= 1:
        return f"{minutes} minute {remainder} seconds"
    if minutes == 1 and remainder == 0:
        return f"{minutes} minute"