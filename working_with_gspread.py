import gspread

sa = gspread.service_account(filename='credentials/service_account.json')

sh = sa.open('Test')

wks = sh.worksheet("Sheet1")

print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

wks.update('A1', 'this is Linh')