# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30,verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    uphone = models.CharField(max_length=11,verbose_name='手机号')
    upwd = models.CharField(max_length=30,verbose_name='密码')


    def __repr__(self):
        return "<User:%r>" % self.uname

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Category(models.Model):
    category = models.CharField(max_length=30,verbose_name='电影分类')

    def __repr__(self):
        return "<Category:%r>" % self.category

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'category'
        verbose_name = '电影类别'
        verbose_name_plural = verbose_name


class Films(models.Model):
    film = models.CharField(max_length=30,verbose_name='电影名字')
    picture = models.ImageField(upload_to='static/upload/picture',null=True,verbose_name='影片图片')
    show_date = models.DateField(verbose_name='上映时间')
    director = models.CharField(max_length=30,verbose_name='导演')
    screenwriter = models.CharField(max_length=100,verbose_name='编剧')
    type = models.CharField(max_length=30,verbose_name='电影类型')
    long_time = models.CharField(max_length=30,verbose_name='电影时长')
    stars = models.CharField(max_length=200,verbose_name='主演')
    synopsis = models.TextField(verbose_name='剧情介绍')
    movie_score = models.FloatField(verbose_name='评分')
    release_date = models.DateField(auto_now=True,verbose_name='发表时间')
    # 添加外键对应category uname
    category = models.ForeignKey(Category)
    user = models.ManyToManyField(User)

    def __repr__(self):
        return "<Films:%r>" % self.film

    def __str__(self):
        return self.film

    class Meta:
        db_table = 'films'
        verbose_name = '影片'
        verbose_name_plural = verbose_name
        ordering = ['-movie_score']


class Info(models.Model):
    read_number = models.IntegerField(default=0,verbose_name='已阅读')
    like_number = models.IntegerField(default=0,verbose_name='点赞数')
    reply_number = models.IntegerField(default=0,verbose_name='评论次数')
    # 添加外键 对应user film category
    user = models.ForeignKey(User)
    film = models.ForeignKey(Films)

    class Meta:
        db_table = 'info'
        verbose_name = '影片信息'
        verbose_name_plural = verbose_name


class Reply(models.Model):
    content = models.TextField(verbose_name='回复内容')
    reply_date = models.DateField(auto_now=True,verbose_name='回复时间')

    user = models.ForeignKey(User)
    film = models.ForeignKey(Films)

    class Meta:
        db_table = 'reply'
        verbose_name = '回复'
        verbose_name_plural = verbose_name



# class Release(models.Model):
#     pass