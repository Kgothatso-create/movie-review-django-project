from django.db import models

# Create your models here.
class Question(models.Model):
    """
    A class representing a poll question.

    Attributes:
        question_text (str): The text of the poll question.
        pub_date (datetime): The date and time when the poll question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns a string representation of the poll question.
        """
        return self.question_text

class Choice(models.Model):
    """
    A class representing a choice in a poll.

    Attributes:
        question (Question): The poll question that this choice is associated with.
        choice_text (str): The text of the poll choice.
        votes (int): The number of votes that this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the poll choice.
        """
        return self.choice_text