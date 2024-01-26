from django.shortcuts import render
import requests
from users.forms import UserRegistrationForm

def index(request):
    return render(request, 'index.html', {})


def workingProcess(request):
    input_text = 'There are several parameters that can be used for indicating the performance of a TTS system. The most common parameter is mean opinion score (MOS) which is broadly used to measure the naturalness of the generated speech'  # request.POST["voice"]
    speech_voice = 'banmai'  # request.POST["name"]
    speech_speed = b'0'  # request.POST["speeds"]
    url = 'https://api.fpt.ai/hmi/tts/v5'
    header = {
        'api-key':'BJtsEZz3CCpeRCixZL6EvVpjPmhCewHQ',
        'speed': speech_speed,
        'voice': speech_voice
    }
    response = requests.request('POST', url,data=input_text.encode('utf-8'), headers=header)
    substr = response.text.split('"')[3]
    # success
    context = {"link": substr}
    print("Context is ",context)
    return render(request, "index.html", context)

def logout(request):
    return render(request, 'index.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


def UserRegister(request):
    form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
