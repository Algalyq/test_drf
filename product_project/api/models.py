from django.db import models

choices_post = (("MANAGER", "Manager"),
            ("FINANCE DIRECTOR", "Finance Director"),
            ("PRODUCT DIRECTOR", "Product Director"),
            ("IT DIRECTOR", "IT Director"),
            ("GENERAL DIRECTOR", "General Director"))


class Employee(models.Model):
    Surename_empl = models.CharField( max_length=50)
    Name_empl = models.CharField( max_length=50)
    Post = models.CharField(choices=choices_post, max_length=50, default='MANAGER')
    Date_employment = models.DateField(auto_now_add=True)
    Salary = models.PositiveIntegerField(default=0)

