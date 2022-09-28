from django.db import models

choices_post = (("Finance Manager", "Finance Manager"),
            ("Product Manager", "Product Manager"),
            ("IT Manager", "IT Manager"),
             ("Finance Director", "Finance Director"),
            ("Product Director", "Product Director"),
            ("IT Director", "IT Director"))

choices_boss = ( ("Finance Director", "Finance Director"),
            ("Product Director", "Product Director"),
            ("IT Director", "IT Director"),
            ("General Director", "General Director"))

class Boss(models.Model):
    Surename_Boss = models.CharField(max_length=50)
    Name_Boss = models.CharField(max_length=50)
    Post_Boss = models.CharField(choices=choices_boss, max_length=50)


    def __str__(self):
        return '%s : %s' % (self.Name_Boss, self.Post_Boss)
    

class Employee(models.Model):
    Surename_empl = models.CharField( max_length=50)
    Name_empl = models.CharField( max_length=50)
    Post = models.CharField(choices=choices_post, max_length=50, default='MANAGER')
    Date_employment = models.DateField(auto_now_add=True)
    Salary = models.PositiveIntegerField(default=0)
    Boss = models.ForeignKey(Boss, on_delete=models.CASCADE)

