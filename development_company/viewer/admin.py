from django.contrib import admin
from .models import Construction_management, Director, Sector
from .models import Engineering_staff, Customer, Contract
from .models import Obj, Specification, Equipment
from .models import Object_equipment, Work_type, Brigade
from .models import Worker, Estimation, Report, Consumption

class Construction_managementAdmin(admin.ModelAdmin):
    list_display = ('id', 'telephone','address')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'management','full_name', 'telephone','birth_date', 'passport')

class SectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'management','address', 'square')

class Engineering_staffAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'sector', 'telephone','birth_date', 'passport','position','is_manager')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name', 'tin', 'telephone')

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'total')

class ObjAdmin(admin.ModelAdmin):
    list_display = ('id','obj_name','sector','contract')

class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id','obj', 'tag','note')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'telephone', 'passport','speciality')

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id','equipment_type', 'tag', 'status')

class Object_equipmentAdmin(admin.ModelAdmin):
    list_display = ('id','obj', 'equipment')

class Work_typeAdmin(admin.ModelAdmin):
    list_display = ('id','tag', 'obj', 'started','finished')

class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id','work_type', 'worker')

class EstimationAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_type', 'item', 'quantity')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_type', 'started_actual', 'finished_actual')

class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 'item', 'quantity')

admin.site.register(Construction_management, Construction_managementAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Engineering_staff, Engineering_staffAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Obj, ObjAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Object_equipment, Object_equipmentAdmin)
admin.site.register(Work_type, Work_typeAdmin)
admin.site.register(Brigade, BrigadeAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Estimation, EstimationAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Consumption, ConsumptionAdmin)



admin.site.site_title = 'Администрирование: строительная компания'
admin.site.site_header = 'Администрирование: строительная компания'