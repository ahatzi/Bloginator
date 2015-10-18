import sqlite3
from os import listdir
from os.path import isfile, join
import md5

def add(filename, username, title, content):
        if not isfile(join('tables/',filename)):
                file = open('tables/' + filename, 'w+')
                new = sqlite3.connect('tables/' + filename)
                c = new.cursor()
                q = "CREATE TABLE content (user text, title text, content text)"
                c.execute(q)
                new.commit()
                file.close()
        conn = sqlite3.connect('tables/' + filename)
        c = conn.cursor()

        TEMPLATE="INSERT INTO content VALUES ('%(user)s','%(title)s', '%(content)s')"
        q = TEMPLATE%({'user':username,'title':title, 'content':content})
        c.execute(q)
        conn.commit()

def getTables():
        onlyfiles=[f for f in listdir('tables/') if isfile(join('tables/',f))]
        return onlyfiles


def authenticate(uname, pword):
    m = md5.new()
    m.update(pword)
    print 'ok'
    f = open("tables/users.txt",'r')
    for line in f.readlines():
        print line
        if uname == line.split(',')[0] and m.hexdigest() == line.split(',')[1]:
            f.close()
            return True
    f.close()
    return False

def register(uname,pword):
    m=md5.new()
    m.update(pword)
    f = open("tables/users.txt", 'r')
    for line in f.readlines():
        if uname == line.split(',')[0]:
            return False
    f.close()
    f = open("tables/users.txt",'a')
    f.write("%(user)s,%(phash)s\n"%({"user":uname,"phash":m.hexdigest()}))
    f.close()
    return True

add("hi.db","user", "title","content")
add("hi.db","leon", "Something", "hello")

def authenticate(uname, pword):
	if uname =="Sir" and pword == "Loin":
		return True
	else:
		return False

def getposts():
        conn = sqlite3.connect('hi.db')
        c = conn.cursor()
        out = ""
        q = 'SELECT user, title, content FROM content'
        info = c.execute(q).fetchall()
        conn.commit()
        for entry in info:
                out+="<br><h2>"+q[1]+"<\h2><h3>"+q[0]+"<\h3>"+q[2]
        return out
        
