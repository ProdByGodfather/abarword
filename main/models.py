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


# posts class
class Posts(models.Model):
    title = models.CharField(verbose_name="موضوع", max_length=50)
    slug = models.SlugField(verbose_name="آدرس", max_length=50,unique=True)
    description = models.TextField(verbose_name="توضیحات کوتاه",blank=True,null=True)
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

# news
class News(models.Model):
    description = models.TextField(verbose_name="متن خبر",max_length=300)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural = 'اخبار'
        verbose_name = "خبر"


class Contact(models.Model):
    email = models.CharField(verbose_name="ایمیل",max_length=400)
    name = models.CharField(verbose_name="نام",max_length=200)
    message = models.TextField(verbose_name='پیغام')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'تماس ها'
        verbose_name = "تماس"

class Emails(models.Model):
    email = models.EmailField(verbose_name="ایمیل",max_length=400, unique=True)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'ایمیل ها'
        verbose_name = "ایمیل"