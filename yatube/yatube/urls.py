from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

app_name = 'posts'

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    '''
    import debug_toolbar
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    '''
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
