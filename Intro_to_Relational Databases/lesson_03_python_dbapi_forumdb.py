#
# Database access functions for the web forum.
# 
import time
import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum");
    c = DB.cursor();
    query = "SELECT content, time FROM posts ORDER BY time DESC"
    c.execute(query);
    rows = c.fetchall();
    DB.close();
    # formatting output as a dictionary
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in rows]
    return posts;

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum");
    c = DB.cursor();
    cleanContent = bleach.clean(content);
    c.execute("INSERT INTO posts (content) VALUES (%s)", (cleanContent,));
    DB.commit();
    DB.close();
