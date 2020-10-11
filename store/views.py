from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_be2bfc4758174ecea5b2405177a5d321
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_be2bfc4758174ecea5b2405177a5d321")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})


def about(request):
    return render(request, 'about.html')

# Create your views here.
