import psycopg2 
import sys

print('program parguments:', sys.argv)


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
if len(sys.argv) == 1:
 cur.execute("SELECT word, count FROM tweetwordcount ORDER BY UPPER(word)")
 records = cur.fetchall()
 for rec in records:
  print "%s, %d" % (rec[0],rec[1])  
 conn.commit()
else:
 cur.execute("SELECT count FROM tweetwordcount WHERE word='%s'" % (sys.argv[1]))
 records = cur.fetchall()
 for rec in records:
  print "Total numer of occurences of %s: %d" % (sys.argv[1],rec[0])
 conn.commit()
