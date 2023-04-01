from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=228)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
