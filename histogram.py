import psycopg2 
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT word, count FROM tweetwordcount WHERE count between %d and %d" % (num1,num2))
records = cur.fetchall()
for rec in records:
 print "%s, %d" % (rec[0],rec[1])  
conn.commit()

