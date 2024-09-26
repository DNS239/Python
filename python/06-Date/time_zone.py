from datetime import datetime, timezone, timedelta

date = datetime.now(timezone(timedelta(hours=2)))
date2 = datetime.now(timezone(timedelta(hours=4)))

print(date)
print(date2)