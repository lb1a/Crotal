import os
import sys
from unipath import Path
from _models.posts import Posts
from templates import Views
from copydir import copyDir

posts = []
categories = []

def get_path():
    dir = Path(__file__).ancestor(1).absolute()
    posts_titles = os.listdir(dir.child('_posts'))
    templates = os.listdir(dir)
    categories_tmp = []
    for post_title in posts_titles:
        post_tmp = Posts()
        post_tmp.save(open(dir + '/_posts/' + post_title, 'r').read().decode('utf8'))
        posts.append(post_tmp)
        for category in post_tmp.categories:
            categories_tmp.append(category)

    categories = sorted({}.fromkeys(categories_tmp).keys())
    posts_sort()
    view = Views()
    view.save(posts, categories)
    view.save_posts(posts)
    view.save_get_more(posts)

def posts_sort():
    for i in range(len(posts)):
        for j in range(len(posts)):
            if  posts[i].pub_time > posts[j].pub_time:
                posts[i] ,posts[j] = posts[j], posts[i]

if __name__ == '__main__':
    flag = 0
    if len(sys.argv) == 1:
        print 'Usage: make'

    elif len(sys.argv) != 1:
        if sys.argv[1] == 'make':
            copyDir('_static','_sites')
            print 'Static Files Copied.'
            get_path()
            print 'Site Generated.'

    else:
        usraccount = sys.argv[1]
        passwd = sys.argv[2]