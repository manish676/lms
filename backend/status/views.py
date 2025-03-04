from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Status

def fetch(req):
    return Response({
        'message': 'get request'
    })

def create(req):
    try:
        data = req.data
        newStatus = Status(
            title=data['title'],
            color=data['color']
        )
        newStatus.save()
        return Response({
            'message': 'Post request successful'
        })
    except Exception as err:
        return Response({'error': str(err)}, status=400)

def update(req):
    return Response({
        'message': 'put request'
    })

def delete(req):
    return Response({
        'message': 'delete request'
    })

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def main(req):
    if req.method == "GET":
        return fetch(req)
    elif req.method == "POST":
        return create(req)
    elif req.method == "PUT":
        return update(req)
    else:
        return delete(req)
