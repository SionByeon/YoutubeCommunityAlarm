# Youtube Community Alarm ([pypi](https://pypi.org/project/youtube-community-alarm/))

- Python3 interface for scheduling crontab to retrieve YouTube community posts and send notifications
- Periodically check for new posts, and if any are found, send a notification to macOS.


## Installing
install youtube-community-alarm
```bash
$ pip install youtube-community-alarm
```


## Using
The **default** setting is to check for posts made within the last `10` minutes, using the corresponding cron expression `*/10 * * * *`.
<br> Here is the default usage:
```python
>>> from youtubeCommunityAlarm import CrontabRegister

>>> channel_id = "@my_channel_id"
>>> cr = CrontabRegister(channel_id=channel_id)
>>> cr.register_crontab()
```

If you want to control the crontab settings, you can do so by passing the following arguments:
```python
>>> from youtubeCommunityAlarm import CrontabRegister

>>> channel_id = "@my_channel_id"
# Check for new posts until those posted within the last 30 minutes using a cron expression "30 * * * *"
>>> cr = CrontabRegister(channel_id=channel_id, time_limit_for_checking_in_minutes=30, cron_expression="30 * * * *")
>>> cr.register_crontab()
```


## Checking Crontab
Check if the crontab is registered by running the following command:
```bash
crontab -l

# Default
*/10 * * * * /usr/bin/python3 /path/youtube_community_alarm.py --channel_id @my_channel_id >> /path/log.log 2>&1

# Custom
30 * * * * /usr/bin/python3 /path/youtube_community_alarm.py --channel_id @my_channel_id --time_limit_for_checking_in_minutes 30 >> /path/log.log 2>&1
```

## Crontab Error Case

If you encounter errors from the crontab, you can refer to [this troubleshooting guide](https://23log.tistory.com/171)









