#!/usr/bin/env python3
#Logic: ARadio.py
#
# Logik zum AlexaRadio in AlexaRc4shNG
#
################################################################################################################

import json
import requests

tmpmeldung = ''
tmpsource = sh.return_item(trigger['source'])
tmpvalue = trigger['value']
if tmpvalue != None:
    tmpvalue = int(tmpvalue)
#logger.info('Quelle: ' + str(tmpsource) + ' - Wert: ' + str(tmpvalue))

def adrok(url):
    try:
        r = requests.get(url)
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def alexaradioan(sh):
    tmpakt = items.return_item(tmppfad+'.Sender.SenderAkt')()
    if (tmpakt.find("s") == 0) and (tmpakt[1:3].isdigit()):
        sh.AlexaRc4shNG.send_cmd(items.return_item(tmppfad+'.Geraet')(),'StartTuneInStation',items.return_item(tmppfad+'.Sender.SenderAkt')())
        #logger.info('TuneIn')
    else:
        sh.AlexaRc4shNG.send_cmd(items.return_item(tmppfad+'.Geraet')(),'PlaySpotifyPlaylist',items.return_item(tmppfad+'.Sender.SenderAkt')())
        #logger.info('Spotify')
    
    if items.return_item(tmppfad+'.Volume.An')() > 0:
        sh.AlexaRc4shNG.send_cmd(items.return_item(tmppfad+'.Geraet')(),'VolumeSet',str(items.return_item(tmppfad+'.Volume.An')()))

def alexaradioaus(sh):
    items.return_item(tmppfad+'.PlayPause').remove_timer()
    sh.AlexaRc4shNG.send_cmd(items.return_item(tmppfad+'.Geraet')(),'Pause',0)
    items.return_item(tmppfad+'.Sender.Info.artist')('...')
    items.return_item(tmppfad+'.Sender.Info.subText1')('...')
    items.return_item(tmppfad+'.Sender.Info.subText2')('...')
    
def alexainfo(sh):
    state,MediaInfo =sh.AlexaRc4shNG.get_player_info(items.return_item(tmppfad+'.Geraet')())
    #logger.info('State: ' + str(state) + ' - Info: ' + str(MediaInfo))
    #logger.info('ARadio MediaInfo Status: ' + str(state))
    if (MediaInfo is not None) and (str(state) == '200'):
        items.return_item(tmppfad+'.Sender.Info.artist')(MediaInfo["playerInfo"]["infoText"]["title"])
        items.return_item(tmppfad+'.Sender.Info.fan_art')(MediaInfo["playerInfo"]["miniArt"]["url"])
        items.return_item(tmppfad+'.Sender.Info.volume')(MediaInfo["playerInfo"]["volume"]["volume"])
        items.return_item(tmppfad+'.Sender.Info.mute')(MediaInfo["playerInfo"]["volume"]["muted"])
        items.return_item(tmppfad+'.Sender.Info.subText1')(MediaInfo["playerInfo"]["infoText"]["subText1"])
        items.return_item(tmppfad+'.Sender.Info.subText2')(MediaInfo["playerInfo"]["infoText"]["subText2"])
        
