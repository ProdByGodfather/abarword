# import modules
from django.db import models
from django_quill.fields import QuillField


# category class for category of posts
class Category(models.Model):
    title = models.CharField(verbose_name="موضوع", max_length=50)
    slug = models.SlugField(verbose_name="آدرس", max_length=50,unique=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = "دسته بندی"



class Posts(models.Model):
    title = models.CharField(verbose_name="موضوع", max_length=50)
    slug = models.SlugField(verbose_name="آدرس", max_length=50,unique=True)
    body = QuillField(verbose_name="متن")
    category = models.ForeignKey(Category, verbose_name="دسته بندی", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="تاریخ ایجاد", auto_now=True)
    image = models.ImageField(verbose_name="عکس", upload_to="posts/%m",null=True,blank=True)
    best = models.BooleanField(verbose_name=" بهترین مقالات",default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'مقالات'
        verbose_name = "مقاله"

