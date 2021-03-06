from django import forms
from .models import Article
from .models import Comment
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         # HTML Tag와 동일
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title',
#                 'placeholder':'제목을 입력해 주세요...!',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
#         widget=forms.Textarea(
#             attrs={
#                 'class':'content',
#                 'placeholder':'내용을 입력해 주세요오오오옹',
#                 'rows':5,
#                 'cols':30,
#             }
#         )
#     )
# ModelForm
# 1. ModelForm 클래스를 상속받아 사용한다
# 2. 메타데이터로 Model정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다
class ArticleForm(forms.ModelForm):
    #메타데이터 :  데이터의 데이터
    #ex) 사진 한장 (촬영장비이름, 촬영환경 등)
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'제목입력'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        max_length=10,
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
        model = Article
        #fields = '__all__' #전체가져오기
        fields = ('title','content',) #선택해서 데이터 가져오기

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'댓글입력',
                'rows':5,
                'cols':30
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
