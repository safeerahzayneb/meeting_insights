import sqlite3

conn = sqlite3.connect('requests.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS requests
             (id text, response json)''')
conn.close()


def add_data(id, response):
    conn = sqlite3.connect('requests.db')
    sql = ''' INSERT INTO requests(id,response)
              VALUES(?,?) '''
    
    data = (id, response)
    cur = conn.cursor()
    cur.execute(sql, data)
    # c.execute("INSERT INTO requests VALUES(?, ?)", id, response)
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('SELECT response FROM requests ORDER BY id DESC')
    return c.fetchone()

def deel():
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('DELETE FROM requests')
    return
