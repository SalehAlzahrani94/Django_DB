from django.db import models
from django.contrib import auth
# Create your models here.



class Publisher (models.Model):
    name =models.CharField(max_length=50 , help_text="the name of the publisher")
    website = models.URLField( max_length=100 ,help_text="pubisher website")
    email = models.EmailField( help_text="pubisher website")
    # return the name of publisher
    def __str__(self) : 
        return self.name
    
# replace contrpuber class
class Members(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length= 50)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length= 50)
    age = models.IntegerField()

    def __str__ (self):
        return self.fname + " " + self.lname
    
# note : fornkey must be down then the one he refare to 
class movies_info (models.Model):
    name = models.CharField(max_length=50 , help_text= "the name of the movie")
    date = models.DateField(max_length= 50 , help_text= "date the movie was relased ")
    # var = many to one foreiignkey( table we relat to , if delete publisher delete movie info )
    publisher = models.ForeignKey(Publisher , on_delete = models.CASCADE)

    # manay to many through to mid class 
    members = models.ManyToManyField("Members", through="MovieMembers")
    def __str__(self) :
        return self.name
    
# class betewenn movie_info and members (who do this movies and there rols)
class MovieMembers(models.Model):
    # sub to make chose 
    class MembersRole(models.TextChoices):
        ACTOR = "ACTOR", "Actor" # roles
        DIRECTOR = "DIRECTOR", "director"
        # link to other tables 
    movie = models.ForeignKey(movies_info,on_delete=models.CASCADE)
    Member = models.ForeignKey(Members, on_delete=models.CASCADE)
    # role is to chose betwennn the choices we make up in this class (ContributionRole)
    role = models.CharField(verbose_name="the role this member had in this movie ", choices=MembersRole.choices , max_length=20)

    
class  Review (models.Model):
    content = models.CharField(max_length=100 ,help_text="the reivew text")
    rating = models.IntegerField( help_text="the rating the reivew given ")
    date_created = models.DateTimeField(auto_now_add=True , help_text="the time and date reivew was created ")
    # craetor chose (show only the user create it , user name saleh then options saleh)
    creator = models.ForeignKey(auth.get_user_model(), on_delete= models.CASCADE)
    movie = models.ForeignKey(movies_info, on_delete= models.CASCADE, help_text="this line to show moveis in DB you can reviews ") 
 