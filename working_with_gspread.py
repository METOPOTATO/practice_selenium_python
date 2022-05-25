# https://www.youtube.com/watch?v=bu5wXjz2KvU
import gspread

sa = gspread.service_account(filename='credentials/service_account.json')

# sh = sa.create('Hello')
sh = sa.open('Test')

wks = sh.worksheet("Sheet1")

print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

wks.update('A1', 'this is Linh')
wks.update('A2', 'this is Linh')
wks.update('A3', 'this is Linh')