from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() #words는 list 형태가 됨.
    word_dictionary = {}

    for x in words:
        if x in word_dictionary:
            #increase
            word_dictionary[x] += 1
        else:
            # add to dictionary
            word_dictionary[x] = 1

    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary' : word_dictionary.items()}) # full - text