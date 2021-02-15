from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from .models import *

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

import datetime
import xlwt
import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


def home(request):
    return render(request, 'ORC/home.html',
                  {'ORC': home})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ORC:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def about(request):
    return render(request, 'ORC/AboutUs.html')


@login_required
def export_workorders_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename=workorders.csv'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Workorders')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['resident', 'id', 'description', 'category', 'priority', 'property number', 'opened date', 'due date', 'closed date', 'open']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style.font.bold = False

    workorders = Workorder.objects.all().values_list('resident_name', 'workorder_id', 'workorder_Description', 'workorder_category', 'workorder_priority', 'property_number', 'workorder_opendate', 'workorder_duedate', 'workorder_closedate', 'is_open')

    for wo in workorders:
        row_num += 1
        for col_num in range(len(wo)):
            value = wo[col_num]
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            if isinstance(value, Resident):
                value = value.__str__()
            if isinstance(value, Roomallotment):
                value = value.__str__()
            ws.write(row_num, col_num, value, font_style)

    wb.save(response)
    return response


@login_required
def workorder_list(request): #resident_id):
        workorder = Workorder.objects.filter()
        return render(request, 'ORC/workorder_list.html', {'workorder': workorder})
    #if request.user.is_resident:
     #   workorder = get_object_or_404(Workorder, pk=workorder.pk)
      #  return redirect(request, 'ORC/workorder_list.html', {'workorder': workorder})


@login_required
def workorder_new(request):
    if request.method == "POST":
        form = WorkorderForm(request.POST)
        if form.is_valid():
            newworkorder = form.save(commit=False)
            newworkorder.created_date = timezone.now()
            newworkorder.save()
            workorder = Workorder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'ORC/workorder_list.html',
                          {'workorder': workorder})
            #return HttpResponseRedirect(reverse('ORC:workorder_list'))
    else:
        form = WorkorderForm()
    # print("Else")
    return render(request, 'ORC/workorder_new.html', {'form': form})


@login_required
def property_list(request):
    roomallotment = Roomallotment.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/property_list.html',
                 {'roomallotments': roomallotment})

@login_required
def property_new(request):
   if request.method == "POST":
       form = RoomallotmentForm(request.POST)
       if form.is_valid():
           newroomallotment = form.save(commit=False)
           newroomallotment.created_date = timezone.now()
           newroomallotment.save()
           roomallotment = Roomallotment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/property_list.html',
                         {'roomallotments': roomallotment})
   else:
       form = RoomallotmentForm()
       # print("Else")
   return render(request, 'ORC/property_new.html', {'form': form})

@login_required
def property_edit(request, pk):
   roomallotment = get_object_or_404(Roomallotment, pk=pk)
   if request.method == "POST":
       # update
       form = RoomallotmentForm(request.POST, instance=roomallotment)
       if form.is_valid():
           editroomallotment = form.save(commit=False)
           editroomallotment.updated_date = timezone.now()
           editroomallotment.save()
           roomallotment = Roomallotment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/property_list.html',
                         {'roomallotments': roomallotment})
   else:
        # edit
       form = RoomallotmentForm(instance=roomallotment)
   return render(request, 'ORC/property_edit.html', {'form': form})

@login_required
def property_delete(request, pk):
   roomallotment = get_object_or_404(Roomallotment, pk=pk)
   roomallotment.delete()
   return redirect('ORC:property_list')

@login_required
def maintenancework_list(request):
    maintenancework = MaintenanceWork.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/maintenancework_list.html',
                  {'maintenanceworks': maintenancework})
@login_required
def maintenancework_new(request):
   if request.method == "POST":
       form = MaintenanceWorkForm(request.POST)
       if form.is_valid():
           maintenancework = form.save(commit=False)
           maintenancework.created_date = timezone.now()
           maintenancework.save()
           ##maintenanceworks = MaintenanceWork.objects.filter(created_date__lte=timezone.now())
           return HttpResponseRedirect(reverse('ORC:maintenancework_list'))

   else:
       form = MaintenanceWorkForm()
       print(form)
       # print("Else")
       return render(request, 'ORC/maintenancework_new.html', {'form': form})

@login_required
def maintenancework_edit(request, pk):
   maintenancework = get_object_or_404(MaintenanceWork, pk=pk)
   if request.method == "POST":
       form = MaintenanceWorkForm(request.POST, instance=maintenancework)
       if form.is_valid():
           maintenancework = form.save()
           maintenancework.updated_date = timezone.now()
           maintenancework.save()
           maintenancework = MaintenanceWork.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/maintenancework_list.html', {'maintenanceworks': maintenancework})
   else:
       # print("else")
       form = MaintenanceWorkForm(instance=maintenancework)
   return render(request, 'ORC/maintenancework_edit.html', {'form': form})


