from rest_framework import serializers

from women.models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

# def encode():
#     model = WomenModel('Test', 'Test content')
#     model_sr = WomenSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#     return json
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Test","content":"Test content"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
