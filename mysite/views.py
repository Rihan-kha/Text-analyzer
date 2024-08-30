# This file by me Rihan``
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = "this is data"
    context = {'data':data}
    return render(request , 'index.html',context)


def analyze(request):
    string = request.POST.get('text','default')
    remove_punc = request.POST.get('remove-punc','off')
    remove_space = request.POST.get('remove-space','off')
    capitalize= request.POST.get('Capitalize','off')
    remove_new_line = request.POST.get('remove-new-line','off')

    punctuations = '''!@#$%^&*()_-+=|\{[]}:;"'<,>.?/'''

    analyzed_text=""
    print(len(string))
    for i in range(len(string)):
        char = string[i]
        
        if remove_punc == 'on' and char not in punctuations:
            analyzed_text+=char

        elif remove_space == 'on' and string[i:i+2] != "  " :
            analyzed_text+=char
        elif remove_new_line == 'on' and char != "\n" and char != "\r" :
            print(char)
            analyzed_text+=char
            

        elif capitalize == 'on':
            char =char.upper()
            analyzed_text+=char

    
        

    context = {'purpose':remove_punc,'data':analyzed_text}
    return render(request , 'analyze.html',context)

