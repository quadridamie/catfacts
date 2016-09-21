from django.shortcuts import render
from my_app.models import CatFacts

# Create your views here.

def home(request):
    import urllib2 as url_req
    import json
    response = url_req.urlopen('http://catfacts-api.appspot.com/api/facts')
    response = response.read().decode('utf-8')
    data=json.loads(response)
    cat_dict = dict()
    fact = data.get('facts')
    cat_dict['facts']=fact[0]
    return render(request,'home.html',cat_dict)

def addName(request):
    return render(request,'addName.html')

def namedCat(request):
    import urllib2 as url_req
    import json
    response = url_req.urlopen('http://catfacts-api.appspot.com/api/facts')
    response = response.read().decode('utf-8')
    data=json.loads(response)
    cat_dict_named = dict()
    fact = data.get('facts')
    catString = str
    catString = fact[0]
    catNamed= request.GET['catName']
    NamedCatOne = catString.replace("cat", catNamed)
    NamedCatTwo = NamedCatOne.replace("cats", catNamed)
    NamedCatThree = NamedCatTwo.replace("Cat", catNamed)
    NamedCat = NamedCatThree.replace("Cats", catNamed)
    cat_dict_named['facts']=NamedCat
    return render(request,'namedCat.html',cat_dict_named)