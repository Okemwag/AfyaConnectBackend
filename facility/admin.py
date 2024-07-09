from django.contrib import admin
from .models import Facility

# Register your models here.
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('Facility_Name', 'SubCounty', 'Level')
    search_fields = ('Facility_Name', 'SubCounty')
    list_filter = ('Level', 'SubCounty')
    ordering = ('Facility_Name', 'Level')
    fieldsets = (
        (None, {
            'fields': ('Facility_Name', 'SubCounty', 'ward_name')
        }),
        ('Location', {
            'fields': ('Latitude', 'Longitude', 'coordinates')
        }),
        ('Services', {
            'fields': ('Care_and_Treatment_Services', 'HIV_Testing_Services', 'PrEP_Services', 'PMTCT_Services')
        }),
    )
    readonly_fields = ('coordinates',)
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from django.utils.safestring import mark_safe

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="facilities.csv"'

        writer = csv.writer(response)
        writer.writerow(['Facility Name', 'SubCounty', 'Ward Name', 'Level', 'Latitude', 'Longitude', 'Care and Treatment Services', 'HIV Testing Services', 'PrEP Services', 'PMTCT Services'])

        for facility in queryset:
            writer.writerow([facility.Facility_Name, facility.SubCounty, facility.ward_name, facility.Level, facility.Latitude, facility.Longitude, facility.Care_and_Treatment_Services, facility.HIV_Testing_Services, facility.PrEP_Services, facility.PMTCT_Services])

        return response

    download_csv.short_description = 'Download CSV file for selected facilities'


