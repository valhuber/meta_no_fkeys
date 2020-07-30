import logging
import nwmodels

import sys
import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import select, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base


log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw1.db"   #  metadata
engine = sqlalchemy.create_engine(conn_string)  #  'sqlite:///nw1.db')

connection = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)

items = meta.tables.items()  # stop here - meta has no foreign_keys for Order
for each_table in items:
    o = each_table[1]
    print("\nname", o.name)

custs = Table('Customer', meta, autoload = True, autoload_with = engine)
stmt = select([custs])  #  .where(table.columns.column_name == 'filter')

results = connection.execute(stmt).fetchall()
print(results)