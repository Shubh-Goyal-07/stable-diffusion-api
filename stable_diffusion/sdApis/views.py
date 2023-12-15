from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from .sd_main import txt2img

# Create your views here.
class stableDiffusionView(APIView):

    def get(self, request, format=None):
        return Response("here", status=status.HTTP_200_OK)
        
    
    def post(self, request, format=None):
        prompt = request.data.get('prompt')
        # model = request.data.get('model')

        img_path = txt2img(prompt)

        # img = open(img_path, 'rb')

        # return FileResponse(fl, as_attachment=True, filename=f"my_filename.xyz", content_type='application/pdf')
        return Response(img_path, status=status.HTTP_200_OK)