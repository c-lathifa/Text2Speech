from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel,UsersSpeechDataModel,UserTimeDurationModel
import requests
import time

# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})
def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def TextToSpeechForm(request):
    return render(request, 'users/UserTextToSpeechForm.html',{})

def GenerateSpeaksforUser(request):
    input_text = request.POST["text"]
    speech_voice = request.POST["voice"]
    speech_speed = request.POST["speed"]
    url = 'https://api.fpt.ai/hmi/tts/v5'
    header = {
        'api-key': 'BJtsEZz3CCpeRCixZL6EvVpjPmhCewHQ',
        'speed': speech_speed,
        'voice': speech_voice
    }
    start = time.time()
    response = requests.request('POST', url, data=input_text.encode('utf-8'), headers=header)
    substr = response.text.split('"')[3]
    end = time.time()

    secDiffe = end-start
    print("Start Time =", start, " End Time = ", end, " Difference = ", secDiffe)
    voice = speech_voice
    txtLen = len(input_text)

    # success
    context = {"link": substr}
    print("Context is ", context)
    loggeduser = request.session['loggeduser']
    loginid = request.session['loginid']
    email = request.session['email']
    UsersSpeechDataModel.objects.create(loggeduser=loggeduser, loginid=loginid,email=email, textdata=input_text,link=substr)
    UserTimeDurationModel.objects.create(username=loginid,voicename=voice,timesec=secDiffe,textlen=txtLen)
    #return render(request, 'users/UserTextToSpeechForm.html',context)
    return render(request, 'users/PlayAudioFile.html', context)

def UserSpeechData(request):
    loginid = request.session['loginid']
    data = UsersSpeechDataModel.objects.filter(loginid=loginid)
    return render(request, 'users/UserSpeechDataView.html', {'data':data})

def UserTimeDifference(request):
    loginid = request.session['loginid']
    data = UserTimeDurationModel.objects.filter(username=loginid)
    return render(request, 'users/UserTimeDataView.html', {'data':data})
