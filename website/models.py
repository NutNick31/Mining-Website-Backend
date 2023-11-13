from django.db import models

class research_area(models.Model):
    topic=models.CharField(max_length=100)
    faculties=models.TextField(blank=True)
    broad_research_area=models.TextField(blank=True)
    # description=models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Research Area'
        verbose_name_plural = 'Research Areas'
    
    def __str__(self):
        return self.topic


class research_area_image(models.Model):
    research_area = models.ForeignKey(research_area,related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="research_area", blank=True)
    description = models.TextField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'Reseach Area Image'
        verbose_name_plural = 'Reseach Area Images'
    
    def __str__(self):
        return self.research_area.topic

class faculty_member(models.Model):
    name = models.CharField(max_length=100)
    phd_college = models.CharField(max_length=100)
    research_area = models.TextField(blank=True) 
    institute_webpage = models.CharField(max_length=100,blank=True)
    personal_website = models.CharField(max_length=100,blank=True)
    email_id=models.EmailField(max_length=100)
    image=models.ImageField(upload_to="faculty_members", blank=True)

    class Meta:
        verbose_name = 'Faculty Member'
        verbose_name_plural = 'Faculty Members'
    
    def __str__(self):
        return self.name

    
class staff_member(models.Model):
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100, null=True, blank=True)
    contact=models.CharField(max_length=100,blank=True)
    lab=models.CharField(max_length=100, blank=True)
    image=models.ImageField(upload_to="staff_members", blank=True)

    class Meta:
        verbose_name = 'Staff Member'
        verbose_name_plural = 'Staff Members'
    
    def __str__(self):
        return self.name

  
class research_scholar(models.Model):
    name=models.CharField(max_length=100)
    research_area=models.CharField(max_length=100)
    # supervisor=models.CharField(max_length=100)
    # personal_website = models.CharField(max_length=100,blank=True)
    # email_id=models.EmailField(max_length=100,blank=True)
    image=models.ImageField(upload_to="research_scholars", blank=True)

    class Meta:
        verbose_name = 'Research Scholar'
        verbose_name_plural = 'Research Scholars'
    
    def __str__(self):
        return self.name


class event(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True,null=True)
    concluded = models.BooleanField(default=False)
    dated_at = models.DateField(blank=True,null=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return self.name
    

class gallery(models.Model):
    image = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return self.name


class education(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return self.name


class society(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    link = models.CharField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'Society'
        verbose_name_plural = 'Societies'
    
    def __str__(self):
        return self.name

