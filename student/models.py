from django.db import models

class Parent(models.Model):
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    parent_number = models.CharField(max_length=20)
    parent_email = models.EmailField(max_length=254)
    present_address = models.TextField()
    parmanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name}-{self.mother_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    student_class = models.CharField(max_length=50)
    section = models.CharField( max_length=50)
    gender = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=False)
    joining_date = models.DateField(auto_now_add=False)
    addmission_number = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.student_id}"