from django.conf.urls import  url
from problem1.views import LatestArrayView, SaveArrayView

app_name = 'problem1'


urlpatterns = [
    url('latest_array',  LatestArrayView.as_view(), name='latest'),
    url('save_array', SaveArrayView.as_view(), name='save')
]

