from django.db import models
from django.utils.crypto import get_random_string
import datetime
# Create your models here.
class Privilege(models.Model):
    def generate_string():
        return get_random_string(12).upper()
    privilege_owner = models.CharField(max_length=12, default=generate_string , editable=False)
    check_count = models.BigIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def checked_today(self):
        return datetime.datetime.today().date() == self.updated_at.date()

    def check_privilege(self):
        print("updating bitch") 
        print(datetime.datetime.today().date())
        print(self.updated_at.date())
        if not self.checked_today():
            self.check_count += 1
            print("UPDATED BITCH")
            return True
        return False
    
