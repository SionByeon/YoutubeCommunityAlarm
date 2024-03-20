import argparse
import re
import os
from youtube_community import YoutubeCommunity, REGEX

DEFAULT_TIME_LIMIT_IN_MINUTES = 10


class YoutubeCommunityAlarm(YoutubeCommunity):
    def __init__(self, channel_id, time_limit_in_minutes=None, time_limit_in_hours=None):
        super().__init__(channel_id)
        self.time_limit_in_minutes = time_limit_in_minutes
        self.time_limit_in_hours = time_limit_in_hours

        if self.time_limit_in_minutes is None and self.time_limit_in_hours is None:
            self.time_limit_in_minutes = DEFAULT_TIME_LIMIT_IN_MINUTES


    def scrap_and_alert_if_new_message(self):
        criterion_value = self.time_limit_in_hours if self.time_limit_in_hours is not None else self.time_limit_in_minutes
        criterion_regex = REGEX["HOUR_TIME_PATTERN"] if self.time_limit_in_hours is not None else REGEX["MINUTE_TIME_PATTERN"]

        posts = self.get_all_posts_with_time()
        for time, text in posts:
            match = re.search(criterion_regex, time)
            if match:
                n = match.group(1)
                if int(n) <= criterion_value:
                    text = f"{time} \n {text} \n\n"
                    os.system(f"osascript -e 'display notification \"{text}\" with title \"{time}\"'")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--channel_id', type=str, help='Channel ID')

    args = parser.parse_args()

    if args.channel_id is not None:
        ycpa = YoutubeCommunityAlarm(channel_id=args.channel_id)
        ycpa.scrap_and_alert_if_new_message()
    else:
        print("Please provide a channel_id.")
        exit(1)

