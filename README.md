# PREGUTECA

## Installation

### Set up the initial database

1. Initialize the database:  
   `python manage.py migrate`
2. Verify that the data from `preguteca_backend/question_library/data/video_data__parsed.json` is correct, if not, run
   the script `parse_video_data.py` from the same folder, ensuring there is a file named `video_data.xlsx` in the
   folder, containing the raw data exported from the Excel with the correct column names.
3. Load the data from `video_data__parsed.json` into the database:  
   `python manage.py load_video_data`
4. Extract Youtube video id and complete the video entries data with it:  
   `python manage.py extract_youtube_id`
5. Generate the missing content with Youtube API:  
   `python manage.py generate_youtube_data`