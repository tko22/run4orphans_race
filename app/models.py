# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime



class Run(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=2017)
    run_code = models.CharField(max_length=5)

    def __str__(self):
        return self.run_code


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=5)
    run_id = models.ForeignKey(Run ,on_delete=models.CASCADE)
    over_18 = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    # 1 - Youth S | 2 - Youth M | 3 - Youth L | 4 - Adult S | 5 - Adult M | 6 - Adult L | 7 - Adult XL
    shirt_size = models.IntegerField(default=5)
    # True - male, False - Female
    gender = models.BooleanField(default=True)
    sign_up_date = models.DateTimeField(default=datetime.date.today)
    minor_name = models.CharField(max_length=30, null=True)
    minor_bday = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name


