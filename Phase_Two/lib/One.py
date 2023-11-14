def estimate_reading_time(text):
    seconds = round(len(text.split()) /200 * 60)
    
    if seconds < 60:
        if seconds == 1:    
            return f"{seconds} second"
        return f"{seconds} seconds"
    remainder = seconds % 60
    minutes = round((seconds - remainder)/60)
    
    if minutes > 1:
        minutes_result = f"{minutes} minutes"
    elif minutes == 1:
        minutes_result = f"{minutes} minute"
    
    if remainder > 1:
        seconds_result = f"{remainder} seconds"
    elif remainder == 1:
        seconds_result = f"{remainder} second"
    
    if remainder == 0:
        return minutes_result
    return f"{minutes_result} {seconds_result}"