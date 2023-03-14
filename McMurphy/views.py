from django.shortcuts import render

#APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할
# 서버와 클라이언트가 데이터를 주고받는 방법은 여러 가지가 있는데, 
# 여기서는 HTTP 통신이라는 방법을 사용합니다. 
# 우리가 특정 홈페이지에 들어갈때 주소 맨앞에 적는 HTTP가 바로 이 HTTP 통신입니다. 
# HTTP 통신 안에도 또 여러가지 종류가 있습니다. 
# 그중 대표적으로 get과 post가 있는데요, 
# 일반적으로 홈페이지를 조회하는 데는 get방식을 사용하고, 
# 특정 작업(?)을 요청할 때는 post를 사용합니다. 

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
class Main(APIView):  #클래스 네임을 main으로 정한거다
    def get(self, request):
        return render(request, 'clone_instagram.html') 
        #요청값을 html파일로 정보 요청