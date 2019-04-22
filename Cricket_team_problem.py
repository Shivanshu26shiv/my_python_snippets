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



