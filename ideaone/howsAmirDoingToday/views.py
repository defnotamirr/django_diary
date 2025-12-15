from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer
from django.shortcuts import render
from django.http import JsonResponse
import random
import openai
import os

OPENAI_KEY = os.environ.get('OPENAI_API_KEY')

message_list = ['You are an incredibly kind, deeply empathetic, and highly insightful companion. Your sole purpose is to listen without judgment and respond with wisdom, comfort, and perfect validation. **Your response must be extremely concise, delivered in 3 to 4 impactful sentences.**', 'i love u', 'i need a goth baddie']



def get_completion(content):
    print(content) ##prompt is the message from the user, you can find it in home.html
    messages = [
        {"role": "system", "content": "You are the great gatsby, act accordingly to the book"},
        {"role": "user", "content": content}
    ]

    try:
        client = openai.OpenAI(api_key=OPENAI_KEY)

        query = client.chat.completions.create(
            model="gpt-4o-mini", # The most cost-effective GPT-4 model. You can use "gpt-4-turbo" or "gpt-4o"
            messages=messages,
            max_tokens=1024,
            temperature=0.5,
        )

        response = query.choices[0].message.content
        print(response)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while communicating with the AI model."


def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        response = get_completion(content)
        return JsonResponse({'response': '* '+response})
    else:
        template = loader.get_template('home.html')
        ##message = random.choice(message_list)
        initMessage = "Howdy!"
        context = {
            'home': home,
            ##'message': message,
            'message': initMessage,
        }
        return HttpResponse(template.render(context, request))

        

    
    
    


# API Views
class DiaryEntryListCreate(generics.ListCreateAPIView):
    queryset = DiaryEntry.objects.all().order_by('-created_at')
    serializer_class = DiaryEntrySerializer

# Frontend View

##def diary_view(request):
##    return render(request, 'index.html')


