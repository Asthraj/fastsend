from django.urls import path, include
from adminpnl.views import myview
from adminpnl.views import myvieww
from adminpnl.views import myviewt
from adminpnl.views import sendsms
from adminpnl.views import sendwhatsapp
from adminpnl.views import myviewe

from . import views



urlpatterns = [
    path('', views.adminhome, name="home"),
    path('file_operations',views.file_operations,name="FO"),
    path('myview',myview,name="myview"),
    path('myviewe',myviewe,name="myviewe"),
    path('myvieww',myvieww,name="myvieww"),
    path('myviewt',myviewt,name="myviewt"),
    path('sendsms',sendsms,name="sendsms"),
    path('sendwhatsapp', sendwhatsapp , name="sendwhatsapp"),
    path("uploadfile",views.uploadfile,name="uploadfile"),
    path("showdata",views.showdata,name="showdata"),
    path("dataexport",views.dataexport,name="dataexport"),
    path("exporttomail",views.export_to_mail,name="exporttomail"),
    path("exportmail",views.exportmail,name="exportmail"),
    path("logout",views.logout,name="logout"),
    path("backtohome",views.backtohome,name="backtohome"),
]
