from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from core.models import About, Address, Career, CareerCsv, Certificates, ConditionCategory, Contact, Innovations, Partners, Project, ProjectCategory, Service, ServiceCategory,Image


# Register your models here.



@admin.register(ProjectCategory)
class ProjectCategoryAdmin(TranslationAdmin):
    list_display = ['name',]



class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 10
    
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['projects_images','image_tag',]
    readonly_fields = ('image_tag',)
    
    
    
@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['image_tag',]
    readonly_fields = ('image_tag',)
    

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ['title','description','condition','area','place','type','term','customer','categories','image_tag',]
    readonly_fields = ('image_tag',)
    inlines = [ProjectImageInline]
    

    




@admin.register(ConditionCategory)
class ConditionCategoryAdmin(TranslationAdmin):
    list_display = ['name',]


    




@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['name','title','image_tag',]
    
    
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslationAdmin):
    list_display = ['title','description',]



@admin.register(Certificates)
class CertificatesAdmin(TranslationAdmin):
    list_display = ['name',]



@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['mission_description',]
    




@admin.register(Innovations)
class InnovationsAdmin(TranslationAdmin):
    list_display = ['title','description','image_tag','created_at','updated_at','is_published',]
    list_filter = ['title','description','created_at','updated_at','is_published',]
    search_fields = ('title',)


@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ['address','phone_number',]
    list_filter = ['address',]
    search_fields = ('address',)
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','message',]
    list_filter = ['name',]
    search_fields = ('name',)
    
@admin.register(Career)
class CareerAdmin(TranslationAdmin):
    list_display = ['title',]
    
    
admin.site.register(CareerCsv)
