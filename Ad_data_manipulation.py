import xlwt
from xlwt import Workbook
from xlrd import open_workbook

book = open_workbook('Ad_data_manipulation.xlsx')

data=[]
target_column = 2
sheet = book.sheets()[1]
data = [sheet.row_values(i) for i in xrange(sheet.nrows)]
labels = data[0]
data = data[1:]

bk = xlwt.Workbook()
sheet = bk.add_sheet(sheet.name)

style = xlwt.XFStyle()
font = xlwt.Font()
font.bold = True
style.font = font

for idx, label in enumerate(labels):
     sheet.write(0, idx, label, style)

sheet.write(0, idx+1, 'New bids', style)
sheet.write(0, idx+2, 'New budgets', style)
sheet.write(0, idx+3, 'New status', style)

print 'Program started'
sum_amt_spent=0

for idx_r, row in enumerate(data):
    sum_amt_spent=sum_amt_spent+row[1]

for idx_r, row in enumerate(data):
    row = row + ['']*3
    for idx_c, value in enumerate(row):
        if row[8].encode('utf-8')=='Active':
            
            if isinstance(row[4],float): reg=row[4]
            else: reg=1
            if isinstance(row[4],float): amt=row[1]
            else: amt=0

            cpr=amt/reg
            
            if (cpr)<3:
                if amt<=200:
                    row[9]=row[6]+(0.12*row[6])
                    row[10]=row[7]+(0.12*row[7])
                else:
                    row[9]=row[6]+(0.18*row[6])
                    row[10]=row[7]+(0.18*row[7])
            elif cpr<4 and cpr>=3:
                row[9]=row[6]+(0.10*row[6])
                row[10]=row[7]+(0.10*row[7])
            elif cpr<5.5 and cpr>=4:
                row[9]=row[6]-(0.10*row[6])
                row[10]=row[7]-(0.15*row[7])
            elif cpr<8 and cpr>=5.5:
                row[9]=row[6]-(0.20*row[6])
                row[10]=row[7]-(0.25*row[7])

            if amt<=(0.01*sum_amt_spent):
                row[9]=row[6]+(0.05*row[6])

            if row[0].find('E')>=0:
                row[9]=row[6]+(0.15*row[6])
                
            if cpr>=8: row[11]='Inactive'
              
            if  row[6]>6: row[6]=6
            if  row[6]<3: row[6]=3
            if  row[7]>150: row[7]=150
            if  row[7]<10: row[7]=10

            if row[5]: row[10]=row[7]*1.5
                    
        sheet.write(idx_r+1, idx_c, value)
        
bk.save('ad_result.xls')
print 'Program ended'

