from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from taggit.managers import TaggableManager


class Retreat(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    image = models.URLField()
    tag = TaggableManager()
    duration = models.IntegerField()

    class Meta:
        ordering = ["id", "date"]

    def __str__(self):
        return f"{self.id} {self.title}"


class Booking(models.Model):
    # Pending if payment not initiated and Successfull when money received
    payment_choices = {"PE": "Pending", "SU": "Successful"}

    date = models.DateField()
    payment_detail = models.CharField(
        max_length=2, choices=payment_choices, default=payment_choices["PE"]
    )
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        book = Booking.objects.filter(
            Q(user=self.user.id) & Q(retreat=self.retreat.id)
        )
        print("Book",book, len(book))
        if len(book) > 0:
            raise Exception("Booking already done")
        user = User.objects.get(pk=self.user.id)
        
        if not user:
            raise ObjectDoesNotExist('User does not exist')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.id}"
