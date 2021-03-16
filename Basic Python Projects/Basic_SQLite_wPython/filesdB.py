

import sqlite3


def makeList():
    """ This function pulls the .txt files from a list of filenames, puts the
    filenames in a database and prints those filenames to the console """
    
    # Creating dummy file list to use for this exercise
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
                'World.txt', 'data.pdf', 'myPhoto.jpg')

    # connecting to a database. If it doesn't exist, this will create the database
    conn = sqlite3.connect('files.db')   

    with conn:
        # Passing in SQL statements to cursor. Creating table.
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        files_filename VARCHAR(30) \
        )")
        conn.commit()  # Commit. Saves the changes.

        # Iterate through list of filenames and add .txt files to the dB.
        for fname in fileList:
            if ".txt" in fname:
                cur.execute("INSERT INTO tbl_files (files_filename) \
                VALUES (?)", (fname,))  # Using sql placeholder.
                conn.commit()

        # Get filenames back out of database and print them to console.
        cur.execute("SELECT files_filename FROM tbl_files")
        dBFiles = cur.fetchall()
        counter = 1
        for i in dBFiles:
             print("File " + str(counter) +": " + i[0])
             counter +=1
    conn.close()  # Closing connection to dB.

if __name__ == "__main__":
    makeList()

