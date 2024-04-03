import psycopg2

try:
    # Verbindung zur Datenbank herstellen und client_encoding festlegen
    conn = psycopg2.connect(
        dbname='weather',
        user='postgres',
        password='miau',
        host='localhost',
        port='5432',
        client_encoding='latin1'  # Hier die gewünschte Zeichenkodierung angeben
    )

    # Cursor erstellen
    cur = conn.cursor()

    # Beispielabfrage ausführen
    cur.execute('SELECT version()')

    # Ergebnis abrufen
    db_version = cur.fetchone()
    print('Datenbankversion:', db_version)

    # Cursor und Verbindung schließen
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print('Fehler beim Verbindungsaufbau zur Datenbank:', e)