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
    minor_name = models.CharField(max_length=30, null=True,blank=True)
    minor_bday = models.CharField(max_length=30, null=True,blank=True)
    page_text = models.CharField(max_length=2000,default="We are so blessed to be healthy, have a family, a job and be able to pursue the American Dream! Millions of orphans living in poverty, hunger and loneliness. Light & Love Home teams up with the Church of San Francisco, Oakland, Sacramento to support the orphans. We are so enthusiastic to see that many orphans are taken care by the children homes in the developing countries. We are very grateful for every dollar that you donate! Without you, we won't be able to share the joy and love with so many orphans! We may not be able to solve the global problem of the orphans, but to the one that we help, his/her life has been changing with hope & love. Please support our runners to run for the orphans and for the community! Your donation is greatly appreciated!")


    def __str__(self):
        return self.first_name + " " + self.last_name


