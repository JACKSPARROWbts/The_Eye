from django.db import models
from .utils import get_filtered_images
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
ACTION_CHOICES=(
    ('NO_FILER','no filter'),
    ('COLORIZED','colorized'),
    ('GRAYSCALE','grayscale'),
    ('BLURRED','blurred'),
    ('BINARY','binary'),
    ('INVERT','invert'),
    ('DELETE','delete')
)
# Create your models here.
class Upload(models.Model):
    image=models.ImageField(upload_to='images',default='/images/default.png',blank=True)
    action=models.CharField(max_length=50,choices=ACTION_CHOICES)
    updated=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    def save(self,*args,**kwargs):
        pil_img=Image.open(self.image)
        cv_img=np.array(pil_img)
        img=get_filtered_images(cv_img,self.action)
        img_pil=Image.fromarray(img)
        buffer=BytesIO()
        img_pil.save(buffer,format='png')
        image_png=buffer.getvalue()
        self.image.save(str(self.image),ContentFile(image_png),save=False)
        super().save(*args,**kwargs)