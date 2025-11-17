from django.shortcuts import render

def home(request):
    # 這裡的 request 物件包含了所有來自使用者的請求資訊

    # render 函數會去 'templates' 資料夾中尋找 'index.html'
    # 並將其作為回應回傳
    return render(request, 'index.html')

def registration(request):
    # 這裡的 request 物件包含了所有來自使用者的請求資訊

    # render 函數會去 'templates' 資料夾中尋找 'index.html'
    # 並將其作為回應回傳
    return render(request, 'registration.html')

def dashboard(request):
    # 這裡的 request 物件包含了所有來自使用者的請求資訊

    # render 函數會去 'templates' 資料夾中尋找 'index.html'
    # 並將其作為回應回傳
    return render(request, 'dashboard.html')