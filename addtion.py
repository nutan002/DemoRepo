from flask import the flask,render_template
from werkzeug.contrib.atom import AtomFeed
import datetime

app=flask(__name__)
pasts=[
    {
        'title':'post 1',
        'content':'This is content of post 1',
        'date':datetime.datetime(2023,1,1),
    },
    {
        'title':'post 2',
        'content':'This is content of post 2',
        'date':datetime.datetime(2023,2,1),
    },
    ]

@app.rout('/feed')
def feed():
    feed=AtomFeed(MyBlog feed_url='https://yourblog.com/feed',url='https://yourblog.com')

    for post in posts:
        feed.add(post['title'])
