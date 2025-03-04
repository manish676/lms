from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Status
from .searializers import StatusSerializers

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
        res = StatusSerializers(newStatus)
        
        return Response(res.data, status= status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_424_FAILED_DEPENDENCY)

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
