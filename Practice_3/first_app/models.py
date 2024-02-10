from django.db import models

# Create your models here.

class ExampleModels(models.Model):
    address = models.CharField(max_length=30)
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()
    integer_field = models.IntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()