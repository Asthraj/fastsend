from django.db import models
from twilio.rest import Client
# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')



# Create your models here.


class sendsms(models.Model):
    fname = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.fname

    def save(self, *args, **kwargs):
        # if self.message >= 70:
            account_sid = 'AC439af5efeef2bea045d7fbbdbedd27d3'
            auth_token = '81726d82eb0c151ed177b351e7c912e2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                messaging_service_sid='MG3fd1368f1ef7561c0b6e68bdcac2df9c',
                body=f"Congratulations {self.fname}, welcome to {self.message}",
                # from_='+12019924209',
                to='+917067041607')
        # return super().save(*args, **kwargs)