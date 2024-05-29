from django.shortcuts import render
from textblob import TextBlob

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity

            return render(request, 'result.html', {'text': text, 'sentiment_score': sentiment_score})

    return render(request, 'setup.html')