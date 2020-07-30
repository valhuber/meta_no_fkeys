# meta_no_fkeys

This is to explore why the following code (in `helloNW.py`) results in `meta` with no `foreign_keys`:

```
log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw1.db"   #  metadata
engine = sqlalchemy.create_engine(conn_string)  #  'sqlite:///nw1.db')

connection = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)
```
