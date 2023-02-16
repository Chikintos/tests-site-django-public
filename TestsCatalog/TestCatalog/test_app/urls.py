from re import search
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="main"),
    path('test/<int:id>',views.testedit),
    path('test/addvariant/<int:id>/<int:testid>',views.add_variant),
    path('test/deletevariant/<int:id>/<int:testid>',views.delete_variant),
    path('test/addquestion/<int:testid>',views.add_question),
    path('test/removequestion/<int:testid>/<int:questid>',views.remove_question),
    path('test/savetest',views.savetest,name='savetest'),
    path('testlist/<int:page>',views.testview),
    path('test/pass/<int:id>',views.pass_test),
    path('test/submit',views.testsubmit,name='testsubmit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    
    