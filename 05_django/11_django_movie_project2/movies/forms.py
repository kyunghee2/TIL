from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):    
    #메타데이터 :  데이터의 데이터
    #ex) 사진 한장 (촬영장비이름, 촬영환경 등)
    score = forms.IntegerField(min_value=0,max_value=10)
    content = forms.CharField(
        label='평점',
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용입력',
                'rows':5,
                'cols':30
            }
        )
    )
    class Meta:
        model = Rating
        fields = ('score','content',) 