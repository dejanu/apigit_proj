# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
import feedparser
#import the app forms
from appone import forms
from appone.models import DevProfile


def index(request):
    """view loads index template after form is valid loads git info"""
    # forms usage
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        print (form.errors)
        if form.is_valid():
            #manually create object in models
            obj = DevProfile()
            # take the user name from form
            user_name = form.cleaned_data['name']
            #save the object in db
            obj.name = user_name
            obj.save()
            response = requests.get('https://api.github.com/users/' + user_name)
            try:
                user_data = response.json()
            except:
                #no json object could be decoded
                return render(request, 'appone/index.html')
            return render(request, 'appone/gitinfo.html', {
                'location': user_data['location'],
                'bio': user_data['bio'],
                'no_of_repos': user_data['public_repos'],
                'git_member_since': user_data['created_at'],
                'followers': user_data['followers'],
                'following': user_data['following'],
                'git_user_name':user_data['login'],
            })
        #form is invalid
        return render(request,'appone/index.html')
    #the first thing that is returned
    return render(request,'appone/index.html',{'form':form})


def more_info(request):
    """read object from db and call api"""
    query_set = DevProfile.objects.all()
    #thake the last element from the db
    last_value_added = str(query_set[len(query_set)-1].name)
    #print (last_value_added)
    """view for API calls"""
    response = requests.get('https://api.github.com/users/'+last_value_added+'/repos')
    repo_data = response.json()
    return render(request, 'appone/more.html', {
                'all_data':repo_data,
                })

def stackoverflow(request):
    """get RSS feed based on user ID"""
    form = forms.FormStackOverflow()
    if request.method == 'POST':
        form = forms.FormStackOverflow(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['id']
            #get RSS feed 7013263
            data =feedparser.parse('https://stackoverflow.com/feeds/user/'+user_id)
            #data dict
            data_dict = data.feed
            return render(request,'appone/stack.html',{'dictionar':data_dict.values()})
    return render(request,'appone/stack.html',{'form':form})