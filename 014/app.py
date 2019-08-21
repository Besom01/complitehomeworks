from flask import jsonify, request, render_template
from jinja2 import Template
from models import Post, Comment, db, app
from forms import PostForm, CommentForm






@app.route('/createpost', methods = ['POST'])
def post_create():    
    if request.method == 'POST':
        p_form = PostForm(request.args)
        if p_form.validate():
            post = Post(**request.args)
            db.session.add(post)
            db.session.commit()
            return render_template('create_post.txt', post = post)
        else:
            return jsonify(p_form.errors)

@app.route('/createcomment', methods = ['POST'])
def comment_create():
    if request.method == 'POST':
        c_form = CommentForm(request.args)
        if c_form.validate():
            comment = Comment(post = Post.query.filter_by(id = request.args['id_post']).first(), 
                            comment_content = request.args['comment_content'], 
                            id_post = request.args['id_post'])
            db.session.add(comment)
            db.session.commit()
            all_comments_post = Comment.query.filter_by(id_post = request.args['id_post']).all()
            return render_template('create_comment.txt', comment = comment, all_comments_post = all_comments_post)
        else:
            return jsonify(c_form.errors)

# @app.route('/')
# def index():
#     posts = GuessBookItem.query.all()
#     return jsonify([p.to_dict() for p in posts])


if __name__ == '__main__':
    db.create_all()
    app.run()
