from django.contrib import admin
from .models import Resident,MaintenanceWorker,Orc_Staff,Workorder,Equipment,MaintenanceWork,Roomallotment,User
from django.contrib.auth.admin import UserAdmin

import xlwt
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many \
              and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


def export_to_excel(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(opts.verbose_name)

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    fields = [field for field in opts.get_fields() if not field.many_to_many \
              and not field.one_to_many]
    for col_num in range(len(fields)):
        ws.write(row_num, col_num, fields[col_num].verbose_name)

    font_style = xlwt.XFStyle()

    for obj in queryset:
        data_row = []
        row_num += 1
        col_num = 0
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            if isinstance(value, Resident):
                value = value.__str__()
            if isinstance(value, Roomallotment):
                value = value.__str__()
            ws.write(row_num, col_num, value, font_style)
            col_num += 1

    wb.save(response)
    return response


export_to_excel.short_description = "Export to Excel"
export_to_csv.short_description = 'Export to CSV'


admin.site.register(User, UserAdmin)

class ResidentList(admin.ModelAdmin):
    list_display = ( 'resident_id', 'resident_name')
    list_filter = ( 'resident_id', 'resident_name')
    search_fields = ('resident_id','resident_name')
    ordering = ['resident_id']

admin.site.register(Resident,ResidentList)

class MaintenanceWorkerList(admin.ModelAdmin):
    list_display = ( 'worker_id', 'maintenanceworker_name')
    list_filter = ( 'worker_id', 'maintenanceworker_name')
    search_fields = ('worker_id','maintenanceworker_name')
    ordering = ['worker_id']

admin.site.register(MaintenanceWorker,MaintenanceWorkerList)

class StaffList(admin.ModelAdmin):
    list_display = ( 'orc_staff_id', 'orc_staff_name')
    list_filter = ( 'orc_staff_id', 'orc_staff_name')
    search_fields = ('orc_staff_id','orc_staff_name')
    ordering = ['orc_staff_id']

admin.site.register(Orc_Staff,StaffList)


class WorkorderList(admin.ModelAdmin):
    list_display = ( 'workorder_Description', 'workorder_id')
    list_filter = ( 'workorder_Description', 'workorder_Description')
    search_fields = ('workorder_Description','workorder_Description')
    ordering = ['workorder_Description']
    actions = [export_to_csv, export_to_excel]

admin.site.register(Workorder,WorkorderList)


class EquipmentList(admin.ModelAdmin):
    list_display = ( 'equipment_id', 'equipment_name')
    list_filter = ( 'equipment_id', 'equipment_name')
    search_fields = ('equipment_id','equipment_name')
    ordering = ['equipment_id']

admin.site.register(Equipment,EquipmentList)

class MaintenanceworkList(admin.ModelAdmin):
    list_display = ( 'maintenancework_id','maintenancework_description')
    list_filter = ( 'maintenancework_id','maintenancework_description')
    search_fields = ('maintenancework_id','maintenancework_description')
    ordering = ['maintenancework_id']

admin.site.register(MaintenanceWork,MaintenanceworkList)

class RoomallotmentList(admin.ModelAdmin):
    list_display = ( 'property_number', 'resident_name')
    list_filter = ( 'property_number', 'resident_name')
    search_fields = ('property_number','resident_name')
    ordering = ['property_number']

admin.site.register(Roomallotment,RoomallotmentList)