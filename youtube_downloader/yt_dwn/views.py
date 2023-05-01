from django.shortcuts import render,redirect
from pytube import *
# Create your views here.
def youtube(request):
   # checking whether request.method is post or not
    if request.method == 'POST':
        
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
  
        # setting video resolution
        stream = video.streams.get_audio_only()
          
        # downloads video
        stream.download()
  
        # returning HTML page
        return render(request, 'youtube.html')
    return render(request, 'youtube.html')

