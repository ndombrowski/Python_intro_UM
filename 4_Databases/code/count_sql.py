import sqlite3

#connect to db, it will create the file if it does not exist
conn = sqlite3.connect('../data/emaildb.sqlite')

#create a database handle
#i.e. we send commands to the cursor and get responses through that cursor
cur = conn.cursor()

#if table exist, delete so we have a fresh start
cur.execute('DROP TABLE IF EXISTS Counts')

#create a new table from fresh
cur.execute('CREATE TABLE counts (email TEXT, count INTEGER)')

fname='../data/mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    
    #extract email addresses
    email = pieces[1]

    #prepare the cursor to receive data:
    #`=?` here, the ? is a placeholder to prevent sql injections
    #the placeholder ultimately will replaced it with a ONE tuple `(email,)`
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    
    #grep the first one and give it back in row
    row = cur.fetchone()

    #if the row is empty insert the mail and an inital count of 1
    # if the row exists, i.e. the mail is already in there, update the counter    
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
   
    #write the db to disk
    conn.commit()

#create string to extract data
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#extract data
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

print('')