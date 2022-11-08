
from flask import *
from dbms import *

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/author-interface/<username>/post-form')
def post_form(username):
    return render_template('post_form.html', username=username, old_post=False)


@app.route('/author-interface/<username>')
def author_dashboard(username):
    return render_template('author_interface.html', username=username)


@app.route('/post/<username>')
def get_post(username):
    posts = get_postdb(id=None, username=username)
    return render_template('author_post.html', posts = posts, username=username)
get_postdb


@app.route('/user-registration')
def user_register():
    return render_template('/user_registration.html')


@app.route('/user-login')
def user_login():
    return render_template('/user_login.html')


@app.route('/author-registration')
def author_registration():
    return render_template('author_registration.html')


@app.route('/author-login')
def author_login():
    return render_template('/author_login.html')


@app.route('/check-user', methods=['post'])
def check_user():
    email = request.form['email']
    password = request.form['password']
    t = (email, password)
    t1 = check_userdb(email)
    if t in t1:
        return redirect('/all-post')
    else:
        return redirect('/user-login')


@app.route('/check-author', methods=['post'])
def check_author():
    email = request.form['email']
    password = request.form['password']
    t = (email, password)
    t1, u = check_authordb(email)
    if t in t1:
        return redirect(url_for('author_dashboard', username=u))
    else:
        return redirect('/author-login')


@app.route('/create-post', methods=['post'])
def create_post():
    username = request.form['username']
    title = request.form['title']
    post = request.form['post']
    t = (username, title, post)
    insert_post(t)
    return redirect(url_for('get_post', username=username))


@app.route('/create-author', methods=['post'])
def create_author():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    city = request.form['city']
    t = (username, password, city, email)
    if insert_author(t):
        return redirect(url_for('author_dashboard', username=username))
    else:
        return redirect('/author-registration')


@app.route('/create-user', methods=['post'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    city = request.form['city']
    t = (username, password, city, email)
    if insert_user(t):
        return redirect('/all-post')
    else:
        return redirect('/user-registration')


@app.route('/all-post')
def get_allpost():
    posts = get_allpostdb()
    return render_template('all_post.html', posts=posts)


@app.route('/edit')
def get_postforupdate():
    id = request.args.get('id')
    post = get_postdb(id=id, username=None)
    return render_template('post_form.html', old_post=post[0])


@app.route('/edit-post', methods=['post'])
def update_post():
    id = request.args.get('id')
    username = request.form['username']
    title = request.form['title']
    post = request.form['post']
    t = (title, post, id)
    update_postdb(t)
    return redirect(url_for('get_post', username=username))


@app.route('/trash')
def delete_post():
    id = request.args.get('id')
    username = delete_postdb(id)
    print(username)
    return redirect(url_for('get_post', username=username[0][0]))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
