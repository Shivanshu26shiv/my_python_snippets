'''
Question:

We have a squad of 20 probables - from which we have to select the playing 11, and the order at which they go into bat and bowl. 
Read their stats for the last 10 matches from the excel sheet attached ('Team_stats' tab)

Here are the rules -

1. The team should have 5 batsmen, 5 bowlers and 1 all rounder (a player who can both bat and bowl). A player can be categorized in only one of these 3 options
2. A player qualifies as a batsman if his average (runs scored/matches played) is above 15. The more runs scored - the more the probability to get in
3. A player qualifies as a bowler if he has taken more than 5 wickets. The more wickets taken - the more the probability to get in
4. A player qualifies as an allrounder if he has taken more than 7 wickets and his average is more than 10.
5. Batting order is decided by the number of runs scored (descending), not the average.
6. Bowling order is decided by this rule - 2 fast bowlers to start with, then two spinners, and then one fast bowler and the all rounder. The order within them will be decided by the number of wickets taken.
7. The team should consist the captain and the wicketkeeper

Your python script should output the following -
- the 20 probables
- the playing 11
- the batting order (with 'captain' and 'wicketkeeper' in parenthesis besides the player's name)
- the bowling order
'''

from xlrd import open_workbook
from collections import OrderedDict

matches_played=10

book = open_workbook('Questions_Data.xlsx')
def sort_excel(col):
    global data
    target_column = col
    sheet = book.sheets()[0]
    data = [sheet.row_values(i) for i in xrange(sheet.nrows)]
    labels = data[0]
    data = data[1:]
    data.sort(key=lambda x: x[target_column],reverse=True)
    return data

captain=[]
wicket_keeper=[]
sort_excel(2)

#batting
dict_bat=OrderedDict()
for details_bat in data:
    if len(dict_bat)<5 and details_bat[2]/matches_played>15:
        dict_bat[details_bat[0].encode('utf-8')]=details_bat[2]
    if details_bat[1].strip() == 'Batsman+Captain':
        captain=[details_bat[0].encode('utf-8')]+[details_bat[2]]
    if details_bat[1].strip() == 'Batsman+Wicketkeeper':
        wicket_keeper=[details_bat[0].encode('utf-8')]+[details_bat[2]]            
    if captain and wicket_keeper: break
    
if captain[0] not in dict_bat and wicket_keeper[0] not in dict_bat:
    dict_bat.popitem()
    dict_bat.popitem()
    dict_bat[captain[0]]=captain[1]
    dict_bat[wicket_keeper[0]]=wicket_keeper[1]
    
elif captain[0] not in dict_bat:
    if dict_bat.popitem()[0]==wicket_keeper[0]:
        dict_bat.popitem()
        dict_bat[wicket_keeper[0]]=wicket_keeper[1]
    dict_bat[captain[0]]=captain[1]
    
elif wicket_keeper[0] not in dict_bat:
    if dict_bat.popitem()[0]==captain[0]:
        dict_bat.popitem()
        dict_bat[captain[0]]=captain[1]
    dict_bat[wicket_keeper[0]]=wicket_keeper[1]

play11_bat=[]
for elem1 in dict_bat:
    play11_bat.append(elem1)

#bowling
sort_excel(3)
dict_bowl=OrderedDict()
fast=0
spin=0
arflag=0
for details_bowl in data:
       
    if details_bowl[0] not in play11_bat and details_bowl[2]>5:
        bowler_type = details_bowl[1].strip()

        if details_bowl[3]>7 and details_bowl[2]/matches_played>10 and arflag!=1:
            dict_bowl[details_bowl[0].encode('utf-8')]=details_bowl[3]
            arflag=1

        elif (bowler_type=='Fast Bowler' or bowler_type=='Batsman+Fast Bowler') and fast<4:
            dict_bowl[details_bowl[0].encode('utf-8')]=details_bowl[3]
            fast+=1

        elif (bowler_type=='Spin Bowler' or bowler_type=='Batsman+Spin Bowler') and spin<3:
            dict_bowl[details_bowl[0].encode('utf-8')]=details_bowl[3]
            spin+=1
         
        if len(dict_bowl)==6: break
        
temp_str=''
print '20 probables: ',
for prob in data:
    temp_str=temp_str+str(prob[0].encode('utf-8'))+', '
print temp_str.strip(', ')

play11_bowl=[]
for elem2 in dict_bowl:
    play11_bowl.append(elem2)

play11=play11_bowl+play11_bat
print '\nPlaying 11: ', play11[::-1]

print '\nBatting order:'
for elem3 in play11_bat:
    for elem4 in data:
        if elem3 == elem4[0].encode('utf-8'):
            print elem3,'(',elem4[1].encode('utf-8'),') | Runs scored:',int(elem4[2])
            break

print '\nBowling order:'
for elem3 in play11_bowl:
    for elem4 in data:
        if elem3 == elem4[0].encode('utf-8'):
            print elem3,'(',elem4[1].encode('utf-8'),') | Wickets:',int(elem4[3])
            break



