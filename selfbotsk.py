# -*- coding: utf-8 -*-
#thanks to allfams

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator

dz = LINE("EzOM95U5wuX2GcJEElZb.SCwNhYE4y4LUNus/QfFtwW.uzfYzwnXix/NrLp3aIYeWS5StmNjmWrDysg6HyTGobY=")
dz.log("Auth Token : " + str(dz.authToken))
dz.log("Timeline Token : " + str(dz.tl.channelAccessToken))

#==============================================================================#
call = dz
oepoll = OEPoll(dz)
dzMID = dz.profile.mid
dzProfile = dz.getProfile()
lineSettings = dz.getSettings()
#==============================================================================#
botStart = time.time()
#==============================================================================#

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

helpMessage ="""╔════════════════════ 
║          SILENT TEAM BOT V'selfbot
╠════════════════════
╠➣  ᴍʏ ɪᴅ
╠➣  ᴍᴇ
╠➣  ɢɪɴғᴏ
╠➣  ɢᴄʀᴇᴀᴛᴏʀ
╠➣  ɢᴜʀʟ
╠➣  ᴏᴜʀʟ
╠➣  ᴄᴜʀʟ
╠➣  ɢɴᴀᴍᴇ:「ᴛᴇᴋs」
╠➣  ʜᴀɪɪ[ᴛᴀɢ]
╠➣  Colok
╠➣  ᴄᴇᴋ
╠➣  sɪᴅᴇʀ
╠➣  sɪᴅᴇʀ ᴏɴ
╠➣  sɪᴅᴇʀ ᴏғғ
╠➣  ɢɪғᴛ
╠➣  ᴄʟᴇᴀɴ ᴀʟʟ ᴄʜᴀᴛ
╠➣  ɢᴍɪᴅ [Tᴀɢ]
╠➣  ɢᴇᴛ ᴍɪᴅ 「sᴄ」
╠➣  ɢᴇᴛ [ᴛᴀɢ]
╠➣  ᴅᴘ[ᴛᴀɢ]
╠➣  ɪɴғᴏ[ᴛᴀɢ]
╠➣  ʙɪᴏ[ᴛᴀɢ]
╠➣  ᴄᴏᴠᴇʀ[ᴛᴀɢ]
╠➣  ᴄʟᴏɴᴇ [ᴛᴀɢ]
╠➣  ʀᴇᴄʟᴏɴᴇ
╠➣  ɪɴᴠɪᴛᴇ: 「sᴄ」
╠➣  Lɪᴋᴇ ᴏɴ/ᴏғғ
╠➣  Gᴇᴛ ᴘᴏsᴛ ᴏɴ/ᴏғғ
╠➣  ᴍʏ ɢʀᴜᴘ
╠➣  ᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠➣  ᴜɴᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠➣  ᴍʏ ɢʀᴜᴘ
╠➣  sᴀʟᴀᴍ1
╠➣  sᴀʟᴀᴍ2
╠➣  ᴡᴇʟʟᴄᴏᴍᴇ
╠════════════════════
╠➣  ʙᴄᴍᴇᴍʙᴇʀ:「ᴛᴇᴋs」
╠➣  ʙᴄɢʀᴜᴘ:「ᴛᴇᴋs」
╠➣  ʏᴛ: 「ᴛᴇᴋs」
╠➣  ɢʀᴜᴘ ᴘɪᴄᴛ
╠➣  ᴍᴜsɪk 「ᴛᴇᴋs」
╠➣  ᴢᴏᴅɪᴀᴋ:
╠➣  Wɪᴋɪ: 「ᴛᴇᴋs」
╠➣  ᴠɴ: 「ᴛᴇᴋs」
╠➣  ᴠɴ-ᴇɴ: 「ᴛᴇᴋs」
╠➣  ʏᴏᴜᴛᴜʙᴇ: 「ᴛᴇᴋs」
╠➣  /Tᴀɢ [ᴛᴀɢ]
╠➣  /Sᴘᴀᴍ[ᴊᴜᴍʟᴀʜ][ᴛᴇᴋs]
╠➣  /Sᴘᴀᴍᴄᴏɴᴛᴀᴄᴛ
╠➣  /Bʟᴀɴᴋ
╠➣  sᴘ
╠➣  ʀᴜɴᴛɪᴍᴇ
╠➣  ᴋᴀʟᴇɴᴅᴇʀ
╠════════════════════
╠➣  ᴀʟʟ ᴍɪᴍɪᴄ ᴍᴇ[ᴛᴀɢ]
╠➣  ᴜɴᴍɪᴍɪᴄ[ᴛᴀɢ]
╠➣  ᴍɪᴍɪᴄ  /ᴏɴ/ᴏғғ
╠➣  ᴍɪᴍɪᴄ Lɪsᴛ
╠➣  ʙᴀɴɴᴇᴅ[ᴛᴀɢ]
╠➣  ᴜɴʙᴀɴɴᴇᴅ[ᴛᴀɢ]
╠➣  ᴄʟᴇᴀʀ ʙᴀɴ
╠➣  ᴋɪʟʟ ʙᴀɴ
╠➣  ᴀᴅᴅ ʙᴀɴɴᴇᴅ
╠➣  ᴅᴇʟ ʙᴀɴɴᴇᴅ
╠➣  ʙᴀɴ ʟɪsᴛ
╠➣  ᴀᴅᴅ ғʀɪᴇɴᴅ
╠➣  ᴅᴇʟ ғʀɪᴇɴᴅ
╠➣  ғʀɪᴇɴᴅ ʟɪsᴛ
╠➣  ᴍᴇᴍʙᴇʀ Lɪsᴛ
╠════════════════════
╠➣  ʟᴏᴄᴋ ᴊᴏɪɴ「ɪɴ」
╠➣  ᴜɴʟᴏᴄᴋ ᴊᴏɪɴ「ɪɴ」
╠➣  ʟᴏᴄᴋ ᴊᴏɪɴ ɢʀᴜᴘ:「ɢɴ」
╠➣  ᴜɴʟᴏᴄᴋ ᴊᴏɪɴ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠➣  ʟᴏᴄᴋ ǫʀ「ɪɴ」 
╠➣  ᴜɴʟᴏᴄᴋ ǫʀ「ɪɴ」 
╠➣  ʟᴏᴄᴋ ǫʀ ɢʀᴜᴘ:「ɢɴ」
╠➣  ᴜɴʟᴏᴄᴋ ǫʀ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠➣  ʟᴏᴄᴋ ɪɴᴠɪᴛᴇ
╠➣  ᴜɴʟᴏᴄᴋ ɪɴᴠɪᴛᴇ
╠➣  ɪɴᴠɪᴛᴇ ᴏɴ ɢʀᴜᴘ:「ɢɴ」
╠➣  ᴜɴʟᴏᴄᴋ ɪɴᴠɪᴛᴇ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠➣  ᴡᴇʟʟᴄᴏᴍᴇ ᴏɴ/ᴏғғ
╠➣  ʟᴇғᴛ ᴏɴ/ᴏғғ 
╠════════════════════
╠➣  ʀᴇsᴇᴛ ᴀʟʟ sᴇᴛ ɢʀᴜᴘ:「ɢɴ」
╠════════════════════
╠➣  ʟɪsᴛ ᴀᴜᴛᴏᴋɪᴄᴋ
╠➣  ʟɪsᴛ ᴀᴜᴛᴏ ɪɴᴛ
╠➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ
╠➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ǫʀ
╠➣  ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ
╠➣  ʟɪsᴛ ᴘʀᴏsɪᴅᴇʀ
╠➣  ʟɪsᴛ ᴅᴇᴛᴇᴄᴛ ᴛɪᴋᴇʟʟ
╠════════════════════
╠➣  ʀᴇsᴇᴛ ɢʀᴜᴘ「ɪɴ」 
╠➣  sᴇᴛ「ɪɴ」 
╠➣  sᴛᴀᴛᴜs「ɪɴ」 
╠➣  ᴀᴅᴅ sᴛᴀᴛᴜs「ɪɴ」 
╠➣  ᴀᴅᴅ ᴏғғ「ɪɴ」 
╠➣  ʀᴀᴛᴀɪɴɴ
╠════════════════════
╠➣ ᴄᴛᴇᴋs ʟᴇғᴛ:「ᴛᴇᴋs」
╠➣ ʟᴇғᴛ ᴛᴇᴋs
╠➣ ᴄᴛᴇᴋs ᴡᴇʟʟᴄᴏᴍᴇ:「ᴛᴇᴋs」
╠➣ ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴇᴋs
╠➣ ᴄᴛᴇᴋs ᴄᴄᴛᴠ:「ᴛᴇᴋs」
╠➣ ᴄᴄᴛᴠ ᴛᴇᴋs
╠➣ ᴄᴛᴇᴋs ᴀᴅᴅ:「ᴛᴇᴋs」
╠➣ ᴀᴅᴅ ᴛᴇᴋs
╠➣ ᴄᴛᴇᴋs ᴄᴏᴍᴍᴇɴᴛ:「ᴛᴇᴋs」
╠════════════════════
╠➣ ᴄᴛᴇᴋs ᴛᴀɢ1:「ᴛᴇᴋs」
╠➣ ᴛᴀɢ1 ᴄᴇᴋ
╠════════════════════
╠➣ ᴄᴛᴇᴋs ᴛᴀɢ2:「ᴛᴇᴋs」
╠➣ ᴄᴛɪᴋᴇʟʟ 2
╠➣ ᴛᴀɢ2 ᴄᴇᴋ
╠════════════════════
╠➣ [ɪᴅ/ᴇɴ] ɪɴᴅ ᴛᴏ ᴇɴɢ
╠➣ [ᴇɴ/ɪᴅ] ᴇɴɢ ᴛᴏ ɪᴅ
╠➣ [ɪᴅ/ᴊᴘ] ɪɴᴅ ᴛᴏ ᴊᴘɴ
╠➣ [ᴊᴘ/ɪᴅ] ᴊᴘɴ ᴛᴏ ɪɴᴅ
╠➣ [ɪᴅ/ᴛʜ] ɪɴᴅ ᴛᴏ ᴛʜᴀ
╠➣ [ᴛʜ/ɪᴅ] ᴛʜᴀ ᴛᴏ ɪɴᴅ
╠➣ [ɪᴅ/ᴀʀ] ɪɴᴅ ᴛᴏ ᴀʀʙ
╠➣ [ᴀʀ/ɪᴅ] ᴀʀʙ ᴛᴏ ɪɴᴅ
╠➣ [ɪᴅ/ᴋᴏ] ɪɴᴅ ᴛᴏ ᴋᴏʀ
╠➣ [ᴋᴏ/ɪᴅ] ᴋᴏʀ ᴛᴏ ɪɴᴅ
╠═══════════════════
║ SILENT TΣΔM βΩT
╠═══════════════════
╠➣line://ti/p/~team bot ptotect
╠➣line://ti/p/~dhenz415
╚═══════════════════
"""

