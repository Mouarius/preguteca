def iso8601_to_duration(duration_str):
    # Remove the 'P' prefix from the duration string
    duration_str = duration_str.replace("PT", "")

    # Initialize the duration components
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    # Parse the duration components
    if "D" in duration_str:
        days_str, duration_str = duration_str.split("D")
        days = int(days_str)
    if "H" in duration_str:
        hours_str, duration_str = duration_str.split("H")
        hours = int(hours_str)
    if "M" in duration_str:
        minutes_str, duration_str = duration_str.split("M")
        minutes = int(minutes_str)
    if "S" in duration_str:
        seconds_str = duration_str[:-1]
        seconds = int(seconds_str)

    # Format the duration as HH:MM:SS
    duration = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return duration
