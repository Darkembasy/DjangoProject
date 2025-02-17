from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms =[
#     {'id': 1, 'name':   'Lets learn python'},
#     {'id': 2, 'name': 'Design With Me'},
#     {'id': 3, 'name': 'Frontend Developers'},
# ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'room': rooms}
    return render(request, 'base/room.html', context)