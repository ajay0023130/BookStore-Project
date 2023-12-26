from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        
    'Books':
    [
    {   'id':1,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },
    {   'id':2,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },
     {  'id':3,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },
     {  'id':4,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },
     {   'id':5,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },
     {  'id':6,
        'name':"Mastering Django: A Beginner's Guide",
        "ImageUrl":"https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/71AR6gLlkrL._SY385_.jpg"
        
    },

    ]
    
    }
    return render(request,'Books/index.html',context)


def show(request,id):

    return render(request,'Books/BookDetails.html')
