from Tkinter import Tk, Text, INSERT, DISABLED
import Tkinter
import MySQLdb

def createnewuser(Username,Password,self):
    global online
    online = 0
    try:
        # connect to the online database
        db = MySQLdb.connect("127.0.0.1","root1","pudding123","userfiles")
    except:
        # if an error is returned, the user cannot log on
        online = 1
    if online != 1:
        cursor = db.cursor()
        # assign a string to the variable sql
        sql = "SELECT * FROM user_credentials WHERE Username='"+Username+"';"
        # execute the string sql through the cursor
        cursor.execute(sql)
        # get results from the database
        results = cursor.fetchall()
        global errorcheck
        if results == ():
            errorcheck = 0
            # assign a string to the variable sql
            SQL = "INSERT INTO user_credentials(Username,Password) VALUES('"+Username+"','"+Password+"')"
            # execute the string sql through the cursor
            cursor.execute(SQL)
            # assign a string to the variable sql
            sql = "INSERT INTO user_scores(Username,Difficulty,WordsPerMinute,Total_Score) VALUES ('"+Username+"',1,0,0)"
            # execute the string sql through the cursor
            cursor.execute(sql)
            # assign a string to the variable sql
            sql = "INSERT INTO user_scores(Username,Difficulty,WordsPerMinute,Total_Score) VALUES ('"+Username+"',2,0,0)"
            # execute the string sql through the cursor
            cursor.execute(sql)
            # assign a string to the variable sql
            sql = "INSERT INTO user_scores(Username,Difficulty,WordsPerMinute,Total_Score) VALUES ('"+Username+"',3,0,0)"
            # execute the string sql through the cursor
            cursor.execute(sql)
            db.commit()
            # Commit values to the database
            db.close()
            # close connection to the database
        else:
            errorcheck = 1
            db.close()
            # close connection to the database

def searchforuser(Username,Password,self):
    global online
    online = 0
    try:
        # connect to the online database
        db = MySQLdb.connect("127.0.0.1","root1","pudding123","userfiles")
    except:
        # if an error is returned, the user cannot log on
        online = 1
    if online != 1:
        # create a cursor object
        cursor = db.cursor()
        # assign a string to the variable sql
        sql = "SELECT * FROM user_credentials WHERE Username='"+Username+"' AND Password='"+Password+"';"
        # execute the string sql through the cursor
        cursor.execute(sql)
        global account
        # get results from the database
        results = cursor.fetchall()
        # If results returns nothing
        if results == ():
            account = 0
            # account tells the program if the user exists
            db.close()
            # close connection to the database
        else:
            account = 1
            # account tells the program if the user exists
            db.close()
            # close connection to the database

def submitscore(Username,acc,words_per_minute,totalscore,difficulty):
    global online
    online = 0
    try:
        # connect to the online database
        db = MySQLdb.connect("127.0.0.1","root1","pudding123","userfiles")
    except:
        # if an error is returned, the user cannot log on
        online = 1
    if online != 1:
        # create a cursor object
        cursor = db.cursor()
        global scoreresults
        
        #Turns values into strings to be executed as sql statements
        accuracy = str(acc)
        WPM = str(words_per_minute)
        totscore = str(totalscore)
        diff = str(difficulty)

        # assign a string to the variable SQL
        SQL ="""SELECT Total_score FROM user_scores
                WHERE Username = '"""+Username+"""'
                AND difficulty = """+diff
        cursor.execute(SQL)
        # execute the string SQL through the cursor

        # Take the result value and turn it into suitable data
        Escore = cursor.fetchall()
        Score = str(Escore[0])
        global Enteredscore
        Enteredscore = Score[1:len(Score)-3]
        Entscore = int(Enteredscore)
        
        if Entscore < totalscore:
            # assign a string to the variable sql
            sql = """UPDATE user_scores
                     SET Accuracy = """+accuracy+""", WordsPerMinute = """+WPM+""", Total_score = """+totscore+"""
                     WHERE Username = '"""+Username+"""'
                     AND Difficulty = """+diff+""";"""
            cursor.execute(sql)
            # execute the string sql through the cursor
            db.commit()
            # assign a string to the variable SQL
            SQL ="""SELECT FIND_IN_SET( Total_score, (    
                    SELECT GROUP_CONCAT( Total_Score
                    ORDER BY Total_Score DESC ) 
                    FROM userfiles.user_scores )
                    ) AS rank
                    FROM userfiles.user_scores
                    WHERE UserName =  '"""+Username+"""'
                    AND difficulty= """+diff+""""""
            cursor.execute(SQL)
            # execute the string SQL through the cursor

            # Take the result value and turn it into suitable data
            result = cursor.fetchall()
            res = str(result[0])
            global results
            results = res[1:len(res)-3]
            
            # assign a string to the variable sql
            sql ="""SELECT Username FROM user_scores
                    ORDER BY Total_score DESC
                    LIMIT 1;"""
            cursor.execute(sql)
            # execute the string sql through the cursor

            # Take the result value and turn it into suitable data
            result1 = cursor.fetchall()
            res1 = str(result1[0])
            global highestuser
            highestuser = res1[2:len(res1)-3]
            
            # assign a string to the variable sql
            sql ="""SELECT Total_score FROM user_scores
                    ORDER BY Total_score DESC
                    LIMIT 1;"""
            cursor.execute(sql)
            # execute the string sql through the cursor

            # Take the result value and turn it into suitable data
            result2 = cursor.fetchall()
            res2 = str(result2[0])
            global highestscore
            highestscore = res2[1:len(res2)-3]
            scoreresults = 0
            db.close()
        else:
            scoreresults = 1
            db.close()
