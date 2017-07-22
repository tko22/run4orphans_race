# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random
import string
import traceback

from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Run, User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse("index")

def run(request, run_code):
    run = get_object_or_404(Run,run_code=run_code)
    return render(request, 'app/run.html', {
        'run':run
    })
def signup(request,run_code):
    run = get_object_or_404(Run, run_code=run_code)
    return render(request, 'app/signup.html', {
        'run': run
    })
def user(request, user_id):
    print user_id
    user = get_object_or_404(User, user_id=user_id)

    return render(request, 'app/user.html', {
        'user':user
    })

def runner(request):
    run = get_object_or_404(Run, run_code='lmr')
    return render(request, 'app/runner.html', {
        'run':run,
        'users':run.user_set.all()
    })

@login_required
def runnerinfo(request,run_code):
    run = get_object_or_404(Run, run_code=run_code)
    return render(request, 'app/runnerinfo.html',{
        'run': run
    })
def registeruser(request):
    ret = {'status': 'success'}
    try:
        data = request.body
        jsondata = json.loads(data)
        code = jsondata['code']
        try:
            run = Run.objects.get(run_code=code)
        except (Exception):
            print 'run doesnt exist'
            ret['status'] = 'failed'
            ret['message'] = 'cant get run'
            return JsonResponse

        first_name = jsondata['fname']
        last_name = jsondata['lname']
        email = jsondata["email"]
        phone = jsondata['phone']
        address = jsondata['address']
        over_eighteen = jsondata["over_eighteen"]
        under_eighteen = jsondata["under_eighteen"]
        size = jsondata["tshirt_size"]
        gender = jsondata["gender"]
        user_id = randomcode()
        if under_eighteen == True and over_eighteen == False:
            minor_name = jsondata["minor_name"]
            minor_bday = jsondata["minor_bday"]
            user = run.user_set.create(first_name=first_name,last_name=last_name,email=email,telephone=phone,
                                       address=address,over_18=False,shirt_size=size,gender=gender,
                                       minor_name=minor_name,minor_bday=minor_bday,user_id=user_id)
            user.save()
        elif under_eighteen == False and over_eighteen == True:
            user = run.user_set.create(first_name=first_name,last_name=last_name,email=email,telephone=phone,
                                       address=address,over_18=True,shirt_size=size,gender=gender,user_id=user_id)
            user.save()
        else:
            ret['status'] = 'failed'
            ret['message'] = 'Please provide minor information'
            return JsonResponse(ret)
        run.save()

    except (Exception):
        ret['status'] = 'failed'
        print traceback.print_exc()
    return JsonResponse(ret)

def randomcode():
   return ''.join(random.choice(string.lowercase) for i in range(5))
