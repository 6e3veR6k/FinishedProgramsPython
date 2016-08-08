import sqlalchemy as sa
import sqlalchemy.dialects.mssql


engine = sa.create_engine('mssql+pyodbc://hq01db05/OrantaSch?driver=SQL+Server+Native+Client+11.0')

engine.echo = False
metadata = sa.MetaData(engine)

dbo_products = sa.Table('ProductTypes', metadata, autoload=True, schema='meta')


def run(smth):
    rs = smth.execute()
    for row in rs:
        print(row)
try:
    s = dbo_products.select(dbo_products.c.Code == '104')
    run(s)
except Exception as Err:
    print('Ok', Err)

