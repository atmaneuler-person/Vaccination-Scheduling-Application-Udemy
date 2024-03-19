from django.db import models
from center.models import Center
from vaccine.models import Vaccine
from django.contrib.auth import get_user_model # 장고에서 유저가져오는 법 아래 Use = 까지, 암기용
# from campaign.models import Campaign --> 허용하지 않는다.

# Create your models here.
User = get_user_model()

class Campaign(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    agents = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        # return self.center.name + " | " + self.vaccine.name # 두 개 방식 모두 사용가능
        return str(self.vaccine.name).upper() + " | " + str(self.center.name).upper()
    
    
class Slot(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    start_time = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    max_capacity = models.IntegerField(default=0, null=True, blank=True)
    reserved = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.date) + " | " + str(self.start_time) + " to " + str(self.end_date)
        
        
        
    