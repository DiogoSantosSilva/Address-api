from django.urls import path
from address import views as addressviews

urlpatterns = [
    path('country/', addressviews.CountryListView.as_view()),
    path('country/<int:pk>', addressviews.CountryView.as_view()),

    path('state/', addressviews.StateListView.as_view()),
    path('state/<int:pk>', addressviews.StateView.as_view()),

    path('city/', addressviews.CityListView.as_view()),
    path('city/<int:pk>', addressviews.CityView.as_view()),

    path('neighbourhood/', addressviews.NeighbourhoodListView.as_view()),
    path('neighbourhood/<int:pk>', addressviews.NeighbourhoodView.as_view()),

    path('address/', addressviews.AddressListView.as_view(), name="get_all_address"),
    path('address/<int:pk>', addressviews.AddressView.as_view(), name="get_address"),

]