#To create table

edata_to_create = '''CREATE TABLE IF NOT EXISTS edata(InvoiceNO varchar(255), StockCode varchar(255), Description varchar(255), Quantity varchar(255), InvoiceDate varchar(255), UnitPrice varchar(255), CustomerID varchar(255), Country varchar(255));'''



#To insert into table

edata_to_insert = '''INSERT INTO edata VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''