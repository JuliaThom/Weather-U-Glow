import pg8000

try:
    # Verbindung zur Datenbank herstellen
    conn = pg8000.connect(
        user='postgres',
        password='Monster',
        host='localhost',
        port=5432,
        database='weather'
    )

    # Cursor erstellen
    cursor = conn.cursor()

    # Beispielabfrage ausführen
    cursor.execute('SELECT version()')

    # Ergebnis abrufen
    db_version = cursor.fetchone()
    print('Datenbankversion:', db_version)

    # Cursor und Verbindung schließen
    cursor.close()
    conn.close()

except Exception as e:
    print('Fehler beim Verbindungsaufbau zur Datenbank:', e)