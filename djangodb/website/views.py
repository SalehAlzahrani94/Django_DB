from django.shortcuts import render ,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages # show succes message or not 
from .utils import avrage_rating
import time
# Create your views here.

def home(request):
    all_date = Members.objects.all() # take all date from members and put it in object 
    return render(request, 'home.html', {"all":all_date}) # send oject with name all to html to show data


def join(request):
    if request.method == "POST": # if the called is post then 
        form =  MembersForm(request.POST or None) # pass the requst to membersform form forms 
        if form.is_valid(): # check if values have error if not then 
            form.save() # save to DB 
        else: 
            messages.success(request, ('errer in form !'))
            return redirect('join') # redirect any where you want 

        messages.success(request, ('added successfully!'))
        return redirect('home') # redirect any where you want 
        
    else:
        return render(request, 'join.html', {})
    
def Publisher(request):
    if request.method == "POST": # if the called is post then 
        x =  PublisherForm(request.POST or None) # pass the requst to membersform form forms 
        '''if x.is_valid(): # check if values have error if not then 
            x.save() # save to DB 
        else: 
            messages.success(request, ('errer in form !'))
            return redirect('publisher') # redirect any where you want 

        messages.success(request, ('added successfully!'))
        return redirect('home') # redirect any where you want 
        '''
        x.save() 
    else:
        return render(request, 'Publisher.html', {})
    
# if there is reviews get avg , if not set to None and number to 0
# send back resutl data in dic has list that has dic 
def MoviesList(request):
    movies = movies_info.objects.all()
    movies_list = []
    for Movie in movies:
        # movie.review_set.all() return all the reviews of that movie
        reviews = Movie.review_set.all()
        if reviews: # if there is reviews 
            movie_rating = avrage_rating([review.rating for review in reviews])
            number_of_reviews= len(reviews)
        else:
            movie_rating = None
            number_of_reviews = 0
        movies_list.append({'Moive': Movie , 'Movie_rating':movie_rating , 'Number_of_reviews':number_of_reviews})
   
    return render(request, 'movie_list.html',{'movies' : movies_list})



def Member_edit(request,pk=None): # take PK to updata 
    # if there is pk for this persone then retrive his data , note if not there 404 not found
    if pk is not None: 
        member = get_object_or_404(Members, pk=pk)
    else:
        member = None

    if request.method == "POST": # if the called is post then 
        form =  MembersForm(request.POST , instance=member) # pass the requst to membersform form forms 
        if form.is_valid(): # check if values have error if not then 
            update_member = form.save() # save to DB 
            if member is None:  # if not in DB show message create 
                messages.success(request, "Member \"{}\"was created ".format(update_member))
            else : # if in DB show message update  
                messages.success(request, "Member \"{}\"was updated ".format(update_member))
            return redirect('Member_edit' , update_member.pk) # redirect and get pk of memeber created of updated 

    else : # if the called not post (just view page - get)
        form =  MembersForm(instance=member) # create new ,  requst to membersform form forms 

    # in the end return request type and instacne (ob to get date from forms.py )
    return render(request, 'forms.html', {"method": request.method, "form" : form})


def add(request): 
    if request.method == "POST": # if the called is post then 
        form =  MembersForm(request.POST) # pass the requst to membersform form forms 
        if form.is_valid(): # check if values have error if not then 
            update_member = form.save() # save to DB 
            messages.success(request, "Member \"{}\"was created ".format(update_member))
            return redirect('add') # redirect and get pk of memeber created of updated 
        else : # if not valid fomat ( emial = 2565)
            messages.success(request, "Member not added  ")
            #time.sleep(3) # dilay 3 sec
            return redirect('add') # redirect and get pk of memeber created of updated 
        

    else : # if the called not post (just view page - get)
      #  form =  MembersForm(instance=member) # create new ,  requst to membersform form forms 

       # in the end return request type and instacne (ob to get date from forms.py )
        return render(request, 'forms.html', {"method": request.method })


def update(request,pk=None): # take PK to updata 
    # if there is pk for this persone then retrive his data , note if not there 404 not found
    if pk is not None: 
        member = get_object_or_404(Members, pk=pk)
    else:
        member = None

    if request.method == "POST": # if the called is post then 
        form =  MembersForm(request.POST , instance=member) # pass the requst to membersform form forms 
        if form.is_valid(): # check if values have error if not then 
            update_member = form.save() # save to DB 
            if member is None:  # if not in DB show message create 
                messages.success(request, "Member \"{}\"was created ".format(update_member))
        #        return redirect('update') # redirect and get pk of memeber created of updated 
            else : # if in DB show message update 
                messages.success(request, "Member \"{}\"was updated ".format(update_member))
            return redirect('update_pk' , update_member.pk) # redirect and get pk of memeber created of updated 


    else : # if the called not post (just view page - get)
     #   form =  MembersForm(instance=member) # create new ,  requst to membersform form forms 

    # in the end return request type and instacne (ob to get date from forms.py )
        return render(request, 'forms.html', {"method": request.method})