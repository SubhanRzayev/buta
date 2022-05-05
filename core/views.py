from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView

from django.views.generic import ListView,CreateView
from django.urls import reverse, reverse_lazy
from .models import About, Address, Career, Certificates, ConditionCategory, Contact, Innovations, Partners, Project, ProjectCategory, Service
from .forms import CareerCsvForm, ContactForm

from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def project_list(request,category_slug=None):
    category=None
    category_query=None
    
    kategory = ProjectCategory.objects.all()
    categories=ConditionCategory.objects.all()
    project = []
   
    category_query = request.GET.get('select')
    
    
    if category_slug is None and category_query is None:
        project = Project.objects.all()
    
    
    if category_query == '' or category_query is not None:
        project = Project.objects.filter(categories__name=category_query)
        
        if category_slug == '' or category_slug is not None:
            project=Project.objects.all()
            category=get_object_or_404(ConditionCategory,slug=category_slug)
        
            project=project.filter(category__name=category)
    
    if category_query == "1":
        print("subhna")
        project = Project.objects.all()
        
        
    if category_slug == '' or category_slug is not None:
        project=Project.objects.all()
        category=get_object_or_404(ConditionCategory,slug=category_slug)
    
        project=project.filter(category__name=category)
        
        
        
        
        
        
    # if category_slugs:
    #     project=Project.objects.all()
        
    #     category=get_object_or_404(ProjectCategory,slug=category_slugs)
    #     project=project.filter(categories__name=category)
        
        
        

    
    
    
    return render(request,'cases.html',{
                    'categories':categories,
                    'project_list':project,
                    'category':category,
                    'kategory':kategory,
                    
                    })




# class ProjectListView(ListView):
#     model = Project
#     template_name = 'cases.html'

#     success_url = reverse_lazy("core:cases")
    
    
    
#     # def get_queryset(self):
#     #     if 'category_slug' in self.kwargs:
#     #         self.category = get_object_or_404(ConditionCategory, slug=self.kwargs['category_slug'])

#     #         return Project.objects.filter(category=self.category)
        
            
            
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = ConditionCategory.objects.all()
#         context["kategory"] = ProjectCategory.objects.all()
        
        
        
        
#         return context
    
        
            
    
    
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'case-detail.html'
    success_url = reverse_lazy("core:cases")
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects_list"] = Project.objects.all()[:3]
    
        return context
    





class ServiceListView(ListView):
    model = Service
    template_name = 'index.html'
    success_url = reverse_lazy("core:index")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects_list"] = Project.objects.all()
        context["partners_list"] = Partners.objects.all()
        
        return context
    
    
    
    


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service-details.html'
    success_url = reverse_lazy("core:index")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects_list"] = Project.objects.all()[:6]
        
        return context



class AboutListView(ListView):
    model = About
    template_name = 'corporate.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_list"] = About.objects.all()[:1]
        context["sertificate_list"] = Certificates.objects.all()
        context["partners_list"] = Partners.objects.all()
        
        
        return context
    
    



class CareerListView(SuccessMessageMixin,FormMixin,ListView):
    model = Career
    template_name = 'career.html'
    form_class = CareerCsvForm
    success_message = 'Your resume has been accepted and will be returned to you!'
    error_message = 'Invalid form submission.'
    success_url = reverse_lazy('core:career')
    
    
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        form.save()
        context =  super().form_valid(form)
        
        return context
    
    def form_invalid(self,form):
        context = super().form_invalid(form)
        return context
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
    
    
class InnovationsListView(ListView):
    model = Innovations
    template_name = 'news.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class InnovationsDetailView(DetailView):
    model = Innovations
    template_name = 'news-details.html'
    success_url = reverse_lazy("core:news_details")
    
    








class ContactCreateView(SuccessMessageMixin,CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = 'Contact request submitted successfully!'
    error_message = 'Invalid form submission.'
    success_url = reverse_lazy('core:contact')
    
    
    def form_valid(self, form):
    #     message = "{name} / {email} said: ".format(
    #     name=form.cleaned_data.get('name'),
    #     email=form.cleaned_data.get('email'))
    #     message += "\n\n{0}".format(form.cleaned_data.get('message'))
        
        
        
    #     subject = 'Message subject'
    #     send_mail(
    #     subject,
    #     message=message,
    #     from_email='elish777888999@gmail.com',
    #     recipient_list=[settings.EMAIL_HOST_USER],
    #     fail_silently=False
        
    # )
        form.save()
        context =  super().form_valid(form)
        return context
    
    def form_invalid(self,form):
        self.messages.error(self.request,self.error_message)
        context = super().form_invalid(form)
        return context
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address_list"] = Address.objects.all()[:1]
        return context
    