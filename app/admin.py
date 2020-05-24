from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quiz_Event)
admin.site.register(Quiz_Section)
admin.site.register(Quiz_Question)
admin.site.register(Quiz_Choices)
admin.site.register(Quiz_Answer)