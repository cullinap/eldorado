import sqlite3

def get_all_results():
    conn = sqlite3.connect('database/warehouse.sqlite')
    cur = conn.cursor()

    print(cur.fetchall())

    conn.commit()
    conn.close()



def create_table():
    conn = sqlite3.connect('database/warehouse.sqlite')
    cur = conn.cursor()

    add_col = """
    ALTER TABLE inventory 
    ADD COLUMN (?, ?);
    """
    
    col = str(input('enter a col name: '))
    col_type = input('enter a type: ')
    
    cur.execute(add_col, (col, col_type))
    conn.commit()

    cur.close()
    conn.close()
    

def print_inventory():
    conn = sqlite3.connect('database/warehouse.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM inventory')
    result = cur.fetchall()

    for r in result:
        print(r)

    cur.close()
    conn.close()


def delete_all_inventory():
    conn = sqlite3.connect('database/warehouse.sqlite')
    cur = conn.cursor()

    cur.execute('DELETE FROM inventory;')
    print(f'deleted {cur.rowcount} from table')
    
    conn.commit()
    cur.close()
    conn.close()


