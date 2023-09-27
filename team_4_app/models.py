from django.db import models

class PromotionalVideo(models.Model):
    title = models.CharField('title', max_length=100, )
    description = models.TextField('description')
    video_url = models.TextField('video_url')
    shop_code = models.CharField('shop_code', max_length=100, )

    def __str__(self):
        return self.title
