from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "users"
urlpatterns = [
    url(regex=r"^$", view=views.UserListView.as_view(), name="list"),
    url(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    url(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=views.UserDetailView.as_view(),
        name="detail",
    ),
    url(r'^obtain-auth-token/$', obtain_auth_token),
]
