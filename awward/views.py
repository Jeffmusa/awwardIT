from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from .forms import *
import datetime as dt
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    
    comment_form = CommentForm()
    return render(request, 'home.html',{"date": date,"projects":projects,"comment_form":comment_form})
@login_required(login_url='/accounts/login/')
def review(request,id):
    comment_form = CommentForm()
    profile = Profile.objects.filter(user_id=id)
    post = Projects.objects.get(id=id)                       
    return render(request,'review.html',{"profile":profile,"post":post,"comment_form":comment_form})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            merch = self.get_merch(pk)
            merch.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Projects.objects.all()
        serializers = ProjectsSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)    

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
            merch = self.get_merch(pk)
            merch.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@login_required(login_url='/accounts/login/')
def profile(request):
    # projects = Projects.objects.all()
    # pr = Profile.objects.all()
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    posts = Projects.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile})
    return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile})


def upload(request):
    # upload = Image.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = ProjectForm()
    return render(request, 'upload.html', {"form": form , "upload": upload})


def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    post=Projects.objects.filter(user_id=id)
   
                       
    return render(request,'pros.html',{"profile":profile,"post":post})

def search_results(request):    
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_projects = Projects.objects.filter(name=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_projects": searched_projects})

    else:
        message = "Please search for a valid Project"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def comment(request,id):
    upload = Projects.objects.get(id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.project = upload
            comment.save()
            print(comment)
        return redirect('/')
    return redirect('/')

def get_post_by_id(request,id):
        post = Projects.objects.get(id=id)
        vote = Votes()
        if request.method == 'POST':

                vote_form = Votes(request.POST)
                if vote_form.is_valid():

                        design = vote_form.cleaned_data['design']
                        usability = vote_form.cleaned_data['usability']
                        content = vote_form.cleaned_data['content']
                        creativity = vote_form.cleaned_data['creativity']
                        rating = Rates(design=design,usability=usability,
                                        content=content,creativity=creativity,
                                        user=request.user,post=post)
                        rating.save()
                        return redirect('/')
        return render(request,'vote.html',{"post":post,"vote":vote})
