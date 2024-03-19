from django.db import models
from vaccine.models import Vaccine

# Create your models here.
class Center(models.Model):
    name = models.CharField("Center Name", max_length=124) # 255가 최대
    address = models.TextField(max_length=500) # 1024가 최대
   
    
    def __str__(self):
        return self.name  # 관리자화면에 Name을 리스트로 디스플레이한다.
    
class Storage(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    Vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    total_quantity = models.IntegerField(default=0)
    booked_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.center.name + " | " + self.Vaccine.name
    