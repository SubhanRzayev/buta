from modeltranslation.translator import translator, TranslationOptions

from .models import (
    About,
    Address,
    Career,
    Certificates,
    ConditionCategory,
    Innovations,
    Project,
    ProjectCategory,
    Service,
    ServiceCategory,
)

class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)
    
translator.register(Address,AddressTranslationOptions)



class CareerTranslationOptions(TranslationOptions):
    fields = ('title',)
    
translator.register(Career,CareerTranslationOptions)


class InnovationsTranslationOptions(TranslationOptions):
    fields = ('title','description',)
    
translator.register(Innovations,InnovationsTranslationOptions)



class CertificatesTranslationOptions(TranslationOptions):
    fields = ('name',)
    
translator.register(Certificates,CertificatesTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('content_about','mission_description',)
    
translator.register(About,AboutTranslationOptions)



class ServiceTranslationOptions(TranslationOptions):
    fields = ('name','title','service_content',)
    
translator.register(Service,ServiceTranslationOptions)


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title','description',)
    
translator.register(ServiceCategory,ServiceCategoryTranslationOptions)


class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('title','description','condition','area','place','type','term',)
    
translator.register(Project,ProjectCategoryTranslationOptions)



class ProjectCategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)
    
translator.register(ProjectCategory,ProjectCategoriesTranslationOptions)



class ConditionCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
translator.register(ConditionCategory,ConditionCategoryTranslationOptions)