sid = []
wait = {
    "spamr":False,
    "Invite":True,
    "ainvite":False,
    "atarget":False,
    "dtarget":False,
    "afriend":False,
    "dfriend":False,
    "atebz":False,
    "dtebz":False,
    "santet":True,
    "Autojoin":False,
    "Timeline":False,
    "LikeOn":True,
    "getmid":False,
    "mimic":False,
    }

org = {
    "tmimic":{},
    "Target":{},
    "Tebz":{},
    "Friend":{},
    "invitan":{}
    }

pro = {
    'prosider':{},
    'proPoint':{},
    'proTime':{},
    'Protectgr':{},
    'Protectcancl':{},
    'Protectjoin':{},
    'Protectinvite':{},
    'wellcome':True,
    'bymsg':True,
    'intaPoint':{},
    "Autokick":{}
    }

Dhenza = {
    "comment":"╔═════════════════════\nAuto like by:TBP\n╚══════════════════════",
    "cctvteks":"Masuk kuy...\nNgitip bacok ni",
    "message":"Cieee kepo !@\n╔═════════════════════\nᵀᴴᴬᴺᴷˢ ᶠᴼᴿ ᴬᴰᴰ ᴹᴱ\n╚══════════════════════",
    "welmsg":"╔═════════════════════\nWelcome\n╚══════════════════════",
    "leftmsg":"╔═════════════════════\Cie baper\n╚══════════════════════",
    "tagteks1":"apa sayang 😙😙",
    "tagteks2":"iya syang😚😚",
    "tagteks3":"kangen ya//-.."
	}

resp = {
    "csticker1":False,
    "csticker2":False,
    "csticker3":False,
    "detectsticker":False,
    "grupsticker":{},
    "Tag1":True,
    "Tag2":False,
    "Tag3":True,
	}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

ciduk = {
    'ceadPoint':{},
    'ceadMember':{},
    'cetTime':{},
    'cOM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 


#myProfile["displayName"] = dzProfile.displayName
#myProfile["statusMessage"] = dzProfile.statusMessage
#myProfile["pictureStatus"] = dzProfile.pictureStatus

    
contact = dz.getProfile()
backup = dz.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#==============================================================================#
def restartBot():
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
    
def logError(text):
    dz.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        yd.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
#==============================================================================#
def dhenzaBot(op):
    try:
        if op.type == 0:
            return
#================[ NOTIFIED_READ_MESSAGE ]================
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = dz.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠ " + Name
                        wait2['ROM'][op.param1][op.param2] = "╠ " + Name
                else:
                    pass
            except:
                pass
        if op.type == 5:
            dz.findAndAddContactsByMid(op.param1)
            if(Dhenza["message"]in[""," ","\n",None]):
                pass
            else:
                dz.sendMessage(op.param1,str(Dhenza["message"]))
#=====================[ CIDUK SIDER ]=======================
        if op.type == 55:
            msg = op.message
            if op.param1 in pro["prosider"]:
                if op.param1 in ciduk['ceadPoint']:
                    x = dz.getContact(op.param2)
                    x_name = x.displayName
                    if x_name not in ciduk['ceadMember'][op.param1]:
                        ciduk['ceadMember'][op.param1] += x_name
                        ciduk['cOM'][op.param1][op.param2] = x_name
                        try:
                            dz.sendMessage(op.param1,""+str(x_name)+"\n"+Dhenza["cctvteks"])
                            dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + x.pictureStatus)
                        except:
                            print ("error")
            else:
                pass
#======================[ PROTECT CANCLE ]=================
        if op.type == 32:
            if op.param1 in pro["Protectcancl"]:
                if op.param2 in org["Friend"]:
                    pass
                else:
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
                        
#=================[ NOTIFIED_INVITE_INTO_GROUP ]==============        
        if op.type == 13:
            if wait["Autojoin"] == True:
                dz.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param2 in org["Tebz"]:
                dz.acceptGroupInvitation(op.param1)
