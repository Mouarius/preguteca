import re
from unidecode import unidecode


def iso8601_to_duration(duration_str):
    # Remove the 'P' prefix from the duration string
    duration_str = duration_str.replace("PT", "")

    # Initialize the duration components
    hours = 0
    minutes = 0
    seconds = 0

    # Parse the duration components
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


def to_snake_case(string: str) -> str:
    string = unidecode(string)
    string = (
        re.sub(r"(?<=[a-z])(?=[A-Z])|[^a-zA-Z]", " ", string).strip().replace(" ", "_")
    )
    return "".join(string.lower())
