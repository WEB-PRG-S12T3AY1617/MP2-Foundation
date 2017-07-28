from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item, Course, Tag
from Profile.models import Degree, Office, User
from django.template import loader
from django.urls import reverse


def index(request):
    content = 10
    next_page = 2
    prev_page = 1
    item_list = Item.objects.order_by('-id')[0:int(content)]
    context = {
		'item_list': item_list,
		'next_page': next_page,
		'prev_page': prev_page,
	}
    return render(request, 'Post/baseTemp.html',context)

def home(request):
    request.session["user"] = -1
    content = 10
    next_page = 2
    prev_page = 1
    item_list = Item.objects.order_by('-id')[0:int(content)]
    context = {
		'item_list': item_list,
		'next_page': next_page,
		'prev_page': prev_page,
	}
    return render(request, 'Post/baseTemp.html',context)

def listItem(request):
	content = 10
	current_page = 1
	if request.method == 'POST':
		content = request.POST["content"]
		current_page = int(request.POST["nextPage"])-1
	start = (current_page-1)*10
	item_list = Item.objects.order_by('-id')[start:(start+int(content))]
	context = {
		'item_list': item_list
	}
	return render(request, 'Post/listItem.html',context)

def viewPage(request,page_num):
	num_page = int(page_num);
	start = (num_page -1) *10
	content = start+10
	next_page = int(page_num)+1
	prev_page = int(page_num)-1
	if int(page_num) == 1:
		prev_page = 1
	item_list = Item.objects.order_by('-id')[start:int(content)]
	context = {
		'item_list': item_list,
		'next_page': next_page,
		'prev_page': prev_page,
	}
	return render(request, 'Post/baseTemp.html',context)

def details(request, itemNo):
    data = get_object_or_404(Item, pk=itemNo)
    return render(request, 'Post/itemDetailTemp.html', {"item": data})

def addPost(request):
    courses = Course.objects.all()
    return render(request, 'Post/addPostTemp.html', {"courses":courses})

def addingPost(request):
    user = get_object_or_404(User, pk=request.session['user'])
    answer = request.POST['itemCondition']
    content = 10
    next_page = 2
    prev_page = 1
    item_list = Item.objects.order_by('-id')[0:int(content)]
    context = {
		'item_list': item_list,
		'next_page': next_page,
		'prev_page': prev_page,
	}
    if request.POST['itemOccupation'] == 0:
        course = get_object_or_404(Course, pk = request.POST['selectingCourse'])
        addingPost = Item(item_name=request.POST['itemName'],item_quantity=request.POST['itemQuantity'],item_condition=answer,item_occupation=request.POST['itemOccupation'],item_img=request.POST['pic'],item_userfk=user, item_coursefk=course)
        addingPost.save()
        addPost = Item.objects.all().order_by('-id')[0]
        if request.POST['tag1']:
            addingTag = Tag(tag_word = request.POST['tag1'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag2']:
            addingTag = Tag(tag_word = request.POST['tag2'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag3']:
            addingTag = Tag(tag_word = request.POST['tag3'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag4']:
            addingTag = Tag(tag_word = request.POST['tag4'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag5']:
            addingTag = Tag(tag_word = request.POST['tag5'], tag_itemfk= addPost)
            addingTag.save()
    else:
        addingPost = Item(item_name=request.POST['itemName'],item_quantity=request.POST['itemQuantity'],item_condition=answer,item_occupation=request.POST['itemOccupation'],item_img=request.POST['pic'],item_userfk=user)
        addingPost.save()
        addPost = Item.objects.all().order_by('-id')[0]
        if request.POST['tag1']:
            addingTag = Tag(tag_word = request.POST['tag1'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag2']:
            addingTag = Tag(tag_word = request.POST['tag2'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag3']:
            addingTag = Tag(tag_word = request.POST['tag3'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag4']:
            addingTag = Tag(tag_word = request.POST['tag4'], tag_itemfk= addPost)
            addingTag.save()
        if request.POST['tag5']:
            addingTag = Tag(tag_word = request.POST['tag5'], tag_itemfk= addPost)
            addingTag.save()
    
    return render(request, 'Post/baseTemp.html',context)

def searchItem(request, tagWord):
    tag_list = Tag.objects.filter(tag_word = tagWord).values('tag_itemfk')
    items = Item.objects.all()
    return render(request, 'Post/filterBaseTemp.html', {'item_list': items, 'tag_list':tag_list})

def searchBoxItem(request):
    tagWord = request.POST['searchWord']
    item_list = []
    tag_list = Tag.objects.filter(tag_word = tagWord).values('tag_itemfk')
    items = Item.objects.all()
    return render(request, 'Post/filterBaseTemp.html', {'item_list': items, 'tag_list':tag_list})
