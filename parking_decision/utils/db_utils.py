# Python Imports

# Third parties imports
import sqlalchemy as db

# Local imports

table = 'Table:'
column = '-> Column::'

metadata = db.MetaData()

def get_db_metadate() -> db.MetaData:
    return metadata


def metadata_sorted(table_obj):
    for t in table_obj.metadata.sorted_tables:
        print(table, t.name)
        for c in t.c.keys():
            print(column, c)


def table_primary_keys(table_obj):
    # get the table's primary key columns
    for t in table_obj.metadata.sorted_tables:
        print(table, t.name)
        for p_key in t.primary_key:
            print('Primary Key:', p_key)


def table_foreign_keys(table_obj):
    # get the table's foreign key objects:
    for t in table_obj.metadata.sorted_tables:
        print(table, t.name)
        for f_key in t.foreign_keys:
            print("Foreign Key:", f_key)
