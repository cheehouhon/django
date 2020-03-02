from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Type of pizzas."""
    pizza = models.CharField(max_length=200)
    dated_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.pizza

class Topping(models.Model):
    """Toppings for pizza."""
    name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    dated_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text}"