def logo(sh, logonr):
    if items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr)+'.Art')() == 1:
        if adrok('https://cdn-radiotime-logos.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + 'g.png'):
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('https://cdn-radiotime-logos.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + 'g.png')
        elif adrok('https://cdn-profiles.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + '/images/logod.png'):
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('https://cdn-profiles.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + '/images/logod.png')
        else:
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('icons/ws/control_dots_hor_f.svg')
    elif items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr)+'.Art')() == 2:
        if adrok('https://cdn-profiles.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + '/images/logod.png'):
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('https://cdn-profiles.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + '/images/logod.png')
        elif adrok('https://cdn-radiotime-logos.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + 'g.png'):
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('https://cdn-radiotime-logos.tunein.com/' + items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(logonr))() + 'g.png')
        else:
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('icons/ws/control_dots_hor_f.svg')
    else:
        items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr))('dropins/icons/ws/' + items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(logonr)+'.Lokal')())

def listeaendern(sh,tempindex):
    st = 0
    if tmpvalue == 91: # Eintrag löschen
        tempnr.pop(tempindex)
        tempname.pop(tempindex)
        if len(tempnr) < 5:
            tempnr.append('0')
            tempname.append('leer')
        if tempindex == 0:
            for x in range(1, 5):
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x)+'.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x+1)+'.Art')())
        if tempindex == 1:
            for x in range(2, 5):
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x)+'.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x+1)+'.Art')())
        if tempindex == 2:
            for x in range(3, 5):
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x)+'.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(x+1)+'.Art')())
        if tempindex == 3:
            items.return_item(tmppfad+'.Sender.SenderLogo.Logo4.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo5.Art')())
        st = 1
    if tmpvalue == 92: # Eintrag nach oben ins minus schieben
        if tempindex - 1 > -1:
            if tempindex < 5: 
                tempart = items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex)+'.Art')()
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex)+'.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+1)+'.Art')())
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+1)+'.Art')(tempart)
            tempnr.insert(tempindex - 1,tempnr.pop(tempindex))
            tempname.insert(tempindex - 1,tempname.pop(tempindex))
            st = 2
    if tmpvalue == 93: # Eintrag nach unten ins plus schieben
        if tempindex + 1 <= len(tempnr):
            if (tempindex >= 0) and (tempindex < 4): 
                tempart = items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+2)+'.Art')()
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+2)+'.Art')(items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+1)+'.Art')())
                items.return_item(tmppfad+'.Sender.SenderLogo.Logo'+str(tempindex+1)+'.Art')(tempart)
            tempnr.insert(tempindex + 1,tempnr.pop(tempindex))
            tempname.insert(tempindex + 1,tempname.pop(tempindex))
            st = 3
    if st > 0:
        items.return_item(tmppfad+'.Sender.SenderNr')(tempnr)
        items.return_item(tmppfad+'.Sender.SenderName')(tempname)
        for x in range(1, 6):
            items.return_item(tmppfad+'.Sender.SenderNr.Setup'+str(x))(tempnr[x-1])
            items.return_item(tmppfad+'.Sender.SenderName.Setup'+str(x))(tempname[x-1])
            logo(sh,x)

# AlexaRadio ItemPfad ermitteln:
tmppfad = str(tmpsource)
tmppfadende = tmppfad.find("AlexaRadio")
if tmppfadende != -1:
    tmppfad = tmppfad[0:tmppfadende+10]
    #logger.info(tmppfad)

if str(tmpsource) == tmppfad+'.Praesenzmelder': # AleaRadio per PM schalten
    if (tmpvalue == 1) and (items.return_item(tmppfad+'.Sperren')() == 0):
        if items.return_item(tmppfad+'.Sender.SenderPMLetzter')() != True:
            items.return_item(tmppfad+'.Sender.SenderAkt')(items.return_item(tmppfad+'.Sender.SenderStart')())
        items.return_item(tmppfad+'.PlayPause')(1)
    if tmpvalue == 0:
        if items.return_item(tmppfad+'.PlayPause')() > 0:
            items.return_item(tmppfad+'.PlayPause')(0)
if str(tmpsource) == tmppfad+'.PlayPause': #  AlexaRadio schalten
    if tmpvalue == 1:
        items.return_item(tmppfad+'.PlayPause').timer(6,10)
        alexaradioan(sh)

    elif tmpvalue == 10:
        alexainfo(sh)
        items.return_item(tmppfad+'.PlayPause').timer(20,10)
    else:
        alexaradioaus(sh)
if str(tmpsource) == tmppfad+'.Station': # Stationstasten schalten
    if (tmpvalue > 0) and (tmpvalue < 6):
        items.return_item(tmppfad+'.Sender.SenderAkt')(items.return_item(tmppfad+'.Sender.SenderNr')(index=tmpvalue-1))
        items.return_item(tmppfad+'.PlayPause').remove_timer()
        items.return_item(tmppfad+'.PlayPause')(1)

