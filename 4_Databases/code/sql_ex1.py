import sqlite3
import re

#connect to db, it will create the file if it does not exist
conn = sqlite3.connect('orga_info.sqlite')

#create a database handle
#i.e. we send commands to the cursor and get responses through that cursor
cur = conn.cursor()

#if table exist, delete so we have a fresh start
cur.execute('DROP TABLE IF EXISTS Counts')

#create a new table from fresh
cur.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

fname='../data/mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): 
        continue

    #extract orga info
    email = line.split()[1]
    orga = email.split('@')[1]
    print((orga))

    #prepare the cursor to receive data:
    #`=?` here, the ? is a placeholder to prevent sql injections
    #the placeholder ultimately will replaced it with a ONE tuple `(email,)`
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orga,))
    
    #grep the first one and give it back in row
    row = cur.fetchone()

    #if the row is empty insert the mail and an inital count of 1
    # if the row exists, i.e. the mail is already in there, update the counter    
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''', (orga,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(orga,))
   
    #write the db to disk
    conn.commit()

#create string to extract data
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

#view data
##for row in cur.execute(sqlstr):
#    print(str(row[0]), row[1])

#count data 
num_list = list()

for row in cur.execute(sqlstr):
    num = int(row[1])
    num_list.append(num)

print(sum(num_list))