#=====================[ PROTECT INVITE ]======================
        if op.type == 12:
            if op.param1 in pro["Protectinvite"]:
                X = dz.getGroup(op.param1)
                orang = [contact.mid for contact in X.invitee]
                for m in orang:
                    org["invitan"][m]=True
                    with open('setting.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
        if op.type == 13:
            if op.param1 in pro["Protectinvite"]:
                if op.param2 in org["Friend"]:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        X = dz.getGroup(op.param1)
                        orang = [contact.mid for contact in X.invitee]
                        for m in orang:
                            org["invitan"][m]=True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                else:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        try:
                            dz.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            dz.sendMessage(op.param1,"limit")
#=========== [ LEFT MESSAGE ] ==============
        if op.type == 15:
            if pro["bymsg"]==True:
                dzx = dz.getContact(op.param2)
                dz.sendMessage(op.param1,""+ str(dzx.displayName)+"\n"+Dhenza["leftmsg"])
            else:
                pass
#==============[ WELLCOME] ===============
        if op.type == 17:
            if pro["wellcome"] == True:
                if op.param1 in pro["Protectjoin"]:
                    if op.param2 not in org["invitan"]:
                        pass
                    else:
                        ginfo = dz.getGroup(op.param1)
                        dzx = dz.getContact(op.param2)
                        dz.sendMessage(op.param1, "Haiii..  " + str(dzx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ Dhenza["welmsg"])
                        dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + ydx.pictureStatus)
                else:
                    ginfo = dz.getGroup(op.param1)
                    dzx = dz.getContact(op.param2)
                    dz.sendMessage(op.param1, "Haiii..  " + str(dzx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ Dhenza["welmsg"])
                    dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + dzx.pictureStatus)                    
                    
#==============[ PROTECT JOIN ]==============
        if op.type == 17:
            if op.param1 in pro["Protectjoin"]:
                if op.param2 in org["Friend"]:
                    pass
                elif op.param2 in org["invitan"]:
                    del org["invitan"][op.param2]
                    pass
                else:
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
#=========== [ GHOST MODE ] =============
#===========[ PROTECT QR friend ]==========           
        if op.type == 11:
           if op.param1 in pro["Protectgr"]:
              if op.param2 in org["Friend"]:
                pass
              else:
                try:
                  X = dz.getGroup(op.param1)
                  X.preventedJoinByTicket = True
                  dz.updateGroup(X)
                  Ti = dz.reissueGroupTicket(op.param1)
                  dz.acceptGroupInvitationByTicket(op.param1,Ti)
                  dz.sendMessage(op.param1,dz.getContact(op.param2).displayName + "ᴊᴀɴɢᴀɴ ᴍᴀɪɴᴀɴ ᴋᴏᴅᴇ Qʀ ɢᴏʙʟᴏᴋ")
                  dz.kickoutFromGroup(op.param1,[op.param2])
                  dz.updateGroup(X)
                  dz.leaveRoom(op.param1)
                except:
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventedJoinByTicket = True
                  yd.updateGroup(Z)
                  Ti = dz.reissueGroupTicket(op.param1)
                  dz.acceptGroupInvitationByTicket(op.param1,Ti)
                  dz.sendText(op.param1,dz.getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                  dz.kickoutFromGroup(op.param1,[op.param2])
                  dz.updateGroup(X)
                  dz.leaveRoom(op.param1)

                    
#=============== [ NOTIFIED_KICKOUT_FROM_GROUP ]===========
        if op.type == 19:
            if op.param1 in pro["Autokick"]:
                if op.param2 in org["Friend"]:
                    pass
                else:
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
                   
						
            if op.param3 in org["Friend"]:
                if op.param2 in org["Friend"]:
                    pass
                else:                   
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
                    try:
                    	dz.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            G = dz.getGroup(op.param1)
                            G.preventJoinByTicket = False
                            yd.updateGroup(G)
                            invsend = 0
                            Ticket = dz.reissueGroupTicket(op.param1)
                            dz.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G = dz.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            dz.updateGroup(G)
                        except Exception as e:
                            print(e)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 7:
                    if resp["csticker1"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID1: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)

                    elif resp["csticker2"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID2: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)

                    elif resp["csticker3"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID3: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)
                    else:
                        pass
                        
                if msg.contentType == 13:
                    if wait["atarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            dz.sendMessage(msg.to, "was save")
                            wait["atarget"]=False
                        else:
                            org["Target"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "save succes")
                            wait["atarget"]=False

                    elif wait["dtarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            del org["Target"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wait["dtarget"]=False
                            dz.sendMessage(msg.to,"Target deleted")
                        else:
                            dz.sendMessage(msg.to,"Target not found")
#=====================[ MODE TEBZ ]=================--======
                if msg.contentType == 13:
                    if wait["atebz"]==True:
                        if msg.contentMetadata["mid"] in org["Tebz"]:
                            dz.sendMessage(msg.to, "was on T")
                            wait["atebz"]=False
                        else:
                            org["Tebz"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "T succes")
                            wait["atebz"]=False

                    elif wait["dtebz"]==True:
                        if msg.contentMetadata["mid"] in org["Tebz"]:
                            del org["Tebz"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"T deleted")
                            wait["dtebz"]=False
                        else:
                            dz.sendMessage(msg.to,"F not found")
                            wait["dtebz"]=False
                    else:
                        pass
#=====================[ SEPAM ]========================
                if msg.contentType == 13:
                    if wait["getmid"]==True:
                        x = msg.contentMetadata["mid"]
                        dz.sendMessage(msg.to,x)
                        wait["getmid"]=False

                if msg.contentType == 13:
                    if wait["santet"]==True:
                        x = msg.contentMetadata["mid"]
                        dz.findAndAddContactsByMid(x)
                        try:
                            M = Message()
                            M.to = x
                            M.contentType = 13
                            M.contentMetadata = {'mid': "'"}
                            dz.sendMessage(M)
                            dz.sendMessage(M)
                            wait["santet"]=False
                        except:
                            pass
#========================[ INVITE ]===================
                if msg.contentType == 13:
                    if wait["afriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            dz.sendMessage(msg.to, "Team done")
                            wait["afriend"]=False
                        else:
                            org["Friend"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "Tem succes")
                            wait["afriend"]=False

                    elif wait["dfriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            del org["Friend"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"Friend deleted")
                            wait["dfriend"]=False
                        else:
                            dz.sendMessage(msg.to,"F not found")
                            wait["dfriend"]=False

#=====================[ MODE INVITE ]==================
                if msg.contentType == 13:
                    if wait["Invite"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = dz.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                dz.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invite"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                dz.findAndAddContactsByMid(target)
                                dz.inviteIntoGroup(msg.to,[target])
                                dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴍᴇɴɢɪɴᴠɪᴛᴇ ᴊᴏᴍʙʟᴏ ɪɴɪ \n➡" + _name)
                                wait["Invite"] = False
                                break
                else:
                    pass
#==================[ RECEIVE_MESSAGE ]===============
        if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.text in ["Help"]:
                    dz.sendMessage(msg.to,helpMessage)          
					
        if op.type == 25:
            msg = op.message
            if msg.text is None:
                return
            if msg.text in ["My id"]:
                if msg.toType == 2:
                    dz.sendMessage(msg.to,ydMID)
            elif msg.text in ["Me"]:
            	dz.sendMessage(receiver, None, contentMetadata={'mid': dzMID}, contentType=13)
            elif msg.text in ["Ginfo"]:
                if msg.toType == 2:
                    ginfo = dz.getGroup(msg.to)
                    gCreator = ginfo.creator.displayName
                    if gCreator is None:
                        gCreator = "Error"
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventedJoinByTicket == True:
                        u = "close"
                    else:
                        u = "open"
                    try:
                        dz.sendMessage(msg.to,"╔══════════════\n╠═⟦ ɢʀᴜᴘ ɴᴀᴍᴇ ⟧\n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═⟦ ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ ⟧\n╠ ➽ " + gCreator + "\n╠══════════════\n╠ ➽ ᴍᴇᴍʙᴇʀs: " + str(len(ginfo.members)) + " ᴍᴇᴍʙᴇʀs\n╠ ➽ ᴘᴇɴᴅɪɴɢ: " + sinvitee + " ᴘᴇᴏᴘʟᴇ\n╠ ➽ ᴜʀʟ : " + u + "\n╚══════════════")
                        dz.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                        dz.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                    except:
                        dz.sendMessage(msg.to,"╔══════════════\n╠═⟦ ɢʀᴜᴘ ɴᴀᴍᴇ ⟧\n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═⟦ ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ ⟧\n╠ ➽ " + gCreator + "\n╚══════════════")
                        dz.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                        dz.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                        
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                group = dz.getGroup(msg.to)
                GS = group.creator.mid
                dz.sendContact(msg.to,GS)            
                dz.sendMessage(msg.to,"Sijones ini ɴᴏʜ ʏɢ ʙɪᴋɪɴ ɢʀᴜᴘ ɪɴɪ..")
                
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = dz.getGroup(msg.to)
                    if x.preventedJoinByTicket == True:
                        dz.sendMessage(msg.to,"ǫʀ ɴʏᴀ ᴅɪ ᴀɴᴜ ᴅᴜʟᴜ ʙᴏss..")
                    elif x.preventedJoinByTicket == False:
                        dz.updateGroup(x)
                        gurl = dz.reissueGroupTicket(msg.to)
                        dz.sendMessage(msg.to,"http://line.me/R/ti/g/" + gurl)
                    else:
                        pass
                        
            elif msg.text in ["Ourl"]:
              if msg.toType == 2:
                X = dz.getGroup(msg.to)
                if X.preventedJoinByTicket == False:
                    dz.sendMessage(msg.to,"⟦Qʀ ᴡᴀs ᴏᴘᴇɴ⟧")
                else:
                    X.preventedJoinByTicket = False
                    dz.updateGroup(X)
                    dz.sendMessage(msg.to,"⟦Qʀ ᴏᴘᴇɴ⟧")
                    
            elif msg.text in ["Curl"]:
              if msg.toType == 2:
                X = dz.getGroup(msg.to)
                if X.preventedJoinByTicket == True:
                    dz.sendMessage(msg.to,"⟦Qʀ ᴡᴀs ᴄʟᴏsᴇ⟧")
                else:
                    X.preventedJoinByTicket = True
                    dz.updateGroup(X)
                    dz.sendMessage(msg.to,"⟦Qʀ ᴄʟᴏsᴇ⟧")
                    
            elif "Gname: " in msg.text:
                if msg.toType == 2:
                    X = dz.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    dz.updateGroup(X)
                    dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n"+X.name)
                    
            elif msg.text in ["Reject"]:
              if msg.toType == 2:
                gid = dz.getGroupIdsInvited()
                for i in gid:
                    dz.rejectGroupInvitation(i)
                dz.sendMessage(msg.to,"done reject")

            elif "Bcmember: " in msg.text:
                xres = msg.text.replace("Bcmember: ","")
                group = dz.getGroup(msg.to)
                mem = [contact.mid for contact in group.members]
                cmem = dz.getContacts(mem)
                nc = ""
                for x in range(len(cmem)):
                    try:
                        dz.sendMessage(cmem[x].mid,xres)
                        nc += "\n" + cmem[x].displayName
                    except:
                        pass
                dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʙᴄ ᴛᴏ :\n%s\n\nᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs: %s"%(nc,str(len(cmem))))
            #    print "done bc"
            elif "Bcgrup: " in msg.text:
                bc = msg.text.replace("Bcgrup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                    dz.sendMessage(i,bc+"\n\nSILENT TΣΔM βΩT")
                dz.sendMessage(msg.to,"⟦ʙʀᴏᴀᴅᴄᴀsᴛ sᴜᴄᴄᴇs⟧")
            elif "Lirik: " in msg.text:
                try:
                    songname = msg.text.replace('Lirik: ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        dz.sendMessage(msg.to, hasil)
                except Exception as wak:
                        dz.sendMessage(msg.to, str(wak))
            elif "Image: " in msg.text:
                try:
                    query = msg.text.replace("Image:", "")
                    images = dz.image_search(query)
                    dz.sendImageWithURL(receiver, images)
                except Exception as e:
                    dz.sendMessage(receiver, str(e))
            elif "Yt: " in msg.text:
                query = msg.text.replace("Yt: ","")
                with requests.session() as s:
                    s.headers['user-agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    dz.sendMessage(msg.to,hasil)
            elif msg.text in ["mid"]:
                wait["getmid"]=True
                dz.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif "Gmid @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            dz.sendMessage(msg.to,str(mention['M']))
                        except Exception as e:
                            pass
            elif "Get @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = dz.getContact(key1)
                vcx = mmid.mid
                dz.sendContact(msg.to,vcx)
            elif "dp @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = dz.getContact(mention['M'])
                            dz.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                        except Exception as e:
                            pass
            elif "info @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = dz.getContact(key1)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    dz.sendMessage(msg.to,"Nama:\n" + contact.displayName)
                    dz.sendMessage(msg.to,"Bio:\n" + contact.statusMessage)
                    dz.sendImageWithURL(msg.to,image)
                except:
                    pass
            elif "bio @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yd.getContact(key1)
                try:
                    dz.sendMessage(msg.to,contact.statusMessage)
                except:
                    dz.sendMessage(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

            elif "Grup pict" in msg.text:
                    group = dz.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    dz.sendImageWithURL(msg.to,path)
                    
            elif "Kedipin: " in msg.text:
                txt = msg.text.replace("Kedipin: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                dz.sendMessage(msg.to, t1 + txt + t2)
            elif "Insta: " in msg.text:
                try:
                    instagram = msg.text.lower().replace("Insta: ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    dz.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                    dz.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	dz.sendMessage(msg.to, str(njer))

            elif "Zodiak: " in msg.text:
                tanggal = msg.text.replace("Zodiak: ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                dz.sendMessage(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
            elif "Wiki: " in msg.text:
                try:
                    wiki = msg.text.lower().replace("Wiki: ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=1)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    dz.sendMessage(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            dz.sendMessage(msg.to, pesan)
                        except Exception as e:
                            dz.sendMessage(msg.to, str(e))

#==================[ REBOOT ]===================
            elif msg.text in ["Reboot"]:
                    try:
                        dz.sendMessage(msg.to,"ʀᴇsᴛᴀrᴛɪɴɢ .....")
                        restartBot()
                    except:
                        dz.sendMessage(msg.to,"Please wait")
                        restartBot()
                        pass
                        
            elif msg.text in ["Sp"]:
                start = time.time()
                dz.sendMessage(msg.to, "ѕaвar вoѕѕ..")
                elapsed_time = time.time() - start
                dz.sendMessage(msg.to, "%ss" % (elapsed_time))
                
            elif msg.text in ["Refresh"]:
                    dz.sendMessage(msg.to, "Bot has been restarted")
                    restart_program()
                    
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                dz.sendMessage(msg.to, rst)
                
            elif msg.text in ["Runtime"]:
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                dz.sendMessage(msg.to, "ʙᴏᴛ ʀᴜɴ  {}".format(str(runtime)))
                
            elif msg.text in ["Tanggal"]:
                    tz = pytz.timezone("Asia/Hong_Kong")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    dz.sendMessage(msg.to, readTime)  

            elif "/spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[1])
                teks = msg.text.replace("/spam "+str(jmlh),"")
                for i in range(jmlh):
                    if str(txt[2])==None:
                        dz.sendMessage(msg.to, "nyepm nya yg bener kk..")
                    else:
                        try:
                            dz.sendMessage(msg.to, teks)
                        except:
                            dz.sendMessage(msg.to, "nyepm nya yg bener kk..")
                            
            elif "/tag @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            coii = dz.getContact(mention['M'])
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)
                            dz.tag(msg.to,coii.mid)                            
                        except:
                            print ("error")
                        print ("spamtag Berhasil.")
                        
            elif msg.text in ["/blank"]:
                blank = "'"
                dz.sendContact(msg.to, blank)	

#=================================================
            elif msg.text in ["cawet"]:
                if msg.toType == 2:
                    group = yd.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    for x in nama:
                            if x not in org["Friend"]:
                                try:
                                    dz.kickoutFromGroup(msg.to,[x])
                                except:
                                    print ("imit")
#==================[ CLONE MODE ]====================
            elif "santet grup: " in msg.text:
                ng = msg.text.replace("santet grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            grup = dz.getGroup(i)
                            M.to = grup.id
                            M.contentType = 13
                            M.contentMetadata = {'mid': "uaff3942633154ae48d90ab41983e3cd6"}
                dz.sendMessage(M)
                dz.sendMessage(msg.to,"「sᴀɴntᴇᴛ ᴛᴇʀᴋɪʀɪᴍ ʙᴏss」")
            elif msg.text in ["Santet"]:
                wait["santet"]=True
                dz.sendMessage(msg.to,"target")
#=================================================
            elif "Clone @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = yd.getProfile()
                            backup.displayName = profile.displayName
                            backup.statusMessage = profile.statusMessage
                            backup.pictureStatus = profile.pictureStatus
                            dz.cloneContactProfile(mention['M'])
                            dz.sendMessage(msg.to,"ᴄʟᴏɴᴇ sᴜᴄᴄᴇs ..")
                        except Exception as error:
                            print (error)
#=================================================
            elif msg.text in ["Reclone"]:
                try:
                    dzProfile.displayName = str(myProfile["displayName"])
                    dzProfile.statusMessage = str(myProfile["statusMessage"])
                    dzProfile.pictureStatus = str(myProfile["pictureStatus"])
                    dz.updateProfileAttribute(8, ydProfile.pictureStatus)
                    dz.updateProfile(ydProfile)
                    dz.sendMessage(msg.to,"reᴄʟᴏɴᴇ sᴜᴄᴄᴇs ..")
                except Exception as e:
                    dz.sendMessage(msg.to, str (e))
#=================================================
            elif "Kick @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            dz.kickoutFromGroup(msg.to, [mention['M']])							
                        except:
                            dz.sendMessage(msg.to, "ʟɪᴍɪᴛ ʙᴏss..")
#=================================================
            elif msg.text in ["Salam"]:
                dz.sendMessage(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
            elif msg.text in ["Salam2"]:
                dz.sendMessage(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
#=================================================
            elif "Reset tikell grup: " in msg.text:
                ng = msg.text.replace("Reset tikell grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del resp["grupsticker"][i]
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
#=================================================
            elif msg.text in ["All protect on"]:
                    pro["Protectgr"][msg.to] = True
                    pro["Protectjoin"][msg.to] = True
                    pro["Protectcancl"][msg.to] = True
                    pro["Protectinvite"][msg.to] = True
                    pro["Autokick"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏɴ")
            elif msg.text in ["All protect off"]:
                if msg.to in pro["Protectgr"]:
                    try:
                        del pro["Protectgr"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectcancl"]:
                    try:
                        del pro["Protectcancl"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectinvite"]:
                    try:
                        del pro["Protectinvite"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectjoin"]:
                    try:
                        del pro["Protectjoin"][msg.to]
                    except:
                        pass
                if msg.to in pro["Autokick"]:
                    try:
                        del pro["Autokick"][msg.to]
                    except:
                        pass
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏғғ")
            elif "All protect on grup: " in msg.text:
                ng = msg.text.replace("All protect on grup: ","")
                gid = yd.getGroupIdsJoined()
                for i in gid:
                        h = yd.getGroup(i).name
                        if h == ng:
                            pro["Protectgr"][i]=True
                            pro["Protectjoin"][msg.to] = True
                            pro["Protectcancl"][msg.to] = True
                            pro["Protectinvite"][msg.to] = True
                            pro["Autokick"][msg.to] = True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏɴ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "All protect off grup: " in msg.text:
                ng = msg.text.replace("All protect off grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            if i in pro["Protectgr"]:
                                try:
                                    del pro["Protectgr"][i]
                                except:
                                    pass
                            if i in pro["Protectcancl"]:
                                try:
                                    del pro["Protectcancl"][i]
                                except:
                                    pass
                            if i in pro["Protectinvite"]:
                                try:
                                    del pro["Protectinvite"][i]
                                except:
                                    pass
                            if i in pro["Protectjoin"]:
                                try:
                                    del pro["Protectjoin"][i]
                                except:
                                    pass
                            if i in pro["Autokick"]:
                                try:
                                    del pro["Autokick"][i]
                                except:
                                    pass
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
#=================================================
            elif msg.text in ["Lock invite"]:
                pro["Protectinvite"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ɪɴᴠɪᴛᴇ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock invite"]:
                del pro["Protectinvite"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ɪɴᴠɪᴛᴇ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock invite grup: " in msg.text:
                ng = msg.text.replace("Unlock invite grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del pro["Protectinvite"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock invite grup: " in msg.text:
                ng = msg.text.replace("Lock invite grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            pro["Protectinvite"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all invite"]:
                pro["Protectinvite"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================
            elif msg.text in ["Lock cancel"]:
                pro["Protectcancl"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock cancel"]:
                del pro["Protectcancl"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock cancel grup: " in msg.text:
                ng = msg.text.replace("Unlock cancel grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del pro["Protectcancl"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock cancel grup: " in msg.text:
                ng = msg.text.replace("Lock cancel grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            pro["Protectcancl"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all cancel"]:
                pro["Protectcancl"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================                
            elif text.lower().startswith("musik"):
                            try:
                                search = text.lower().replace("musik ","")
                                params = {"search": search}
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))                    
                                dz.sendImageWithURL(msg.to, str(data["gambar"]))
                                dz.sendMessage(msg.to, str(hasil))
                                dz.sendMessage(msg.to, "Sabar mas lagi di puterin...😍")
                                dz.sendAudioWithURL(msg.to, str(audio["mp3"]))                    
                                dz.sendMessage(msg.to, str(data["lirik"]))
                            except Exception as error:
                            	pass                         
#=================================================
            elif msg.text in ["Lock join"]:
                pro["Protectjoin"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴊᴏɪɴ ᴏɴ ᴘʀᴏᴛᴇᴄᴛ")
            elif msg.text in ["Unlock join"]:
                del pro["Protectjoin"][msg.to]
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴊᴏɪɴ ᴜɴᴘʀᴏᴛᴇᴄᴛ")
            elif "Unlock join grup: " in msg.text:
                ng = msg.text.replace("Unlock join grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del pro["Protectjoin"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock join grup: " in msg.text:
                ng = msg.text.replace("Lock join grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            pro["Protectjoin"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all join"]:
                pro["Protectjoin"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================
            elif msg.text in ["Left on"]:
                pro["bymsg"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Left off"]:
                pro["bymsg"]=False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=================================================
            elif msg.text in ["Welcome on"]:
                pro["wellcome"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Welcome off"]:
                pro["wellcome"]= False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=================================================
            elif msg.text in ["Autokick on"]:
                pro["Autokick"][msg.to]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Autokick off"]:
                pro["Autokick"][msg.to]=False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ᴋɪᴄᴋ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
            elif "Unlock autokick grup: " in msg.text:
                ng = msg.text.replace("Unlock autokick grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del pro["Autokick"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif "Lock autokick grup: " in msg.text:
                ng = msg.text.replace("Lock autokick grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            pro["Autokick"][i]=True
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs sᴇᴛ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
            elif msg.text in ["Clear all autokick"]:
                pro["Autokick"] = {}
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʟᴇᴀʀ")
#=================================================                
            elif "Sider on grup: " in msg.text:
                ng = msg.text.replace("Sider on grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                  h = dz.getGroup(i).name
                  if h == ng:
                    dz.sendMessage(i,"ɢᴇᴛ ɢʀᴏᴜᴘ ᴅᴏɴᴇ")
                    dz.sendMessage(i,"ɢᴇᴛ ᴍᴇᴍʙᴇʀ ᴅᴏɴᴇ")
                    dz.sendMessage(i,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                    dz.sendMessage(i,"ᴀᴜᴛᴏ sɪᴅᴇʀ ʙʏ: dhenza")
                    pro["prosider"][i] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    try:
                        del ciduk['ceadPoint'][i]
                        del ciduk['ceadMember'][i]
                    except:
                        pass
                    now2 = datetime.now()
                    ciduk['ceadPoint'][i] = msg.id
                    ciduk['ceadMember'][i] = ""
                    ciduk['cetTime'][i] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    ciduk['cOM'][i] = {}
                    dz.sendMessage(msg.to,"sider on that grup")

            elif "Sider off grup: " in msg.text:
                ng = msg.text.replace("Sider off grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                  h = dz.getGroup(i).name
                  if h == ng:
                        dz.sendMessage(i,"ᴄʟᴇᴀʀ ᴍᴇᴍʙᴇʀ ᴅᴏɴᴇ")
                        dz.sendMessage(i,"sɪᴅᴇʀ sᴇᴛ ᴏғғ")
                        dz.sendMessage(i,"ᴀᴜᴛᴏ sɪᴅᴇʀ ʙʏ: dhenza")
                        del pro["prosider"][i]
                        with open('pro.json', 'w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        try:
                            del ciduk['ceadPoint'][i]
                            del ciduk['ceadMember'][i]
                            dz.sendMessage(msg.to,"sider off")
                        except:
                            pass
#=============================================
            elif "Reset all set grup: " in msg.text:
                ng = msg.text.replace("Reset all set grup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                        h = dz.getGroup(i).name
                        if h == ng:
                            del pro["Protectgr"][i]
                            del pro["Protectcancl"][i]
                            del pro["Protectinvite"][i]
                            del pro["Protectjoin"][i]
                            del pro["Autokick"][i]
                            del pro["intaPoint"][i]
                            with open('pro.json', 'w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇsᴇᴛ ᴀʟʟ sᴇᴛ ["+ h +"] ɢʀᴏᴜᴘ")
                        else:
                            pass
#=============================================
            elif msg.text in ["Tag1 on"]:
                    resp["Tag1"]=True
                    resp["Tag2"]=False
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Tag1 off"]:
                    resp["Tag1"]=False
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=============================================
            elif msg.text in ["Tag2 on"]:
                    resp["Tag1"]=False
                    resp["Tag2"]=True

                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Tag2 off"]:
                    resp["Tag2"]=False
                    with open('resp.json', 'w') as fp:
                        json.dump(resp, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴsᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=============================================
            elif msg.text in ["Reset"]:
                if msg.to in pro["Protectgr"]:
                    try:
                        del pro["Protectgr"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectcancl"]:
                    try:
                        del pro["Protectcancl"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectinvite"]:
                    try:
                        del pro["Protectinvite"][msg.to]
                    except:
                        pass
                if msg.to in pro["Protectjoin"]:
                    try:
                        del pro["Protectjoin"][msg.to]
                    except:
                        pass
                if msg.to in pro["Autokick"]:
                    try:
                        del pro["Autokick"][msg.to]
                    except:
                        pass
                if msg.to in pro["intaPoint"]:
                    try:
                        del pro['intaPoint'][msg.to]
                    except:
                        pass
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴀʟʟ sᴇᴛ ᴄʟᴇᴀʀ")
            elif msg.text in ["Set"]:
                md = "╔════════════════════\n╠➣SILENT TΣΔM βΩT\n╠════════════════════\n"
                if msg.to in pro["intaPoint"]: md+="╠➣ᴀᴜᴛᴏ ɪɴ : ✔\n"
                else: md +="╠➣ᴀᴜᴛᴏ ɪɴ : ❌\n"
				
                if msg.to in pro["Protectgr"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ɢʀᴜᴘ : ✔\n"
                else: md +="╠➣ᴘʀᴏᴛᴇᴄᴛ ɢʀᴜᴘ : ❌\n"
				
                if msg.to in pro["Protectcancl"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ✔\n"
                else: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ❌\n"
				
                if msg.to in pro["Protectjoin"]: md+="╠➣ᴘʀᴛᴏᴛᴇᴄᴛ ᴊᴏɪɴ : ✔\n"
                else: md+= "╠➣ᴘʀᴛᴏᴛᴇᴄᴛ ᴊᴏɪɴ : ❌\n"
				
                if msg.to in pro["Protectinvite"]: md+="╠➣ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠ : ✔\n"
                else: md+= "╠➣ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠ : ❌\n"
				
                if msg.to in pro["Autokick"]: md+="╠➣ᴀᴜᴛᴏ ᴋɪᴄᴋ : ✔\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~tambotprotect\n╚════════════════════"
                else:md+="╠➣ᴀᴜᴛᴏ ᴋɪᴄᴋ : ❌\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~teambotprotect\n╚════════════════════"
				
                dz.sendMessage(msg.to,md)
            elif msg.text in ["Add off"]:
                wait["Invi"]=False
                wait["ainvite"]=False
                wait["atarget"]=False
                wait["dtarget"]=False
                wait["afriend"]=False
                wait["dfriend"]=False
                wait["atebz"]=False
                wait["dtebz"]=False
                wait["getmid"]=False
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴀʟʟ ᴀᴅᴅ ᴄʟᴇᴀʀ")
            elif msg.text in ["Add status"]:
                md = "╔════════════════════\n╠SILENT TΣΔM βΩT\n╠════════════════════\n"
                if wait["Invi"] == True: md+="╠➣Invite : ✔\n"
                else:md+="╠➣Invite : ❌\n"
                if wait["atarget"] == True: md+="╠➣ᴀᴅᴅ ʙᴀɴɴᴇᴅ : ✔\n"
                else:md+="╠➣ᴀᴅᴅ ʙᴀɴɴᴇᴅ : ❌\n"
                if wait["dtarget"] == True: md+="╠➣ᴅᴇʟ ʙᴀɴɴᴇᴅ : ✔\n"
                else:md+="╠➣ ᴅᴇʟ ʙᴀɴɴᴇᴅ : ❌\n"
                if wait["atebz"] == True: md+="╠➣ᴀᴅᴅ ᴛᴇʙᴢ : ✔\n"
                else:md+="╠➣ ᴀᴅᴅ ᴛᴇʙᴢ : ❌\n"
                if wait["dtebz"] == True: md+="╠➣ᴅᴇʟ ᴛᴇʙᴢ : ✔\n"
                else:md+="╠➣ᴅᴇʟ ᴛᴇʙᴢ : ❌\n"
                if wait["afriend"] == True: md+="╠➣ᴀᴅᴅ ғʀɪᴇɴᴅ : ✔\n"
                else:md+="╠➣add friend : ❌\n"
                if wait["dfriend"] == True: md+="╠➣ᴅᴇʟ ғʀɪᴇɴᴅ : ✔\n"
                else:md+="╠➣ᴅᴇʟ ғʀɪᴇɴᴅ : ❌\n"
                if wait["getmid"] == True: md+="╠➣ɢᴇᴛ ᴍɪᴅ : ✔\n╠════════════════════\n╠➣line://ti/p/~teambotprotect\n╠➣line://ti/p/~dhenz415\n╚════════════════════"
                else:md+="╠➣ɢᴇᴛ ᴍɪᴅ : ❌\n╠════════════════════\n╠➣line://ti/p/~dhenz415\n╠➣line://ti/p/~teambotprotect\n╚════════════════════"
                dz.sendMessage(msg.to,md)
            elif msg.text in ["Status"]:
                md = "╔════════════════════\n╠SILENT TΣΔM βΩT\n╠════════════════════\n"
                if wait["Autojoin"] == True: md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ❌\n"
                if resp["Tag1"] == True: md+="╠➣ ᴍᴇɴᴛɪᴏɴ1 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ1 : ❌\n"
                if resp["Tag2"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ❌\n"
                if resp["Tag3"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ❌\n"
                if wait["Invi"] == True: md+="╠➣ɪɴᴠɪᴛᴇ : ✔\n"
                else:md+="╠➣ɪɴᴠɪᴛᴇ : ❌\n"
                if wait["LikeOn"] == True: md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ❌\n"
                if wait["getmid"] == True: md+="╠➣ɢᴇᴛ ᴍɪᴅ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴍɪᴅ : ❌\n"
                if wait["Timeline"] == True: md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ❌\n"
                if pro["wellcome"] == True: md+="╠➣ᴡeʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ✔\n"
                else:md+="╠➣ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ❌\n"
                if pro["bymsg"] == True: md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ✔\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~dhenz415\n╚════════════════════"
                else:md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ❌\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~tambotprotect\n╚════════════════════"
                dz.sendMessage(msg.to,md)
#=============================================
            elif msg.text in ["Cek ginfo"]:
                if msg.toType == 2:
                    ginfo = yd.getGroup(msg.to)
                    gCreator = ginfo.creator.displayName
                    if gCreator is None:
                        gCreator = "Error"
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventedJoinByTicket == True:
                        u = "close"
                    else:
                        u = "open"
                    try:
                        dz.sendMessage(msg.to,"「ɢʀᴜᴘ ɴᴀᴍᴇ」 \n➽ " + ginfo.name)
                        time.sleep(0.2)
                        dz.sendMessage(msg.to,"「ɢʀᴜᴘ ᴄʀᴇᴀᴛᴏʀ」 \n➽ "+ gCreator )
                        time.sleep(0.2)
                        dz.sendMessage(msg.to,"「ᴍᴇᴍʙᴇʀs」 \n➽" + str(len(ginfo.members)) + " ᴍᴇᴍʙᴇʀs")
                        time.sleep(0.2)
                        dz.sendMessage(msg.to,"「ᴘᴇɴᴅɪɴɢ:」 " + sinvitee + " ᴘᴇᴏᴘʟᴇ")
                        time.sleep(0.2)
                        dz.sendMessage(msg.to,"「ᴜʀʟ:」 \n➽ " + u )
                        dz.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                    except:
                        dz.sendMessage(msg.to,"get info failed")
            elif msg.text in ["Yd cek grup set"]:
                if msg.to in pro["intaPoint"]:
                    dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ɪɴ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ɪɴ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectgr"]:
                    dz.sendMessage(msg.to,"「ǫʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"「ǫʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")

                if msg.to in pro["Protectcancl"]:
                    dz.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"ᴄᴀɴᴄᴇʟ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectjoin"]:
                    dz.sendMessage(msg.to,"ᴊᴏɪɴᴇᴅ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"ᴊᴏɪɴᴇᴅ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Protectinvite"]:
                    dz.sendMessage(msg.to,"ɪɴᴠɪᴛᴇʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"ɪɴᴠɪᴛᴇʀ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
                if msg.to in pro["Autokick"]: 
                    dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏɴ」")
                else:
                    dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴍᴏᴅᴇ 「ᴏғғ」")
				
#=============================================
            elif msg.text in ["Mimic list"]:
                if org["tmimic"] == {}:
                    dz.sendMessage(msg.to,"Not have list")
                else:
                    mc = []
                    for mi_d in org["tmimic"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴍɪᴍɪᴄ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "Addmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        org['tmimic'][mention['M']] = True
                        dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴀᴅᴅᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "Unmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        del org['tmimic'][mention['M']]
                        dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴅᴇʟᴇᴛᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "Mimic " in msg.text:
                xpesan = msg.text
                xres = xpesan.replace("Mimic ","")
                if xres == "off":
                    wait['mimic'] = False
                    dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏғғ")
                elif xres == "on":
                    wait['mimic'] = True
                    dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏɴ")
            elif "Banned @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in org["Target"]:
                            dz.sendMessage(msg.to,"Already save")
                        elif mention['M']in org["Friend"]:
                            dz.sendMessage(msg.to,"S empty")
                        else:
                            org["Target"][mention['M']] = True
                            with open('setting.json', 'w') as fp:
                                json.dump(wait, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
            elif "Unbanned @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in org["Target"]:
                            del org["Target"][mention['M']]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                        else:
                            dz.sendMessage(msg.to,"ᴇᴍᴘᴛʏ ᴛᴀʀɢᴇᴛ")
            elif msg.text in ["Clear ban"]:
                org['Target'] = {}
                with open('org.json', 'w') as fp:
                    json.dump(org, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴄʟᴇᴀʀ")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = yd.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in org["Target"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        dz.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                        return
                    for jj in matched_list:
                        try:
                            dz.kickoutFromGroup(msg.to,[jj])						
                        except:
                            print ("limit")
                    dz.sendMessage(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Add banned"]:
                    wait["atarget"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del banned"]:
                    wait["dtarget"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Ban list"]:
                if org["Target"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in org["Target"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴛᴀʀɢᴇᴛ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Add tebz"]:
                    wait["atebz"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del tebz"]:
                    wait["dtebz"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Clear tebz"]:
                org['Tebz'] = {}
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴄʟᴇᴀʀ")
            elif msg.text in ["Tebz list"]:
                if org["Tebz"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in org["Tebz"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴛᴇʙᴢ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Add friend"]:
                    wait["afriend"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Del friend"]:
                    wait["dfriend"]=True
                    dz.sendMessage(msg.to, "sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Friend list"]:
                if org["Friend"] == {}:
                    try:
                        dz.sendMessage(msg.to,"ɴᴏ ғʀɪᴇɴᴅ ᴀᴅᴅᴇᴅ")
                    except:
                        pass
                else:
                    mc = []
                    for mi_d in org["Friend"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ Friend List ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif msg.text in ["Clear friend"]:
                org['Friend'] = {}
                with open('org.json', 'w') as fp:
                    json.dump(org, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ғʀɪᴇɴᴅ ᴄʟᴇᴀʀ")
#=============================================
            elif msg.text in ["My grup"]:
                    gid = dz.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = dz.getGroup(i).name
                        h += "╠ ➽ %s\n" % (gn)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴍʏ ɢʀᴜᴘ ⟧\n╔══════════════\n"+ h +"╚══════════════")
#=============================================
            elif "Cname: " in msg.text:
                x = dz.getProfile()
                x.displayName = msg.text.replace("Cname: ","")
                dz.updateProfile(x)
                dz.sendMessage(msg.to, "ᴅᴏɴᴇ")
#=============================================
            elif msg.text in ["Autojoin on"]:
                wait["Autojoin"]=True
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏɴ")
            elif msg.text in ["Autojoin off"]:
                wait["Autojoin"]=False
                with open('setting.json', 'w') as fp:
                    json.dump(wait, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏғғ")
#=============================================
            elif msg.text in ["Gift"]:
                    giftnya={'MSGTPL': '5',
                            'PRDTYPE': 'THEME',
                            'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58'}           
                    dz.sendMessage(msg.to,None, contentMetadata=giftnya, contentType=9)
#=============================================
            elif "List grup tikell" == msg.text:
                if resp["grupsticker"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in resp["grupsticker"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ Tikell on ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List prosider" == msg.text:
                if pro["prosider"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["prosider"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ sɪᴅᴇʀ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List autokick" == msg.text:
                if pro["Autokick"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Autokick"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴀᴜᴛᴏᴋɪᴄᴋ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List auto in" == msg.text:
                if pro["intaPoint"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["intaPoint"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔═════════════\n╠⟦ ᴘ ᴊᴏɪɴ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect join" == msg.text:
                if pro["Protectjoin"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectjoin"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ ᴊᴏɪɴ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══���═══════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect qr" == msg.text:
                if pro["Protectgr"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectgr"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ ǫʀ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "List protect cancel" == msg.text:
                if pro["Protectcancl"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectcancl"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ ᴄᴀɴᴄᴇʟ ɢʀᴜᴘ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
#=============================================
            elif "List protect invite" == msg.text:
                if pro["Protectinvite"] == {}:
                    dz.sendMessage(msg.to,"ɴᴏ ɢʀᴜᴘ ᴀᴅᴅᴇᴅ")
                else:
                    mc = []
                    for mi_d in pro["Protectinvite"]:
                        mc.append(mi_d)
                    pass
                    cban = yd.getGroups(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].name)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴘ ɪɴᴠɪᴛᴇ ɢʀᴜᴘ ⟧\n╔═���════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")

            elif msg.text in ["Tag"]:
                group = dz.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                k = len(nama)//20
                for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*20 : (a+1)*20]:
                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                        s += 7
                        txt += u'@Zero \n'
                    dz.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    
            elif msg.text in ["Cek"]:
                    dz.sendMessage(msg.to, ".")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
            elif msg.text in ["Sider"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        dz.sendMessage(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                      
                    else:
                        dz.sendMessage(msg.to, "ʙᴇʟᴏᴍ ᴅɪ sᴇᴛ ʙᴏsss")
            elif msg.text in ["Sider on"]:
                    pro["prosider"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "sIder ᴍᴏᴅᴇ ᴏɴ ʙᴏs")
                    try:
                        del ciduk['ceadPoint'][msg.to]
                        del ciduk['ceadMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    ciduk['ceadPoint'][msg.to] = msg.id
                    ciduk['ceadMember'][msg.to] = ""
                    ciduk['cetTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    ciduk['cOM'][msg.to] = {}
            elif msg.text in ["Sider off"]:
                    del pro["prosider"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    dz.sendMessage(msg.to, "sIder ᴍᴏᴅᴇ ᴏғғ ʙᴏs")
                    try:
                        del ciduk['ceadPoint'][msg.to]
                        del ciduk['ceadMember'][msg.to]
                    except:
                        pass
#=============================================
            elif msg.text in ["Recover"]:
                thisgroup = dz.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                dz.createGroup("test", mi_d)
                dz.sendMessage(msg.to,"done")
#=============================================
            elif msg.text in ["Clean all chat"]:
                try:
                    dz.removeAllMessages(op.param2)
                    dz.sendMessage(msg.to,"ᴅᴏɴᴇ")
                except:
                    pass
#=============================================
            elif msg.text in ["Wellcome"]:
                gs = dz.getGroup(msg.to)
                dz.sendMessage(msg.to,"ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴏ "+ gs.name)
#=============================================
            elif msg.text in ["Cancel all"]:
                group = dz.getGroup(msg.to)
                if group.invitee is None:
                    dz.sendMessage(op.message.to, "No one is inviting.")
                else:
                    nama = [contact.mid for contact in group.invitee]
                    for x in nama:
                        time.sleep(0.2)
                        dz.cancelGroupInvitation(msg.to, [x])
                    dz.sendMessage(msg.to, "done")
#=============================================
            elif msg.text in ["Invite"]:
                    wait["Invi"] = True
                    dz.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
#=============================================
            elif msg.text in ["Member list"]:   
                kontak = dz.getGroup(msg.to)
                group = kontak.members
                msgs="╔══════════════\n╠⟦ ᴍᴇᴍʙᴇʀ ʟɪsᴛ ⟧\n╔══════════════"
                for ids in group:
                    msgs+="\n╠ ➽ %s" % (ids.displayName)
                msgs+="\n╚══════════════\n╠⟦ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i ⟧\n" % len(group)+"╚══════════════"
                dz.sendMessage(msg.to, msgs)

            elif "Cteks comment: " in msg.text:
                Dhenza["comment"] = msg.text.replace("Cteks comment: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Comment teks"]:
                dz.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + Dhenza["comment"])
#=============================================
            elif "Cteks cctv: " in msg.text:
                Dhenza["cctvteks"] = msg.text.replace("Cteks cctv: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Cctv teks"]:
                dz.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + Dhenza["cctvteks"])
#=============================================
            elif "Cteks tag1: " in msg.text:
                Dhenza["tagteks1"] = msg.text.replace("Cteks tag1: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")
#=============================================
            elif "Cteks tag2: " in msg.text:
                Dhenza["tagteks2"] = msg.text.replace("Cteks tag2: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")
#=============================================
            elif "Cteks left: " in msg.text:
                Dhenza["leftmsg"] = msg.text.replace("Cteks left: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Left teks"]:
                dz.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + Dhenza["leftmsg"])
#=============================================
            elif "Cteks wellcome: " in msg.text:
                Dhenza["welmsg"] = msg.text.replace("Cteks wellcome: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Wellcome teks"]:
                dz.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + Dhenza["welmsg"])   
#=============================================
            elif "Cteks add: " in msg.text:
                Dhenza["message"] = msg.text.replace("Cteks add: ","")
                with open('teks.json', 'w') as fp:
                    json.dump(Dhenza, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to,"ᴄʜᴀɴɢᴇ sᴜᴄᴄᴇs")   
            elif msg.text in ["Add teks"]:
                dz.sendMessage(msg.to,"ᴍsɢ ᴛᴇxᴛ: \n\n" + Dhenza["message"])
#=============================================
        if op.type == 26:
            msg = op.message
            if msg.toType == 2:
                if wait["mimic"] == True:
                    if msg.from_ in wait["tmimic"]:
                        text = msg.text
                        if text in helpMessage:
                            pass
                        elif text in helpMessage1:
                            pass
                        elif text in helpMessage2:
                            pass
                        elif text in helpMessage3:
                            pass
                        else:
                            dz.sendMessage(msg.to,text)
                    else:
                        pass
                else:
                    pass

            if msg.toType == 2:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if resp["Tag1"] == True:    
                        contact = dz.getContact(msg._from)
                        cName = contact.displayName
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in dzMID:
                                dz.sendMessage(msg.to,"ᴴᴬᵞ @!"+cName+"\n"+Dhenza["tagteks1"])
                                dz.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+contact.pictureStatus)
                                rnd = ["Jangan tag tar syang"]
                                p = random.choice(rnd)
                                lang = 'id'
                                tts = gTTS(text=p, lang=lang)
                                tts.save("hasil.mp3")
                                dz.sendAudio(msg.to,"hasil.mp3")
                                break
                    else:
                        pass
                    if resp["Tag2"] == True:          
                        contact = dz.getContact(msg._from)
                        cName = contact.displayName
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in dzMID:
                                dz.sendMessage(msg.to,cName+"\n"+Dhenza["tagteks2"])   
                                break
                    else:
                        pass
    except Exception as error:
        logError(error)
#==============================================================================#

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                dhenzaBot(op)
                # jangan di hapus bagian  dhenza, byar tidak terjadi troblle!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
