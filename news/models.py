from django.conf import settings
from django.db import models
from django.urls import reverse
from uuslug import slugify
from taggit.managers import TaggableManager
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,default='news')
    image = models.ImageField(upload_to='image/%Y/%m/%d',default=None)
    image_url = models.URLField(default=None)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    love_times = models.PositiveIntegerField(default=1)
    good_times = models.PositiveIntegerField(default=0)
    bad_times = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='news_created', on_delete=models.CASCADE)

    TAG_CHOICES = (
        ('tech','Tech'),
        ('life','Life'),
        ('music','Music'),
        ('idol','Idol'),
    )
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)



    def get_absolute_url(self):
        #self.slug = slugify(self.slug)
        return reverse('news:news_detail', args=[
                                            self.created.year,
                                            self.created.strftime('%m'),
                                            self.created.strftime('%d'),
                                            self.slug,
                                                    ])

class Comments(models.Model):
    news = models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comment_user", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Comments by {} on {}".format(self.name,self.news)




class Images(models.Model):
    """
    图片类：
    1 把图片生成url
    2 保存到url到数据库
    3 把图片放到upload
    """
    pass




