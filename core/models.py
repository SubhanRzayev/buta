from re import T
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.



class Partners(models.Model):
    image = models.FileField(upload_to='media')
    
    
    class Meta:
        verbose_name_plural = 'Tərəfdaşlarımız'
        
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'



class Project(models.Model):
    #relation
    
    categories = models.ForeignKey('ProjectCategory',on_delete=models.SET_NULL,blank=True,null=True,related_name='project_categories')
    category = models.ForeignKey('ConditionCategory',on_delete=models.CASCADE,blank=True,null=True,related_name='condition_categories')
    
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    condition = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='media')
    
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Layihələr'
        
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.project_image.url))
    image_tag.short_description = 'Image'
    
    
    
    def get_absolute_url(self):
        return reverse("core:case_detail", kwargs={
            'slug':self.slug
        })
        
        
        
        
class ProjectCategory(models.Model):
    name = models.CharField(max_length=120,blank=True,null=True)
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    
    
    
    
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("core:project_category", args=[self.slug,])
    
    class Meta:
        verbose_name_plural = 'Project Categories'




class ConditionCategory(models.Model):
    
    name = models.CharField(max_length=50,blank=True,null=True)
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:cases_category", args=[self.slug,])
    
    
    

    
    
    



class Service(models.Model):
    service_icon_image = models.FileField(upload_to='media')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    service_content = RichTextUploadingField()
    service_content_image = models.ImageField(upload_to='media',default='JPG')
    
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    service_head_image = models.ImageField(upload_to='media')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Xidmətlər'
        ordering = ('id',)
    
    
    def get_absolute_url(self):
        return reverse("core:service_detail", kwargs={
            'slug':self.slug
        })        
        
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.service_head_image.url))
    image_tag.short_description = 'Image'
    
    
    
    


    


class ServiceCategory(models.Model):
    service = models.ManyToManyField('Service',db_index=True,blank=True,related_name='service_title',default=None)
    title = models.CharField(max_length=120,blank=True,null=True)
    description = models.TextField(max_length=2000,blank=True,null=True)
    image = models.FileField(upload_to='media',blank=True,null=True,default="JPG")
    
    
    
    def __str__(self):
        return self.title
    
    
    
    
    class Meta:
        verbose_name_plural = 'Xidmət Categories'
        
        

        
    
        


    



class About(models.Model):
    content_about = RichTextUploadingField()
    mission_description = models.TextField(max_length=3000)
    
    class Meta:
        verbose_name_plural = 'Haqqımızda'
        
        
    def __str__(self):
        return self.mission_description
    
        


class Certificates(models.Model):
    sertificate_image = models.FileField(upload_to='media',blank=True,null=True)
    name = models.CharField(max_length=200)
    pdfile = models.FileField(upload_to='pdf',blank=True,null=True)
    
    def __str__(self):  
        return str(self.pdfile)
    
    
    class Meta:
        verbose_name_plural = 'Sertifikatlar'  
    
    
    
class Image(models.Model):
    projects_images = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True,related_name='projects_images')
    image = models.ImageField(upload_to='images')


    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'




class Address(models.Model):
    address = models.CharField(max_length=200,default='Xəzər rayonu, Binə Sovxoz Sahəsi')
    phone_number = models.CharField(max_length=200,default='+994 51 201 85 70')
    email = models.EmailField(default='INFO@BUTACONSTRUCTION.COM',blank=True)
    
    
    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Address'
        
        

class Contact(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    message = models.TextField(max_length=1000)
    
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Əlaqə'
        
        
    

class CareerCsv(models.Model):
    career = models.ForeignKey('Career',on_delete=models.CASCADE,related_name='careers',blank=True,null=True)
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=120)
    cv = models.FileField(upload_to='career/cvler/')
    
    
    def __str__(self):
        return str(self.career) 
    
    
    
class Career(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Vakansiyalar'
    
    
class Innovations(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    news_image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Yenilikler'
    
    
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.news_image.url))


    def get_absolute_url(self):
        return reverse("core:news_details", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title    
    
    
    
    