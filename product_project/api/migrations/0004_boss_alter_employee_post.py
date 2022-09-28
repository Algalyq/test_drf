# Generated by Django 4.0.1 on 2022-09-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_employee_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surename_Boss', models.CharField(max_length=50)),
                ('Name_Boss', models.CharField(max_length=50)),
                ('Post_Boss', models.CharField(max_length=50, verbose_name=(('Finance Director', 'Finance Director'), ('Product Director', 'Product Director'), ('IT Director', 'IT Director'), ('General Director', 'General Director')))),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='Post',
            field=models.CharField(choices=[('Finance Manager', 'Finance Manager'), ('Product Manager', 'Product Manager'), ('IT Manager', 'IT Manager')], default='MANAGER', max_length=50),
        ),
    ]