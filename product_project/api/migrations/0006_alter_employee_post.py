# Generated by Django 4.0.1 on 2022-09-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_employee_boss_alter_boss_post_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Post',
            field=models.CharField(choices=[('Finance Manager', 'Finance Manager'), ('Product Manager', 'Product Manager'), ('IT Manager', 'IT Manager'), ('Finance Director', 'Finance Director'), ('Product Director', 'Product Director'), ('IT Director', 'IT Director')], default='MANAGER', max_length=50),
        ),
    ]
