from django.urls import path 
from . import views 

urlpatterns = [ 
	path('upload_metadata/', views.upload_metadata.as_view(), name ='upload_metadata'), 
    path('get_metadata/', views.get_metadata.as_view(), name ='get_metadata'), 
    path('get_all_metadata/', views.get_all_metadata.as_view(), name ='get_all_metadata'),
    path('upload/<str:filename>', views.FileUploadView.as_view()),
    path('documents/', views.get_documents.as_view(), name ='documents'),
    path('document/<str:filename>', views.get_document.as_view(), name ='document'),
    path('register/',views.register.as_view(), name='register')
] 