@login_required
def maintenancework_delete(request, pk):
   maintenancework = get_object_or_404(MaintenanceWork, pk=pk)
   maintenancework.delete()
   return redirect('ORC:maintenancework_list')

@login_required()
def maintenancework_workerview(request, pk):
    print(" pk of logged in user",pk)
    worker=MaintenanceWorker.objects.get(user_id = pk)
    print(" object",worker)
    workerid=worker.worker_id
    print("worker id ",workerid)
    workerview = [x for x in (MaintenanceWork.objects.filter(maintenanceworker_name_id=workerid))]
    print("workder assigned to worker",workerview)
    return render(request, 'ORC/maintenancework_workerview.html',
                  {'workerview': workerview})


@login_required()
def resident_list(request):
    resident = Resident.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/resident_list.html',
                 {'residents': resident})

@login_required
def resident_new(request):
   if request.method == "POST":
       form = ResidentForm(request.POST)
       if form.is_valid():
           newresident = form.save(commit=False)
           newresident.created_date = timezone.now()
           newresident.save()
           resident = Resident.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/resident_list.html',
                         {'resident': resident})
   else:
       form = ResidentForm()
       # print("Else")
   return render(request, 'ORC/resident_new.html', {'form': form})

@login_required
def resident_edit(request, pk):
   resident = get_object_or_404(Resident, pk=pk)
   if request.method == "POST":
       # update
       form = ResidentForm(request.POST, instance=resident)
       if form.is_valid():
           editresident = form.save(commit=False)
           editresident.updated_date = timezone.now()
           editresident.save()
           resident = Resident.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/resident_list.html',
                         {'residents': resident})
   else:
        # edit
       form = ResidentForm(instance=resident)
   return render(request, 'ORC/resident_edit.html', {'form': form})

@login_required
def resident_delete(request, pk):
   resident = get_object_or_404(Resident, pk=pk)
   resident.delete()
   return redirect('ORC:resident_list')

@login_required()
def resident_workorderview(request, pk):
    print(" pk of logged in user",pk)
    Res=Resident.objects.get(user_id = pk)
    print(" object",Resident)
    res_id=Res.resident_id
    workerview = [x for x in (Workorder.objects.filter(resident_id=res_id))]
    print("workder assigned to worker",workerview)
    return render(request, 'ORC/resident_workorderview.html',
                  {'workerview': workerview})





@login_required
def maintenance_worker_list(request):
    maintenanceworker = MaintenanceWorker.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/maintenance_worker_list.html',
                 {'maintenanceworkers': maintenanceworker})

@login_required
def maintenance_worker_new(request):
   if request.method == "POST":
       form = MaintenanceWorkerForm(request.POST)
       if form.is_valid():
           newmaintenanceworker = form.save(commit=False)
           newmaintenanceworker.created_date = timezone.now()
           newmaintenanceworker.save()
           maintenanceworker = MaintenanceWorker.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/maintenance_worker_list.html',
                         {'maintenanceworkers': maintenanceworker})
   else:
       form = MaintenanceWorkerForm()
       # print("Else")
   return render(request, 'ORC/maintenance_worker_new.html', {'form': form})


@login_required
def maintenance_worker_edit(request, pk):
   maintenanceworker = get_object_or_404(MaintenanceWorker, pk=pk)
   if request.method == "POST":
       # update
       form = MaintenanceWorkerForm(request.POST, instance=maintenanceworker)
       if form.is_valid():
           editmaintenanceworker = form.save(commit=False)
           editmaintenanceworker.updated_date = timezone.now()
           editmaintenanceworker.save()
           maintenanceworker = MaintenanceWorker.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/maintenance_worker_list.html',
                         {'maintenanceworkers': maintenanceworker})
   else:
        # edit
       form = MaintenanceWorkerForm(instance=maintenanceworker)
   return render(request, 'ORC/maintenance_worker_edit.html', {'form': form})


@login_required
def maintenance_worker_delete(request, pk):
   maintenanceworker = get_object_or_404(MaintenanceWorker, pk=pk)
   maintenanceworker.delete()
   return redirect('ORC:maintenance_worker_list')





@login_required
def orc_staff_list(request):
    orc_staff = Orc_Staff.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/orc_staff_list.html',
                 {'orc_staffs': orc_staff})


