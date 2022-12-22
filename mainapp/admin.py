from django.contrib import admin
from .models import (Military,
Prospect,
Areas_Of_Interest,
CallCenter,
Search,
Other_Info,
SearchConnected,)

# Register your models here.

admin.site.register(Military)
admin.site.register(Prospect)
admin.site.register(Areas_Of_Interest)
admin.site.register(CallCenter)
admin.site.register(Search)
admin.site.register(Other_Info)
admin.site.register(SearchConnected)
