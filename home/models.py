from django.db import models

class Phase(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    is_active = models.BooleanField(default=False) 

    def __str__(self):
        return self.name
    
class UserSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organisation = models.CharField(max_length=200)
    rollno = models.CharField(max_length=20)
    consent = models.CharField(max_length=10, default="Yes")
    
    error_description_11 = models.CharField(max_length=10)
    understandability11 = models.IntegerField(default=0)
    error_description_12 = models.CharField(max_length=10)
    understandability12 = models.IntegerField(default=0)
    
    error_description_21 = models.CharField(max_length=10)
    understandability21 = models.IntegerField(default=0)
    error_description_22 = models.CharField(max_length=10)
    understandability22 = models.IntegerField(default=0)
    
    error_description_31 = models.CharField(max_length=10)
    understandability31 = models.IntegerField(default=0)
    error_description_32 = models.CharField(max_length=10)
    understandability32 = models.IntegerField(default=0)
    
    error_description_41 = models.CharField(max_length=10)
    understandability41 = models.IntegerField(default=0)
    error_description_42 = models.CharField(max_length=10)
    understandability42 = models.IntegerField(default=0)
    
    error_description_51 = models.CharField(max_length=10)
    understandability51 = models.IntegerField(default=0)
    error_description_52 = models.CharField(max_length=10)
    understandability52 = models.IntegerField(default=0)
    
    error_description_61 = models.CharField(max_length=10)
    understandability61 = models.IntegerField(default=0)
    error_description_62 = models.CharField(max_length=10)
    understandability62 = models.IntegerField(default=0)
    
    error_description_71 = models.CharField(max_length=10)
    understandability71 = models.IntegerField(default=0)
    error_description_72 = models.CharField(max_length=10)
    understandability72 = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class TASubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organisation = models.CharField(max_length=200)
    rollno = models.CharField(max_length=20)
    consent = models.CharField(max_length=10, default="Yes")
    
    feedback11_rating = models.IntegerField(default=0)
    feedback12_rating = models.IntegerField(default=0)
    feedback13_rating = models.IntegerField(default=0)
    feedback14_rating = models.IntegerField(default=0)
    feedback15_rating = models.IntegerField(default=0)
    feedback16_rating = models.IntegerField(default=0)
    feedback17_rating = models.IntegerField(default=0)
    
    feedback21_rating = models.IntegerField(default=0)
    feedback22_rating = models.IntegerField(default=0)
    feedback23_rating = models.IntegerField(default=0)
    feedback24_rating = models.IntegerField(default=0)
    feedback25_rating = models.IntegerField(default=0)
    feedback26_rating = models.IntegerField(default=0)
    feedback27_rating = models.IntegerField(default=0)
    
    feedback31_rating = models.IntegerField(default=0)
    feedback32_rating = models.IntegerField(default=0)
    feedback33_rating = models.IntegerField(default=0)
    feedback34_rating = models.IntegerField(default=0)
    feedback35_rating = models.IntegerField(default=0)
    feedback36_rating = models.IntegerField(default=0)
    feedback37_rating = models.IntegerField(default=0)
    
    feedback41_rating = models.IntegerField(default=0)
    feedback42_rating = models.IntegerField(default=0)
    feedback43_rating = models.IntegerField(default=0)
    feedback44_rating = models.IntegerField(default=0)
    feedback45_rating = models.IntegerField(default=0)
    feedback46_rating = models.IntegerField(default=0)
    feedback47_rating = models.IntegerField(default=0)
    
    feedback51_rating = models.IntegerField(default=0)
    feedback52_rating = models.IntegerField(default=0)
    feedback53_rating = models.IntegerField(default=0)
    feedback54_rating = models.IntegerField(default=0)
    feedback55_rating = models.IntegerField(default=0)
    feedback56_rating = models.IntegerField(default=0)
    feedback57_rating = models.IntegerField(default=0)
    
    feedback61_rating = models.IntegerField(default=0)
    feedback62_rating = models.IntegerField(default=0)
    feedback63_rating = models.IntegerField(default=0)
    feedback64_rating = models.IntegerField(default=0)
    feedback65_rating = models.IntegerField(default=0)
    feedback66_rating = models.IntegerField(default=0)
    feedback67_rating = models.IntegerField(default=0)
    
    feedback71_rating = models.IntegerField(default=0)
    feedback72_rating = models.IntegerField(default=0)
    feedback73_rating = models.IntegerField(default=0)
    feedback74_rating = models.IntegerField(default=0)
    feedback75_rating = models.IntegerField(default=0)
    feedback76_rating = models.IntegerField(default=0)
    feedback77_rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class TAFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organisation = models.CharField(max_length=200)
    rollno = models.CharField(max_length=20)
    consent = models.CharField(max_length=10, default="Yes")
    
    ta_feedback1 = models.TextField()
    ta_feedback2 = models.TextField()
    ta_feedback3 = models.TextField()
    ta_feedback4 = models.TextField()
    ta_feedback5 = models.TextField()
    ta_feedback6 = models.TextField()
    ta_feedback7 = models.TextField()
    
    taproblem1_elapsed_time = models.IntegerField() 
    taproblem2_elapsed_time = models.IntegerField() 
    taproblem3_elapsed_time = models.IntegerField() 
    taproblem4_elapsed_time = models.IntegerField() 
    taproblem5_elapsed_time = models.IntegerField() 
    taproblem6_elapsed_time = models.IntegerField() 
    taproblem7_elapsed_time = models.IntegerField() 
    
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    problem_id = models.IntegerField()
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    content5 = models.TextField()
    consent = models.CharField(max_length=10, default="Yes")