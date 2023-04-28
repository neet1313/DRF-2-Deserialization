import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        # First we parse a stream into Python native datatypes
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)

        # then we restore those native datatypes into a dictionary of validated data.
        serializer = StudentSerializer(data=pythonData)

        # convert python native data to complex data type->de-serialization
        if serializer.is_valid():
            # -->If True; serializer.validated_data={'name':'Henal', 'roll':1, 'city':'Mumbai'}

            # -->If we want to be able to return complete object instances
            # based on the validated data we need to
            # implement .create() method in serializers.py
            # -->Calling .save() will create a new instance
            serializer.save()
            res = {'msg': 'Data inserted'}
            return Response(res)
        else:
         # -->When deserializing data, you always need to call is_valid()
            # before attempting to access the validated data, or save an object instance.
            # If any validation errors occur, the .errors property will contain 
            # a dictionary representing the resulting error messages
            return Response(serializer.errors, serializer.is_valid(raise_exception=True))


# -> Make a create function in serializers.
