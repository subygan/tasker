from django.db import models
from django.utils import timezone

STATUS = (
    (0, "unpicked"),
    (1, "progressing"),
    (2, "completed")
)


class Profile(models.Model):

    username = models.CharField('username of the user', max_length=50, unique=True)
    # Still am guilty about this
    password = models.CharField('password of the user', max_length=50)
    first_name = models.CharField('first name of the user', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    bio = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_password(self):

        return self.password

    def get_data(self):

        data = {
            'username': self.username,
            'first_name': self.password,
            'last_name': self.last_name,
            'bio': self.bio,

        }

        return data

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.password


class Task(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField('Task Title', max_length=50)
    description = models.CharField('Task description', max_length=50)
    start_time = models.DateTimeField('Start time of task', default=timezone.now)
    completion_time = models.DateTimeField('completion time')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
