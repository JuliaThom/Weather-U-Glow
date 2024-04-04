import pg8000
# Importieren des pg8000-Moduls,
# das zur Verbindung mit einer PostgreSQL-Datenbank verwendet wird

try:
    # Verbindung zur Datenbank herstellen
    conn = pg8000.connect(
        user='postgres',    # Benutzername für die Datenbankverbindung
        password='Monster',      # Passwort für die Datenbankverbindung
        host='localhost',   # Hostname oder IP-Adresse des Servers, auf dem die Datenbank läuft
        port=5432,  # Port, über den die Verbindung hergestellt wird (standardmäßig 5432 für PostgreSQL)
        database='weather'  # Name der Datenbank, zu der eine Verbindung hergestellt werden soll
    )

    # Erstellen eines Cursor-Objekts für die Datenbankverbindung
    cursor = conn.cursor()

    # Beispielabfrage ausführen, um die Datenbankversion abzurufen
    cursor.execute('SELECT version()')

    # Ergebnis abrufen
    db_version = cursor.fetchone()
    # Ausgabe der Datenbankversion
    print('Datenbankversion:', db_version)

    # Cursor und Verbindung schließen
    cursor.close()  # Schließen des Cursors, um Ressourcen freizugeben
    conn.close()    # Schließen der Verbindung zur Datenbank


except Exception as e:
    # Ausgabe einer Fehlermeldung, falls ein Fehler auftritt
    print('Fehler beim Verbindungsaufbau zur Datenbank:', e)