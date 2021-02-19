from discord import utils
import discord
import mysql.connector
import json
from datetime import datetime

config = json.loads(open("./config.json","r").read())

mydb = mysql.connector.connect(
  host=config["db"]["host"],
  user=config["db"]["user"],
  password=config["db"]["password"],
  database=config["db"]["name"]
)

sql = mydb.cursor()


def executeSql(cmd):
    mydb.connect()
    print("Executing: " + cmd)
    if cmd.startswith("SELECT"):
        sql.execute(cmd)
        result = sql.fetchall()
        mydb.close()
        return result
    else:
        # insert, update or delete
        sql.execute(cmd)
        mydb.commit()
        mydb.close()
        return

class weebnation():
    async def addAnime(self, message):
        params = message.content.split(' ')[1:]
        link = [i for i in params if i.startswith('https://')][0]
        linkIndex = params.index(link)
        name = ' '.join(params[0:linkIndex])
        tags = ''.join(params[linkIndex+1:])
        if name == None or link == None or tags == None:
            await channel.send("Du musst den Namen, einen Link und mindestens einen Tag angeben!🤷🏼‍♂️")
            return
        else:
            cmd = "SELECT aTitle,aLink FROM tblAnime WHERE aTitle = '%s' OR aLink = '%s'" % (name, link)
            result = executeSql(cmd)
            if result == None:
                 await channel.send("Der Anime ist bereits in der Weeb-Datenbank!🤷🏼‍♂️")
                 return
            else:
                cmd = "INSERT INTO tblAnime(aTitle, aLink, aCreator, aTags) VALUES ('%s','%s','%s','%s')" % (name, link, message.author.id, tags)
                executeSql(cmd)
                await message.channel.send("Ich habe %s der Weeb-Datenbank hinzugefügt." % (name))

    async def listAnimes(self, message):
        cmd = "SELECT aTitle, aLink, aTags FROM tblAnime ORDER BY RAND() LIMIT 5"
        result = executeSql(cmd)
        msg = "Hier 5 random Animes aus meiner Datenbank:\n"
        for i in range(len(result)):
            msg = msg + ("%d. %s (%s) [%s]\n" % (i+1, result[i][0],result[i][1],result[i][2]))
        await message.channel.send(msg)
        return
    
    async def showAnimes(self,message):
        await channel.send("Hier ist der Link zum Himmel!")
        await channel.send(link)