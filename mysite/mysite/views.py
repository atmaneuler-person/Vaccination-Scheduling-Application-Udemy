# 이제 Mysite 폴더에 views.py 파일이라는 파일을 생성해야 합니다.
# Django에서 뷰를 생성하려면 매개변수에서 요청을 받는 함수를 생성해야 합니다.
# 그래서 index라는 함수를 생성하고 이 함수는 매개변수에서 요청을 받습니다: def index(request):

# 이제 요청을 받아 응답을 반환하는 뷰를 만들고 싶습니다. 따라서 응답을 반환하려면 Http 응답으로 가져와야 합니다. 그래서 Django dot SDP에서 우리는 얻었습니다.
# 이 SDP 응답을 가져와야 합니다.
from django.http import HttpResponse 
# setting에서 BASE_DIR/"templates"] 후에, 이제 Views.py 파일을 열고 HTML 페이지로 렌더링하려면 Django dot에서 렌더링 메서드를 가져와야 합니다.
# 따라서 Django Dot 단축키에서 render라는 메서드를 가져오겠습니다.
from django.shortcuts import render


def index(request):  # 이제 이 함수는 Django에서 뷰로 처리됩니다.
    # return HttpResponse("Hi") # 응답한다 --> render 반영으로 대체
    context = {
        "message": "Hellow Django Developers",
    }
    return render(request, "mysite/index.html", context)