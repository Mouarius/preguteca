import os.path
import re

import numpy as np
import pandas as pd
import unidecode


def main():
    file = os.path.join(os.path.dirname(__file__), "video_data.xlsx")
    videos = pd.read_excel(file)

    def create_category_name(category_name):
        if (
            not category_name
            or category_name is None
            or not isinstance(category_name, str)
        ):
            return ""
        category_name = re.sub("[0-9]+", "", category_name).lower()
        category_name = re.sub("\s", "_", category_name)
        category_name = unidecode.unidecode(category_name)
        return category_name

    def clean_fullname(fullname):
        if not fullname or fullname is None or not isinstance(fullname, str):
            return ""
        fullname = re.sub("\s$", "", fullname)
        fullname = re.sub("[0-9]+", "", fullname)
        fullname = re.sub("\s\(.+\)", "", fullname)
        return fullname

    def is_youtube_url(string):
        if (
            string
            and isinstance(string, str)
            and string.startswith("https://www.youtube.com")
        ):
            return True
        return False

    def clean_url(url):
        if url == "":
            url = np.nan
        return url

    # Replace all none values for fullname
    videos["category_fullname"].fillna(method="ffill", inplace=True)

    # Clean all fullnames
    videos["category_fullname"] = videos["category_fullname"].apply(clean_fullname)

    # Clean all urls
    videos["video_url"] = videos["video_url"].apply(clean_url)
    videos.dropna(subset=["video_url"], inplace=True)

    videos.fillna("", inplace=True)

    # Clean all languages
    videos["language"].replace("-", "", inplace=True)

    videos["category_name"] = videos.iloc[:, 0].apply(create_category_name)

    videos.to_excel("video_data__parsed.xlsx")
    videos.to_json("video_data__parsed.json", orient="records")


if __name__ == "__main__":
    main()
