from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Status


def fetch():
    return Response({
        'message': 'get request'
    })
    
def create():
    newStatus = Status(
        title="pending",  # Added a comma here
        color="#323232"
    )
    newStatus.save()
    return Response({
        'message': 'Post request successful'
    })


def update():
    return Response({
        'message': 'put request'
    })
    
def delete():
    return Response({
        'message': 'delete request'
    })



@api_view(['GET','PUT','POST','DELETE'])
def main(req) :
    if req.method == "GET": return fetch()
    elif req.method == "POST": return create()
    elif req.method == "PUT": return update()
    else: return delete()
    
    
