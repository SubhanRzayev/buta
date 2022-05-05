from django import forms
from core.models import Career, CareerCsv, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone',
            'email',
            'message',
        )
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-surname'
                }),
            
            'phone':forms.TextInput(attrs={
                'class':'phone'
                
                }),
            
            'email': forms.EmailInput(attrs={
                'class':'email1'
                
                }),
            
            
            'message': forms.Textarea(attrs={
                'class': 'textarea'
            })
        }
        

class CareerCsvForm(forms.ModelForm):
    
    
    class Meta:
        model = CareerCsv
        fields = [
            'career',
            'full_name',
            'email',
            'cv',
            
        ]
        
        def __init__(self, *args, **kwargs):
            super(CareerCsvForm, self).__init__(*args, **kwargs)
            self.fields['career'] = forms.ModelChoiceField(
                queryset=Career.objects.all(),initial=0
            )
            
    
    
        widgets = {
                
            'career':forms.Select(attrs={
                        'class':'custom-select',
                        'placeholder': 'Mövcud vakansiyalar *'
                    }),
            
            
            'full_name':forms.TextInput(attrs={
                        'class':'input-title',
                        'placeholder': 'Ad, Soyad, Ata adı *'
                    }),
            
            'email':forms.TextInput(attrs={
                        'class':'input-title',
                        'placeholder': 'Email *'
                    }),
            }
    
        