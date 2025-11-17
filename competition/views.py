from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()
def home(request):
    # 這裡的 request 物件包含了所有來自使用者的請求資訊

    # render 函數會去 'templates' 資料夾中尋找 'index.html'
    # 並將其作為回應回傳
    return render(request, 'index.html')

def registration(request):
    context = {
        'FIREBASE_CONFIG': {
            'apiKey': os.getenv('FIREBASE_API_KEY'),
            'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
            'projectId': os.getenv('FIREBASE_PROJECT_ID'),
            'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
            'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
            'appId': os.getenv('FIREBASE_APP_ID'),
            'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID'),
        }
    }
    return render(request, 'registration.html', context)

def dashboard(request):
    # 這裡的 request 物件包含了所有來自使用者的請求資訊

    # render 函數會去 'templates' 資料夾中尋找 'index.html'
    # 並將其作為回應回傳
    return render(request, 'dashboard.html')