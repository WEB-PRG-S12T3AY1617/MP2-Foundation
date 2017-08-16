from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item, Course, Tag
from django.template import loader
from django.urls import reverse

def index(request):
	item_list = Item.objects.order_by('-id')[:5]
	context = {
		'item_list': item_list
	}
	return render(request, 'Post/baseTemp.html',context)