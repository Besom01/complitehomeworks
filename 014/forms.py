from models import Post, Comment
from wtforms_alchemy import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        include = ['id_post']