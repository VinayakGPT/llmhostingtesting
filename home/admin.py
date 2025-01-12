from django.contrib import admin
from .models import Phase, UserSubmission, TASubmission, TAFeedback, Feedback

admin.site.register(Phase)
admin.site.register(UserSubmission)
admin.site.register(TASubmission)
admin.site.register(TAFeedback)
admin.site.register(Feedback)