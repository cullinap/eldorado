import sqlite3


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
