from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Degree, Office, User
from Post.models import Item
from django.template import loader
from django.urls import reverse

def viewProfile(request, userID):
	user = get_object_or_404(User, pk = userID)
	item_list = Item.objects.filter(item_userfk = userID).order_by('-id')[0:10]
	context={
		'user': user,
		'item_list':item_list,
	}
	return render(request, 'Profile/profTemp.html', context)

def signUp(request):
    course_list = Degree.objects.all()
    office_list = Office.objects.all()
    context={
		'office': office_list,
		'courses':course_list,
	}
    return render(request, 'Profile/signUpTemp.html', context)

def justSignedUp(request):
    if request.POST['newOccupation'] == '0':
        course_list = get_object_or_404(Degree, pk = request.POST['selectingCourse'])
        addingUser = User(user_name=request.POST['newName'],user_username=request.POST['newUserName'],user_password=request.POST['newPassword'],user_occupation=request.POST['newOccupation'],user_degreefk=course_list)
        addingUser.save()
    else:
        office_list = get_object_or_404(Office, pk = request.POST['selectingOffice'])
        addingUser = User(user_name=request.POST['newName'],user_username=request.POST['newUserName'],user_password=request.POST['newPassword'],user_occupation=request.POST['newOccupation'],user_officefk=office_list)
        addingUser.save()
    return render(request, 'Profile/signInTemp.html')

def signInPage(request):
    return render(request, 'Profile/signInTemp.html')    
    
def signIn(request):
    userList = User.objects.all()
    request.session["user"] = -1
    for x in userList:
        if x.user_username == request.POST['userName']:
            if x.user_password == request.POST['userPassword']:
                request.session["user"] = x.id
    if request.session["user"] < 0:
        return render(request, 'Profile/signInTemp.html')
    else:
        return HttpResponseRedirect(reverse('profileApp:viewProfile', args=(request.session["user"],)))