if str(tmpsource) == tmppfad+'.Sender.speichern': # Sender speichern
    if tmpvalue == 101:
        items.return_item(tmppfad+'.Sender.SenderNr')(items.return_item(tmppfad+'.Sender.SenderNr.Setup1')(),index = 0)
        items.return_item(tmppfad+'.Sender.SenderName')(items.return_item(tmppfad+'.Sender.SenderName.Setup1')(),index = 0)
        logo(sh,1)
    if tmpvalue == 102:
        items.return_item(tmppfad+'.Sender.SenderNr')(items.return_item(tmppfad+'.Sender.SenderNr.Setup2')(),index = 1)
        items.return_item(tmppfad+'.Sender.SenderName')(items.return_item(tmppfad+'.Sender.SenderName.Setup2')(),index = 1)
        logo(sh,2)
    if tmpvalue == 103:
        items.return_item(tmppfad+'.Sender.SenderNr')(items.return_item(tmppfad+'.Sender.SenderNr.Setup3')(),index = 2)
        items.return_item(tmppfad+'.Sender.SenderName')(items.return_item(tmppfad+'.Sender.SenderName.Setup3')(),index = 2)
        logo(sh,3)
    if tmpvalue == 104:
        items.return_item(tmppfad+'.Sender.SenderNr')(items.return_item(tmppfad+'.Sender.SenderNr.Setup4')(),index = 3)
        items.return_item(tmppfad+'.Sender.SenderName')(items.return_item(tmppfad+'.Sender.SenderName.Setup4')(),index = 3)
        logo(sh,4)
    if tmpvalue == 105:
        items.return_item(tmppfad+'.Sender.SenderNr')(items.return_item(tmppfad+'.Sender.SenderNr.Setup5')(),index = 4)
        items.return_item(tmppfad+'.Sender.SenderName')(items.return_item(tmppfad+'.Sender.SenderName.Setup5')(),index = 4)
        logo(sh,5)
    if tmpvalue == 90: # Eintrag hinzufügen
        if (items.return_item(tmppfad+'.Sender.SenderNr.aendern')() != '') and (items.return_item(tmppfad+'.Sender.SenderName.aendern')() != ''):
            tempnr = items.return_item(tmppfad+'.Sender.SenderNr')()
            tempname = items.return_item(tmppfad+'.Sender.SenderName')()
            tempnr.append(items.return_item(tmppfad+'.Sender.SenderNr.aendern')())
            tempname.append(items.return_item(tmppfad+'.Sender.SenderName.aendern')())
            items.return_item(tmppfad+'.Sender.SenderName')(tempname)
            items.return_item(tmppfad+'.Sender.SenderNr')(tempnr)
    if (tmpvalue == 91) or (tmpvalue == 92) or (tmpvalue == 93): # Eintrag löschen / verschieben
        if (items.return_item(tmppfad+'.Sender.SenderNr.aendern')() != '') or (items.return_item(tmppfad+'.Sender.SenderName.aendern')() != ''):
            tempnr = items.return_item(tmppfad+'.Sender.SenderNr')()
            tempname = items.return_item(tmppfad+'.Sender.SenderName')()
            if items.return_item(tmppfad+'.Sender.SenderNr.aendern')() != '':
                tempindex = tempnr.index(items.return_item(tmppfad+'.Sender.SenderNr.aendern')())
                if tempindex != -1: 
                    listeaendern(sh,tempindex)
            else:
                if items.return_item(tmppfad+'.Sender.SenderName.aendern')() != '':
                    tempindex = tempname.index(items.return_item(tmppfad+'.Sender.SenderName.aendern')())
                    if tempindex != -1: 
                        listeaendern(sh,tempindex)
            
if (str(tmpsource) == tmppfad+'.Volume.Setzen') and (tmpvalue == 1): # Lautstaerke setzen
    sh.AlexaRc4shNG.send_cmd(items.return_item(tmppfad+'.Geraet')(),'VolumeSet',str(items.return_item(tmppfad+'.Volume')()))
    #logger.info('Volume Wert: ' + items.return_item(tmppfad+'.Volume')())
    alexainfo(sh)

# Alexa Geräte in ein Item schreiben:
myDevices = sh.AlexaRc4shNG.Echos.devices
if myDevices != None:
    existingDevices = []
    for actDevice in myDevices:
      existingDevices.append(sh.AlexaRc4shNG.Echos.devices.get(actDevice).name)
    items.return_item(tmppfad+'.Meine_Geraete')(existingDevices)
