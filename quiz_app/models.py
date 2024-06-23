from django.db import models


class User(models.Model):
    USER_CATEGORIES = [
        ('ST', 'STUDENT'),
        ('TC', 'TEACHER'),
        ('FnF', 'FAMILY_AND_FRIENDS'),
        ('PR', 'PROFESSIONAL'),
    ]
    user_category = models.CharField(max_length=1, choices=USER_CATEGORIES, default='ST')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Quiz(models.Model):
    USER_CATEGORIES = [
        ('ST', 'STUDENT'),
        ('TC', 'TEACHER'),
        ('FnF', 'FAMILY_AND_FRIENDS'),
        ('PR', 'PROFESSIONAL'),
    ]
    quiz_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_created = models.DateTimeField(auto_now_add=True)
    questions = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
        ('T/F', 'True or False'),
        ('ST', 'Short Text'),
    ]
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES, default='MC')
    question_text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    answer_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    time_submitted = models.DateTimeField(auto_now_add=True)
    answer = models.ManyToManyField(Answer, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return f'This answer submission is by {self.user.username} for {self.quiz.title}'
