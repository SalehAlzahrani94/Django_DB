from django import forms
from .models import movies_info,Members,Publisher,MovieMembers,Review

# take the date form sended from view  and send it to members form models to add to DB
class MembersForm(forms.ModelForm): 
    class Meta : 
        model = Members  # add to member form models to add to that table in DB 
        fields = "__all__"
        # use fields = "-__all__" to take all data
    

# take the date form sended from view  and send it to members form models to add to DB
class PublisherForm(forms.ModelForm): 
    class Meta : 
        model = Publisher  # add to member form models to add to that table in DB 
        fields = ['name', 'website', 'email']
    

# take the date form sended from view  and send it to members form models to add to DB
class movies_infoForm(forms.ModelForm): 
    class Meta : 
        model = movies_info  # add to member form models to add to that table in DB 
        fields = ['name', 'date', 'publisher']
    
# take the date form sended from view  and send it to members form models to add to DB
class MovieMembersForm(forms.ModelForm): 
    class Meta : 
        model = MovieMembers  # add to member form models to add to that table in DB 
        fields = ['movie', 'Member', 'role']
    
# take the date form sended from view  and send it to members form models to add to DB
class ReviewForm(forms.ModelForm): 
    class Meta : 
        model = Review  # add to member form models to add to that table in DB 
        fields = ['content', 'rating','creator' , 'movie']