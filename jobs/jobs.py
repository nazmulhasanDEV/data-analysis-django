# job schedular for monitoring our paid and trial members. After the the duration, it will automatically made the user free user(while time is up)

import datetime
from user.models import Account

def monitorMembeshipStatus():
    users = Account.objects.filter(is_paid_member=True)
    for user in users:
        if user:
            timeNow = datetime.datetime.now().timestamp() * 1000
            membershipEndingDate = user.membershipEndingDate.timestamp() * 1000
            if membershipEndingDate <= timeNow:
                user.is_paid_member = False
                user.save()
