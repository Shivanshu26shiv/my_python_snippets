'''
Purpose: To sdrap wikipedia and validate the input and feed it to a mysql database
By: Shivanshu
'''

import mysql.connector
import wikipedia
import datetime
import re

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='DBname'
)
mycursor = mydb.cursor()

def insert_db():
    sql = 'INSERT INTO `news`(`serial`, `description`, `title`, `timestamp`) VALUES (%s,%s,%s,%s)'
    t = str(datetime.datetime.now()).split('.')[0]
    pieces = elife.split('. ')
    strinp = '.<br><br>'.join([''.join(pieces[i:i+3]) for i in xrange(0,len(pieces),3)])
    strinp = "<b>Source: <a href='"+wpage.url+"' target='_blank'>wikipedia.com</a></b><br><br>"+strinp 
    val = (p_key,strinp,str(wpage.title),t)
    mycursor.execute(sql, val)
    mydb.commit()
    #print p_key,matchObj.group(1)
    print p_key,str(wpage.title)


gi = wikipedia.page('Page_name')
se = gi.section('Sample_section')


sel = se.split('\n')[1:]
p_key = 1

for i in sel:

    '''
    matchObj = re.match( r'(.*)\(',i,re.I)
    if matchObj: i = matchObj.group(1)
    else: continue
    '''
    i = i.partition(',')[0].partition('(')[0].strip()
    
    try:
        wpage = wikipedia.page(i)
    except wikipedia.exceptions.DisambiguationError as e:
        wpage = wikipedia.page(e.options[0])
    except wikipedia.exceptions.PageError as e:
        print 'Error: ',e
        continue

    flag = 0
    elife=wpage.section('Early life and education')    
    if elife == None:
        elife=wpage.section('Education and career')
        if elife == None:
            elife=wpage.section('Early life and career')
            if elife == None: continue
        else:  flag = 1
    else: flag = 1
    
    if flag==1 and len(elife)>=300: insert_db();p_key +=1
    else: continue

