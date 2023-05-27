from django.shortcuts import render 
import requests
# Create your views here.

def index(request):
    url = "https://newsapi.org/v2/everything?q=Everything&from=2023-05-22&sortBy=popularity&apiKey=a7bbc567609842aeb10ab6ebe37c27bf"
    c_news = requests.get(url).json()
    print(c_news)

    a = c_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(title,desc,img)
    context = {'mylist':mylist}
    return render(request,'index.html',context)


def apple(request):
    url = "https://newsapi.org/v2/everything?q=Apple&from=2023-05-22&sortBy=popularity&apiKey=a7bbc567609842aeb10ab6ebe37c27bf"
    a_news = requests.get(url).json()
    print(a_news)

    a = a_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    apple_li = zip(title,desc,img)
    context = {'apple_li':apple_li}
    return render(request,'index.html',context)

def sport(request):
    url = "https://newsapi.org/v2/everything?q=Cricket&from=2023-05-22&sortBy=popularity&apiKey=a7bbc567609842aeb10ab6ebe37c27bf"
    cc_news = requests.get(url).json()
    print(cc_news)

    a = cc_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    cc = zip(title,desc,img)
    context = {'cc':cc}
    return render(request,'Sport.html',context)

def electronics(request):
    url = "https://newsapi.org/v2/everything?q=Electronics&from=2023-05-22&sortBy=popularity&apiKey=a7bbc567609842aeb10ab6ebe37c27bf"
    el_news = requests.get(url).json()
    print(el_news)

    a = el_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    el = zip(title,desc,img)
    context = {'el':el}
    return render(request,'Electronics.html',context)


def bolly(request):
    url = "https://newsapi.org/v2/everything?q=Bollywood&from=2023-05-22&sortBy=popularity&apiKey=a7bbc567609842aeb10ab6ebe37c27bf"
    b_news = requests.get(url).json()
    print(b_news)

    a = b_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    bl = zip(title,desc,img)
    context = {'bl':bl}
    return render(request,'bollywood.html',context)


