from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	uid = models.IntegerField(primary_key=True)
	otp_enabled = models.BooleanField(default=False, null=True)
	password = models.CharField(max_length=128, null=True, blank=True)
	refresh_token = models.CharField(max_length=1024, null=True, blank=True)
	win = models.IntegerField(default=0)
	lose = models.IntegerField(default=0)
	multi_nickname = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self):
		return self.username
	def update_two_factor(self,otp_enabled):
		self.otp_enabled = otp_enabled
		self.save()
	def update_refresh_token(self, refresh_token):
		self.refresh_token = refresh_token
		self.save()


class FollowList(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	following_username = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self):
		return f'{self.user} follows {self.following_uid}'
	
	def save(self, *args, **kwargs):
		if self.user.username == self.following_username:
			raise Exception('자기 자신을 친구로 추가할 수 없습니다.')
		if FollowList.objects.filter(user=self.user, following_username=self.following_username).exists():
			raise Exception('이미 친구로 추가된 사용자입니다.')
		super().save(*args, **kwargs)
