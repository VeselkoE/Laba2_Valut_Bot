from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
  #  path('task18/', include(('simpleapp.urls_18', 'task18'),
    #  namespace='task18')),
  #  path('task19/', include(('simpleapp.urls_19', 'task19'),
    #  namespace='task19')),
]


#Для каждого модуля создан свой urls, где в название пишется его номер
for i in range(18, 20):
    urlpatterns.append(
        path(f'task{i}/', include((f'simpleapp.urls_{i}', f'task{i}'),
                                 namespace=f'task{i}'))
    )