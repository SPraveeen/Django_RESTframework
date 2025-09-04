from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST','PUT'])
def index(request):
    courses={
        'course_name':'Python',
        'Learn':['Flask','Django',"FastAPI"],
        'Course_Provider':'Scaler'
    }    
    if request.method=='GET':
        print(request.GET.get('search'))
        print('YOU HIT A GET METHOD')
        return Response(courses)
    elif request.method=='POST':
        data=request.data
        print("------")
        print(data['name'])
        print("------")
        print('YOU HIT A POST METHOD')
        return Response(courses)
    elif request.method=='PUT':
        print('YOU HIT A PUT METHOD')
        return Response(courses)
    
