from django.utils import translation
from django.template import Library
from core.models import ServiceCategory,Service

from django.conf import settings
import flag

register = Library()




@register.simple_tag
def header_category():
    a = Service.objects.order_by('id')
    

    b = ServiceCategory.objects.order_by('id').filter(description__isnull=False)[:3]
    c = ServiceCategory.objects.order_by('id')
    
    
    context = {
        "service_list":a,
        "servicecategory":b,
        "cat":c,
        
    }
            
    return context



@register.filter
def get_language_info_list_ex(request):
    """
    Sample result:

        [{'bidi': False,
        'code': 'en',
        'flag': '🇬🇧',
        'is_current': False,
        'name': 'en',
        'name_local': 'en',
        'name_translated': 'en'},
        {'bidi': False,
        'code': 'az',
        'flag': '🇦🇿',
        'is_current': False,
        'name': 'az',
        'name_local': 'az',
        'name_translated': 'az'},
        {'bidi': False,
        'code': 'ru',
        'flag': '🇷🇺',
        'is_current': False,
        'name': 'Ru',
        'name_local': 'ru',
        'name_translated': 'ru'}]
    """
    data = []


    # From django.templatetags.i18n.GetLanguageInfoListNode
    def get_language_info(language):
        # ``language`` is either a language code string or a sequence
        # with the language code as its first item
        if len(language[0]) > 1:
            return translation.get_language_info(language[0])
        else:
            return translation.get_language_info(str(language))

    flag_map = {
        'en': 'gb',
    }

    # Es: 'es'
    current_language = translation.get_language()

    # Es: [('en', 'Inglés'), ('it', 'Italiano'), ('es', 'Español')]
    #languages = [(k, translation.gettext(v)) for k, v in settings.LANGUAGES]
    for language in settings.LANGUAGES:
        # Es: {'bidi': False, 'code': 'es', 'name': 'Spanish', 'name_local': 'español', 'name_translated': 'Español'}
        info = get_language_info(language)

        code = info['code']
        info['is_current'] = (code == current_language)

        # This requires emoji-country-flag Python package
        info['flag'] = flag.flag(flag_map.get(code, code))
        data.append(info)

    return data


