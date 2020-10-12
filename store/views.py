from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # pk_be2bfc4758174ecea5b2405177a5d321
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_be2bfc4758174ecea5b2405177a5d321")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker':"Enter a ticker symbol above..."})



def about(request):
    return render(request, 'about.html')


def add_stock(request):
    return render(request, 'add_stock.html')

# Create your views here.
