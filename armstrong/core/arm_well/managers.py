import datetime
from django.db import models


class WellManager(models.Manager):
    def get_current(self, title):
        now = datetime.datetime.now()
        queryset = self.filter(title=title, pub_date__lte=now) \
            .exclude(expires__lte=now, expires__isnull=False)
        return queryset[0]