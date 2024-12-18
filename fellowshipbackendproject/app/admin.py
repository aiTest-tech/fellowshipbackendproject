from django.contrib import admin
from .models import MediaModel, BatchModel, MeetOurFellowsModel

# Register your models here.


class MediaModelAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ("id", "title_eng", "title_guj", "img", "active_deactivate")

    # Optional: Add filters for boolean fields or others
    list_filter = ("active_deactivate",)

    # Optional: Add search functionality
    search_fields = ("title_eng", "title_guj")


# Register the model with the custom admin class
admin.site.register(MediaModel, MediaModelAdmin)


class MeetOurFellowAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ("batch", "department", "full_name", "ug_degree", "age", "post_graduation", "pg_university", "bachelore_degree","ug_university")

    # Optional: Add filters for boolean fields or others
    list_filter = ("batch", "department", "full_name", "ug_degree", "age", "post_graduation", "pg_university", "bachelore_degree","ug_university")

    # Optional: Add search functionality
    search_fields = ("department", "full_name", "batch")

admin.site.register(MeetOurFellowsModel, MeetOurFellowAdmin)



admin.site.register(BatchModel)
# admin.site.register(MeetOurFellowsModel)