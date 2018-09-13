from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateField()
    def __str__(self):
        return self.text
    class Meta:
        ordering = ('-pub_date',)

    def jumlah_peserta_poll(self):
        return self.vote_set.count()

    def user_sudah_voting(self, user):
        user_vote = user.vote_set.all()
        sudah_vote_poll_ini = user_vote.filter(poll=self)
        if sudah_vote_poll_ini.exists():
            return True
        return False


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Choice(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

    def jumlah_pemilih_choice(self):
        return self.vote_set.count()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