@login_required
def orc_staff_new(request):
   if request.method == "POST":
       form = Orc_StaffForm(request.POST)
       if form.is_valid():
           neworcstaff = form.save(commit=False)
           neworcstaff.created_date = timezone.now()
           neworcstaff.save()
           orc_staff = Orc_Staff.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/orc_staff_list.html',
                         {'orc_staffs': orc_staff})
   else:
       form = Orc_StaffForm()
       # print("Else")
   return render(request, 'ORC/orc_staff_new.html', {'form': form})



@login_required
def orc_staff_edit(request, pk):
   orc_staff = get_object_or_404(Orc_Staff, pk=pk)
   if request.method == "POST":
       # update
       form = Orc_StaffForm(request.POST, instance=orc_staff)
       if form.is_valid():
           editorcstaff = form.save(commit=False)
           editorcstaff.updated_date = timezone.now()
           editorcstaff.save()
           orc_staff = Orc_Staff.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/orc_staff_list.html',
                         {'orc_staffs': orc_staff})
   else:
        # edit
       form = Orc_StaffForm(instance=orc_staff)
   return render(request, 'ORC/orc_staff_edit.html', {'form': form})

@login_required
def orc_staff_delete(request, pk):
   orc_staff = get_object_or_404(Orc_Staff, pk=pk)
   orc_staff.delete()
   return redirect('ORC:orc_staff_list')




@login_required
def equipment_list(request):
    equipment = Equipment.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ORC/equipment_list.html',
                 {'equipments': equipment})


@login_required
def equipment_new(request):
   if request.method == "POST":
       form = EquipmentForm(request.POST)
       if form.is_valid():
           newequipment = form.save(commit=False)
           newequipment.created_date = timezone.now()
           newequipment.save()
           equipment = Equipment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/equipment_list.html',
                         {'equipments': equipment})
   else:
       form = EquipmentForm()
       # print("Else")
   return render(request, 'ORC/equipment_new.html', {'form': form})


@login_required
def equipment_edit(request, pk):
   equipment = get_object_or_404(Equipment, pk=pk)
   if request.method == "POST":
       # update
       form = EquipmentForm(request.POST, instance=equipment)
       if form.is_valid():
           editequipment = form.save(commit=False)
           editequipment.updated_date = timezone.now()
           editequipment.save()
           equipment = Equipment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/equipment_list.html',
                         {'equipments': equipment})
   else:
        # edit
       form = EquipmentForm(instance=equipment)
   return render(request, 'ORC/equipment_edit.html', {'form': form})

@login_required
def equipment_delete(request, pk):
   equipment = get_object_or_404(Equipment, pk=pk)
   equipment.delete()
   return redirect('ORC:equipment_list')





@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ORC/password_change.html', {
        'form': form
    })


@login_required
def workorder_list(request): #resident_id):
        workorder = Workorder.objects.filter()
        return render(request, 'ORC/workorder_list.html', {'workorder': workorder})
    #if request.user.is_resident:
     #   workorder = get_object_or_404(Workorder, pk=workorder.pk)
      #  return redirect(request, 'ORC/workorder_list.html', {'workorder': workorder})


@login_required
def workorder_new(request):
    if request.method == "POST":
        form = WorkorderForm(request.POST)
        if form.is_valid():
            newworkorder = form.save(commit=False)
            newworkorder.created_date = timezone.now()
            newworkorder.save()
            workorder = Workorder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'ORC/workorder_list.html',
                          {'workorder': workorder})
            #return HttpResponseRedirect(reverse('ORC:workorder_list'))
    else:
        form = WorkorderForm()
    # print("Else")
    return render(request, 'ORC/workorder_new.html', {'form': form})

@login_required
def workorder_edit(request, pk):
   workorder = get_object_or_404(Workorder, pk=pk)
   if request.method == "POST":
       # update
       form = WorkorderForm(request.POST, instance=workorder)
       if form.is_valid():
           editworkorder = form.save(commit=False)
           editworkorder.updated_date = timezone.now()
           editworkorder.save()
           workorder = Workorder.objects.filter(created_date__lte=timezone.now())
           return render(request, 'ORC/workorder_list.html',
                         {'workorder': workorder})
   else:
        # edit
       form = WorkorderForm(instance=workorder)
   return render(request, 'ORC/workorder_edit.html', {'form': form})

@login_required
def workorder_delete(request, pk):
   workorder = get_object_or_404(Workorder, pk=pk)
   workorder.delete()
   return redirect('ORC:workorder_list')


class WorkorderList(APIView):
    def get(self, request):
        workorders_json = Workorder.objects.all()
        serializer = WorkorderSerializer(workorders_json, many=True)
        return Response(serializer.data)


class ResidentList(APIView):
    def get(self, request):
        residents_json = Resident.objects.all()
        serializer = ResidentSerializer(residents_json, many=True)
        return Response(serializer.data)