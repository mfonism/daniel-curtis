from django.db import models


class WantToSee(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField("What would you like to see on Daniel Curtis?")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Prospective Customer's Wish"
        verbose_name_plural = "Prospective Customers' Wishes"

    def __str__(self):
        return (
            f"Fullname: {self.fullname}\nEmail: {self.email}\n"
            f"Message: {self.message}\nDate: {self.date}"
        )
