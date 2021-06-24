from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from classapp.schema import schema


admin.site.site_title = "Yam's Site"
admin.site.site_header = "Yam's Admin"
admin.site.index_title = "Welcome To Yam's Administration"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classapp.urls', namespace='classapp')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(schema=schema, graphiql=True))),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
