from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('', views.stableDiffusionView.as_view(), name='stableDiffusion'),
    path('adApis/generate', views.stableDiffusionView.as_view(), name='stableDiffusionGenerate')
]