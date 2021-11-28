from django.contrib import admin  
from django.urls import path  
from App import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show,name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('accounts/signup', views.signup, name='signup'),
    path('delete/<int:id>', views.destroy),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)