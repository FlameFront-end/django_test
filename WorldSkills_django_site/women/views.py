from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenApiView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                woman = Women.objects.get(pk=pk)
                serializer = WomenSerializer(woman)
                return Response(serializer.data)
            except Women.DoesNotExist:
                return Response({"error": "Object does not exist"}, status=404)
        else:
            data = Women.objects.all()
            return Response({"women": WomenSerializer(data, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        women_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({"women": WomenSerializer(women_new).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "PK is required"}, status=400)

        try:
            instance = Women.objects.get(pk=pk)
        except Women.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=404)

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"women": serializer.data}, status=200)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "PK is required"}, status=400)

        try:
            instance = Women.objects.get(pk=pk)
            instance_id = instance.id
        except Women.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=404)

        instance.delete()
        return Response({"message": f"Record with ID {instance_id} deleted"}, status=200)
