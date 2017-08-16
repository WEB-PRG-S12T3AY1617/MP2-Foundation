from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item, Course, Tag, Offer
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
    startIndex=0
    if request.method == 'POST':
        content = request.POST["content"]
        current_page = int(request.POST["nextPage"])-1
        startIndex = int(request.POST['start'])
    item_list = Item.objects.order_by('-id')[startIndex:(startIndex+int(content))]
    context = {
        'item_list': item_list
    }
    return render(request, 'Post/listItem.html',context)

def viewPage(request,page_num,start_num):
	num_page = int(page_num);
	start = (num_page -1) *int(start_num)
	content = start+int(start_num)
	next_page = int(page_num)+1
	prev_page = int(page_num)-1
	if int(page_num) == 1:
		prev_page = 1
	item_list = Item.objects.order_by('-id')[start:int(content)]
	context = {
		'item_list': item_list,
		'next_page': next_page,
		'prev_page': prev_page,
        'start': start,
        'numOfItems': start_num,
	}
	return render(request, 'Post/baseTemp.html',context)

def details(request, itemNo):
    data = get_object_or_404(Item, pk=itemNo)
    offer_list = Offer.objects.filter(offer_itemfk = data.id).exclude(offer_status = 1).order_by('id')
    data2=None
    item_list=None
    myOffer = None
    if request.session["user"] != -1:
        data2 = get_object_or_404(User, pk=request.session['user'])
        item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0).order_by('-id')
        myOffer = Offer.objects.filter(offer_itemfk = itemNo, offer_clientfk = data2.id).exclude(offer_status = 1).order_by('-id')
        if data2.id == data.item_userfk.id:
            return render(request, 'Post/myItemDetTemp.html', {"item": data,"offerList":offer_list,"itemList":item_list,})
        else:
            return render(request, 'Post/updateOfferTemp.html', {"item": data,"offerList":myOffer,"itemList":item_list,})
    else:
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

def searchByOccupation(request, tagOccupation):
    item_list = Item.objects.filter(item_occupation = tagOccupation)
    return render(request, 'Post/occupationBaseTemp.html', {'item_list': item_list})

def searchByCondition(request, tagCondition):
    item_list = Item.objects.filter(item_condition = tagCondition)
    return render(request, 'Post/conditionBaseTemp.html', {'item_list': item_list})

def addingOffer(request):
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0)
    user = get_object_or_404(User, pk=request.session['user'])
    currentItem = get_object_or_404(Item, pk = request.POST['currentItemForOffer'])
    myOffer = Offer.objects.filter(offer_itemfk = currentItem.id, offer_clientfk =user.id).exclude(offer_status = 1).order_by('-id')
    if request.POST['typeOffer'] == '1':
        exchangingItem = get_object_or_404(Item, pk = request.POST['exchangingItem'])
        addingOffer = Offer(offer_itemfk=currentItem, offer_type=request.POST['typeOffer'], offer_clientfk=user, offer_itemexfk= exchangingItem, offer_status='0')
        addingOffer.save()
    else:
        addingOffer = Offer(offer_itemfk=currentItem, offer_type=request.POST['typeOffer'], offer_clientfk=user, offer_cash=request.POST['itemQuantity'], offer_status='0')
        addingOffer.save()
    return render(request, 'Post/updateOfferTemp.html',{"item": currentItem,"itemList":item_list, "offerList":myOffer})

