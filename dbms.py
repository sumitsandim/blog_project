import pymysql as p


def connect():
    return p.connect(host='localhost', user='root', password='', database='Blog_project', port=3306)


def insert_author(t):
    con = connect()
    cur = con.cursor()
    Q = 'insert into authors(username,password,city,email) values(%s,%s,%s,%s)'
    cur.execute(Q, t)
    created = True
    con.commit()
    con.close()
    return created


def insert_user(t):
    con = connect()
    cur = con.cursor()
    Q = 'insert into users(username,password,city,email) values(%s,%s,%s,%s)'
    cur.execute(Q, t)
    created = True
    con.commit()
    con.close()
    return created


def check_userdb(email):
    con = connect()
    cur = con.cursor()
    Q = 'select email,password from users where email = %s'
    cur.execute(Q, email)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


def check_authordb(email):
    con = connect()
    cur = con.cursor()
    Q = 'select email,password from authors where email = %s'
    Q1 = 'select username from authors where email = %s'
    cur.execute(Q, email)
    data = cur.fetchall()
    cur.execute(Q1, email)
    username = cur.fetchall()
    con.commit()
    con.close()
    return data, username[0][0]


def get_postdb(**kwargs):
    con = connect()
    cur = con.cursor()
    if kwargs['id'] == None and kwargs['username'] != None:
        Q = 'select username from authors where username = %s'
        cur.execute(Q, kwargs['username'])
        username = cur.fetchall()
        Q = 'select * from author_posts where username = %s'
        cur.execute(Q, username[0][0])
        post = cur.fetchall()
    if kwargs['id'] != None and kwargs['username'] == None:
        Q = 'select * from author_posts where id = %s'
        cur.execute(Q, kwargs['id'])
        post = cur.fetchall()
    con.commit()
    con.close()
    return post


def insert_post(t):
    con = connect()
    cur = con.cursor()
    Q = 'insert into author_posts(username,title,post) values(%s,%s,%s)'
    cur.execute(Q, t)
    con.commit()
    con.close()


def get_allpostdb():
    con = connect()
    cur = con.cursor()
    Q = 'select * from author_posts'
    cur.execute(Q) 
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


def update_postdb(t):
    con = connect()
    cur = con.cursor()
    Q = 'update author_posts set title=%s, post=%s where id=%s'
    cur.execute(Q, t)
    con.commit()
    con.close()


def delete_postdb(id):
    con = connect()
    cur = con.cursor()
    Q = 'select username from author_posts where id = %s'
    cur.execute(Q, id)
    username = cur.fetchall()
    Q1 = 'delete from author_posts where id=%s'
    cur.execute(Q1, id)
    con.commit()
    con.close()
    return username
