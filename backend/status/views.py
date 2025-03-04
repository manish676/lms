from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Status
from .serializers import StatusSerializer  # Fixed import

def fetch(req):
    statuses = Status.objects.all()
    res = StatusSerializer(statuses, many=True)  # Serialize multiple objects
    return Response(res.data, status=status.HTTP_200_OK)

def create(req):
    try:
        data = req.data
        newStatus = Status(
            title=data['title'],
            color=data['color']
        )
        newStatus.save()
        res = StatusSerializer(newStatus)
        
        return Response(res.data, status=status.HTTP_201_CREATED)  # Correct status
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

def update(req):
    try:
        data = req.data
        status_obj = Status.objects.get(id=data['id'])
        status_obj.title = data.get('title', status_obj.title)
        status_obj.color = data.get('color', status_obj.color)
        status_obj.save()
        
        res = StatusSerializer(status_obj)
        return Response(res.data, status=status.HTTP_200_OK)
    except Status.DoesNotExist:
        return Response({'error': 'Status not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

def delete(req):
    try:
        data = req.data
        status_obj = Status.objects.get(id=data['id'])
        status_obj.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Status.DoesNotExist:
        return Response({'error': 'Status not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def main(req):
    if req.method == "GET":
        return fetch(req)
    elif req.method == "POST":
        return create(req)
    elif req.method == "PUT":
        return update(req)
    elif req.method == "DELETE":
        return delete(req)