def updatingOffer(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['updatingThisOffer'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0)
    user = get_object_or_404(User, pk=request.session['user'])
    currentItem = get_object_or_404(Item, pk = request.POST['currentItemForOffer'])
    myOffer = Offer.objects.filter(offer_itemfk = currentItem.id, offer_clientfk =user.id).exclude(offer_status = 1).order_by('-id')
    if request.POST['updatingOfferType'] == '1':
        exchangingItem = get_object_or_404(Item, pk = request.POST['updatingExchangeItem'])
        updatingOffer.offer_type=request.POST['updatingOfferType']
        updatingOffer.offer_itemexfk= exchangingItem
        updatingOffer.save()
    else:
        updatingOffer.offer_type=request.POST['updatingOfferType']
        updatingOffer.offer_cash=request.POST['updatingQuantity']
        updatingOffer.save()
        
    return render(request, 'Post/updateOfferTemp.html',{"item": currentItem,"itemList":item_list, "offerList":myOffer})

def cancellingOffer(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['deleteThisOffer'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0)
    user = get_object_or_404(User, pk=request.session['user'])
    currentItem = get_object_or_404(Item, pk = request.POST['currentItemForOffer'])
    myOffer = Offer.objects.filter(offer_itemfk = currentItem.id, offer_clientfk =user.id).exclude(offer_status = 1).order_by('-id')
    updatingOffer.offer_status='1'
    updatingOffer.save()
    return render(request, 'Post/updateOfferTemp.html',{"item": currentItem,"itemList":item_list, "offerList":myOffer})

def acceptOffer(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['acceptThisOfferP'])
    data = get_object_or_404(Item, pk=request.POST['acceptThisOffer'])
    offer_list = Offer.objects.filter(offer_itemfk = data.id).exclude(offer_status = 1).order_by('id')
    data2=None
    item_list=None
    myOffer = None
    data2 = get_object_or_404(User, pk=request.session['user'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0).order_by('-id')
    myOffer = Offer.objects.filter(offer_itemfk = request.POST['acceptThisOffer'], offer_clientfk = data2.id).exclude(offer_status = 1).order_by('-id')
    updatingOffer.offer_status='2'
    updatingOffer.offer_comment=request.POST['acceptedCommentTextarea']
    updatingOffer.save()
    return render(request, 'Post/myItemDetTemp.html', {"item": data,"offerList":offer_list,"itemList":item_list,})

def rejectOffer(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['rejectThisOfferP'])
    data = get_object_or_404(Item, pk=request.POST['rejectThisOffer'])
    offer_list = Offer.objects.filter(offer_itemfk = data.id).exclude(offer_status = 1).order_by('id')
    data2=None
    item_list=None
    myOffer = None
    data2 = get_object_or_404(User, pk=request.session['user'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0).order_by('-id')
    myOffer = Offer.objects.filter(offer_itemfk = request.POST['rejectThisOffer'], offer_clientfk = data2.id).exclude(offer_status = 1).order_by('-id')
    updatingOffer.offer_status='3'
    updatingOffer.offer_comment = request.POST['rejectedCommentTextarea']
    updatingOffer.save()
    return render(request, 'Post/myItemDetTemp.html', {"item": data,"offerList":offer_list,"itemList":item_list,})

def acceptOffer1(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['acceptThisOfferP'])
    data = get_object_or_404(Item, item_name=request.POST['acceptThisOffer'])
    offer_list = Offer.objects.filter(offer_itemfk = data.id).exclude(offer_status = 1).order_by('id')
    data2=None
    item_list=None
    myOffer = None
    data2 = get_object_or_404(User, pk=request.session['user'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0).order_by('-id')
    myOffer = Offer.objects.filter(offer_itemfk__item_name = request.POST['acceptThisOffer'], offer_clientfk = data2.id).exclude(offer_status = 1).order_by('-id')
    updatingOffer.offer_status='2'
    updatingOffer.offer_comment=request.POST['acceptedCommentTextarea']
    updatingOffer.save()
    return render(request, 'Post/myItemDetTemp.html', {"item": data,"offerList":offer_list,"itemList":item_list,})

def rejectOffer1(request):
    updatingOffer = get_object_or_404(Offer,pk=request.POST['rejectThisOfferP'])
    data = get_object_or_404(Item, item_name =request.POST['rejectThisOffer'])
    offer_list = Offer.objects.filter(offer_itemfk = data.id).exclude(offer_status = 1).order_by('id')
    data2=None
    item_list=None
    myOffer = None
    data2 = get_object_or_404(User, pk=request.session['user'])
    item_list = Item.objects.filter(item_userfk=request.session['user'],item_status=0).order_by('-id')
    myOffer = Offer.objects.filter(offer_itemfk__item_name = request.POST['rejectThisOffer'], offer_clientfk = data2.id).exclude(offer_status = 1).order_by('-id')
    updatingOffer.offer_status='3'
    updatingOffer.offer_comment = request.POST['rejectedCommentTextarea']
    updatingOffer.save()
    return render(request, 'Post/myItemDetTemp.html', {"item": data,"offerList":offer_list,"itemList":item_list,})