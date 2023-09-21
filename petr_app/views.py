from rest_framework.decorators import api_view
from .models import Category, Post, Tag
from .serializer import CategorySerialiser
from rest_framework.response import Response


@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerialiser(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerialiser(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerialiser(category)
        return Response(serializer.data, status=200)
    except Category.DoesNotExist:
        return Response(f'This category, with pk {pk} doesn\'t exist', status=404)


@api_view(['PUT'])
def category_change(request, pk):
    if not pk:
        return Response(f'Method don\'t allowed', status=405)
    try:
        instance = Category.objects.get(id=pk)
    except:
        return Response(f'This category, with pk {pk} doesn\'t exist', status=404)
    serializer = CategorySerialiser(data=request.data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
def category_delete(request, pk):
    if not pk:
        return Response(f'Method don\'t allowed', status=405)
    try:
        instance = Category.objects.get(id=pk)
    except:
        return Response(f'This category, with pk {pk} doesn\'t exist', status=404)
    instance.delete()
    return Response('deleted')
