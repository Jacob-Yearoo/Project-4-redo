from .models import Comment, Report
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reporter_name', 'reporter_email', 'report_reason']
