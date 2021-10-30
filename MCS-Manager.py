import os
import requests
import urllib.request
import glob

if not os.path.exists('vanillaservers'):
    os.mkdir('vanillaservers')
if not os.path.exists('forgeservers'):
    os.mkdir('forgeservers')
if not os.path.exists('fabricservers'):
    os.mkdir('fabricservers')

def writequeue():
    wqueuepy = open(file='mod-download-queue.py', mode='w+', encoding='utf-8')
    wqueuepy.write('import requests\nimport urllib.request\nimport time\nimport datetime\n\nrqueuelist = open(file=\'download-queue.txt\', mode=\'r\', encoding=\'utf-8\')\nrdqueuelist = rqueuelist.read()\nrqueuelist.close()\n\nbetterurllist = []\nurlistsearchbytesa = 0\nurlistsearchbytesb = 0\nfor x in rdqueuelist:\n    if rdqueuelist[urlistsearchbytesb] == \'\\n\':\n        betterurllist.append(rdqueuelist[urlistsearchbytesa:urlistsearchbytesb])\n        urlistsearchbytesa -= urlistsearchbytesa\n        urlistsearchbytesa += urlistsearchbytesb+1\n    urlistsearchbytesb += 1\nmodspath = betterurllist[0]\nbetterurllist.remove(betterurllist[0])\n\nmaxurls = 0\nfor x in betterurllist:\n    maxurls += 1\n\ncurrenturl = 1\ntimetaken = 0\nprint(\'Starting up Queue...\')\nprint(\'Please wait, this might take a while because of download limits\')\nprint()\nprint(\'Downloading Mods: \'+str(currenturl)+\'/\'+str(maxurls))\nwhile True:\n    if currenturl == maxurls+1:\n        print(\'It took \' + str(timetaken) + \' minutes to download \' + str(maxurls) + \' mods\')\n        print(\'Finished at \' + (str(datetime.datetime.now())[5:-7]))\n        print()\n        print(\'You can close this windows now\')\n        exit()\n    availabilitycheck = 0\n    modhtml = requests.get(betterurllist[currenturl-1])\n    modhtmlbytesa = 0\n    modhtmlbytesb = 0\n    for x in modhtml.text:\n        if x == \'\\n\':\n            modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]\n            if \'You\\\'re trying to download again too soon!\' in modhtmlline:\n                availabilitycheck = 1\n                break\n            if \'<td align=center class=middle><h1>\' in modhtmlline:\n                modnamesearchbytes = 0\n                for x in modhtmlline:\n                    if modhtmlline[modnamesearchbytes:modnamesearchbytes + 4] == \'.jar\':\n                        modnamebytesb = modnamesearchbytes + 4\n                    modnamesearchbytes += 1\n                modname = modhtmlline[35:modnamebytesb]\n            if \'document.getElementById(\\\"dl\\\").innerHTML = \\\'<a href=\\\"\' in modhtmlline:\n                moddownloadurlsearchbytes = 56\n                for x in modhtmlline:\n                    if modhtmlline[moddownloadurlsearchbytes] == \'\\\"\':\n                        moddownloadurl = modhtmlline[56:moddownloadurlsearchbytes]\n                        break\n                    moddownloadurlsearchbytes += 1\n            modhtmlbytesa -= modhtmlbytesa\n            modhtmlbytesa += modhtmlbytesb\n        modhtmlbytesb += 1\n    if availabilitycheck != 1:\n        moddownloadpath = modspath + \'\\\\\' + modname\n        print()\n        print(\'Found \' + modname + \'!\')\n        print(\'Downloading Mod...\')\n        urllib.request.urlretrieve(moddownloadurl, moddownloadpath)\n        print(\'Downloading Completed!\')\n        print()\n        currenturl += 1\n        if currenturl == maxurls + 1:\n            print(\'It took \' + str(timetaken) + \' minutes to download \' + str(maxurls) + \' mods\')\n            print(\'Finished at \' + (str(datetime.datetime.now())[5:-7]))\n            print()\n            print(\'You can close this windows now\')\n            exit()\n        print(\'Downloading Mods: \' + str(currenturl) + \'/\' + str(maxurls))\n    else:\n        print(\'Waiting...\')\n        time.sleep(95)\n        timetaken += 1')
    wqueuepy.close()

def listvanillaversions():
    versiondir = glob.glob("vanillaservers/*")
    versiondirline = 0
    for x in versiondir:
        mversiondirline = versiondir[versiondirline] + ' '
        print(mversiondirline[15:-1])
        versiondirline += 1
def listforgeversions():
    versiondir = glob.glob("forgeservers/*")
    versiondirline = 0
    for x in versiondir:
        mversiondirline = versiondir[versiondirline] + ' '
        print(mversiondirline[13:-1])
        versiondirline += 1
def listfabricversions():
    versiondir = glob.glob("fabricservers/*")
    versiondirline = 0
    for x in versiondir:
        mversiondirline = versiondir[versiondirline] + ' '
        print(mversiondirline[14:-1])
        versiondirline += 1

minecrafttype = input("Do you wish to manage \"vanilla\", \"forge\" or \"fabric\"?: ")
print()
while True:
    if minecrafttype != 'vanilla' and minecrafttype != 'forge' and minecrafttype != 'fabric':
        minecrafttype = input("Do you wish to manage \"vanilla\", \"forge\" or \"fabric\"?: ")
        print()

    if minecrafttype == 'vanilla':
        scoption = input("Do you wish to \"modify\"/\"start\" an existing server or \"create\" a new one? (\"menu\" to go back to menu): ")
        print()

        if scoption == 'menu':
            minecrafttype = input("Do you wish to manage \"vanilla\", \"forge\" or \"fabric\"?: ")
            print()

        if scoption == "exit":
            exit()

        if scoption == "start":
            listvanillaversions()
            startoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('vanillaservers\\'+startoptname):
                if startoptname != '':
                    startoptnamebytes = (len(startoptname.encode("utf8")))
                    startnamedir = glob.glob("vanillaservers/" + startoptname + "/*")
                    if startnamedir != ([]):
                        for x in startnamedir:
                            startnamedirline = 0
                            for x in startnamedir:
                                startmversiondirline = startnamedir[startnamedirline] + ' '
                                startmversiondirlinecut = startoptnamebytes + 16
                                print(startmversiondirline[startmversiondirlinecut:-1])
                                startnamedirline += 1
                            startoptservername = input("Which server do you want to start?: ")
                            print()
                            startserverpath = 'vanillaservers\\' + startoptname + '\\' + startoptservername
                            if os.path.exists(startserverpath):
                                if startoptservername != '':
                                    serverram = input('How much GB/MB of RAM would you like to use (Example 256MB, 1GB, 4GB) (Leave empty for default)?: ')
                                    if 'GB' or 'MB' in serverram or serverram == '':
                                        if 'GB' in serverram:
                                            RAMgb = serverram[0:-2]
                                            RAM = int(RAMgb)*1024
                                            print('Running Server on '+RAMgb+'GB...')
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx'+str(RAM)+'M -Xms'+str(RAM)+'M -jar server.jar nogui')
                                        if 'MB' in serverram:
                                            RAMmb = serverram[0:-2]
                                            RAM = int(RAMmb)*1
                                            print('Running Server on '+RAMmb+'MB...')
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx'+str(RAM)+'M -Xms'+str(RAM)+'M -jar server.jar nogui')
                                        if serverram == '':
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx1024M -Xms1024M -jar server.jar nogui')
                                    else:
                                        print('Value was entered incorrectly, please try again')
                                    print()

                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "modify":
            listvanillaversions()
            modifyoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('vanillaservers\\'+modifyoptname):
                if modifyoptname != '':
                    modifyoptnamebytes = (len(modifyoptname.encode("utf8")))
                    modifynamedir = glob.glob("vanillaservers/" + modifyoptname + "/*")
                    if modifynamedir != ([]):
                        for x in modifynamedir:
                            modifynamedirline = 0
                            for x in modifynamedir:
                                modifymversiondirline = modifynamedir[modifynamedirline] + ' '
                                modifymversiondirlinecut = modifyoptnamebytes + 16
                                print(modifymversiondirline[modifymversiondirlinecut:-1])
                                modifynamedirline += 1
                            modifyoptservername = input("Which server do you want to modify?: ")
                            print()
                            modifyserverpath = 'vanillaservers\\' + modifyoptname + '\\' + modifyoptservername
                            modifyopt = input('Do you wish to modify \"properties\" or \"delete\" this server?: ')

                            if modifyopt == 'delete':
                                print()
                                removeservercheck = input('Type out \"delete ' + modifyoptservername + '\" to confirm deletion of \"' + modifyoptservername + '\" running on \"' + modifyoptname + '\" version of minecraft: ')
                                if removeservercheck == 'delete ' + modifyoptservername:
                                    print('Deleting Server...')
                                    os.system('rmdir /S ' + modifyserverpath)
                                    if str(glob.glob("vanillaservers/" + modifyoptname + "/*")) == '[]':
                                        deletionversionpath = 'vanillaservers\\' + modifyoptname
                                        os.system('rmdir /S ' + deletionversionpath)
                                    print('Deletion Completed!')
                                    print()

                            if modifyopt == 'properties':
                                propertiespath = modifyserverpath + '\\server.properties'
                                if os.path.exists(modifyserverpath):
                                    if modifyoptservername != '':
                                        try:
                                            if not os.path.exists(propertiespath):
                                                with open(os.path.join(os.path.dirname(__file__), propertiespath), 'a+') as createserverproperties:
                                                    print('Creating Properties File...')
                                                    createserverproperties.close()
                                                    with open(os.path.join(os.path.dirname(__file__), propertiespath), 'w') as wserverproperties:
                                                        wserverproperties.write('view-distance=10\nmax-build-height=256\nserver-ip=\nlevel-seed=\ngamemode=0\nserver-port=25565\nenable-command-block=false\nallow-nether=true\nenable-rcon=false\nop-permission-level=4\nenable-query=false\ngenerator-settings=\nresource-pack=\nplayer-idle-timeout=0\nlevel-name=world\nmotd=A Minecraft Server\nannounce-player-achievements=true\nforce-gamemode=false\nhardcore=false\nwhite-list=false\npvp=true\nspawn-npcs=true\ngenerate-structures=true\nspawn-animals=true\nsnooper-enabled=true\ndifficulty=1\nnetwork-compression-threshold=256\nlevel-type=DEFAULT\nspawn-monsters=true\nmax-tick-time=60000\nmax-players=20\nresource-pack-sha1=\nonline-mode=true\nallow-flight=false\nmax-world-size=29999984')
                                                        wserverproperties.close()
                                            with open(os.path.join(os.path.dirname(__file__), propertiespath), 'r+') as rserverproperties:
                                                rproperties = rserverproperties.readlines()
                                                rserverproperties.close()
                                        except:
                                            print()
                                            print('Error: No such file or directory')
                                            exit()
                                        propertiesline = -1
                                        maxpropertiesline = 0
                                        modifiedproperties = []
                                        print()
                                        for x in rproperties:
                                            maxpropertiesline += 1
                                        for x in rproperties:
                                            propertiesline += 1
                                            modifyline = rproperties[propertiesline][0:-1]
                                            if '#' not in modifyline:
                                                print('Line: ' + str(propertiesline + 1) + '/' + str(maxpropertiesline))
                                                print(modifyline)
                                                modifyinput = input('Do you wish to edit this line if not leave this field empty? (If you want to make field empty type \"empty\"): ')
                                                print()
                                                if modifyinput == '':
                                                    modifiedproperties.append(modifyline)
                                                else:
                                                    if modifyinput == 'empty':
                                                        modifyinput = ''
                                                    searchmodifyline = 0
                                                    for x in modifyline:
                                                        if modifyline[searchmodifyline] == '=':
                                                            bmodifyline = (modifyline[0:searchmodifyline+1])
                                                            modifiedproperties.append(bmodifyline+modifyinput)
                                                        searchmodifyline += 1
                                        with open(os.path.join(os.path.dirname(__file__), propertiespath), 'w') as wproperty:
                                            for modifiedpropertiesline in modifiedproperties:
                                                wproperty.write(modifiedpropertiesline+"\n")
                                            wproperty.close()
                                        print('All settings were saved')
                                        print()
                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "create":
            imkversion = input("What version of server do you want to create? (example 1.17.1): ")
            dmcsurl = 'https://mcversions.net/download/'
            mkversion = 'vanillaservers\\' + imkversion
            dvurl = dmcsurl + imkversion
            dvhtml = requests.get(url=dvurl)
            if '<Response [200]>' in str(dvhtml):
                chtmlc = dvhtml.text
                searcha = 0
                searchb = 10
                print('Searching for Download Link...')
                for x in chtmlc:
                    searcha += 1
                    searchb += 1
                    search = (chtmlc[searcha:searchb])
                    if search == "server.jar":
                        print('Download Link Found!')
                        break
                serversearcha = searcha-80
                serverurl = (chtmlc[serversearcha:searchb])
                #print(serverurl)
                if not os.path.exists(mkversion):
                    os.mkdir(mkversion)
                print()
                servername = input("Name your Server: ")
                mkversionname = mkversion + '\\' + servername
                if not os.path.exists(mkversionname):
                    os.mkdir(mkversionname)
                    serverjarloc = mkversionname + '\server.jar'
                    print('Downloading Server...')
                    urllib.request.urlretrieve(serverurl, serverjarloc)
                    print('Downloading Completed!')
                    print()
                    eulapath = mkversionname+'\\eula.txt'
                    with open(os.path.join(os.path.dirname(__file__), eulapath), 'w+') as eulainput_file:
                        weula = eulainput_file.write('eula=true')
                        eulainput_file.close()
                else:
                    print('Name Already Exists')
                    print()
            else:
                if '<Response [404]>' in str(dvhtml):
                    print('Error 404: Version Not Found')
                    print()
                else:
                    print('Unknown Error: ' + str(dvhtml))
                    print()

    if minecrafttype == 'forge':
        scoption = input("Do you wish to \"modify\"/\"start\" an existing server or \"create\" a new one? (\"menu\" to go back to menu): ")
        print()

        if scoption == 'menu':
            minecrafttype = input("Do you wish to manage \"vanilla\", \"forge\" or \"fabric\"?: ")
            print()

        if scoption == "exit":
            exit()

        if scoption == "start":
            listforgeversions()
            startoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('forgeservers\\'+startoptname):
                if startoptname != '':
                    startoptnamebytes = (len(startoptname.encode("utf8")))
                    startnamedir = glob.glob("forgeservers/" + startoptname + "/*")
                    if startnamedir != ([]):
                        for x in startnamedir:
                            startnamedirline = 0
                            for x in startnamedir:
                                startmversiondirline = startnamedir[startnamedirline] + ' '
                                startmversiondirlinecut = startoptnamebytes + 14
                                print(startmversiondirline[startmversiondirlinecut:-1])
                                startnamedirline += 1
                            startoptservername = input("Which server do you want to start?: ")
                            print()
                            startserverpath = 'forgeservers\\' + startoptname + '\\' + startoptservername
                            if os.path.exists(startserverpath):
                                if startoptservername != '':
                                    runbatpath = startserverpath + '\\run.bat'
                                    userjvmargspath = startserverpath + '\\user_jvm_args.txt'
                                    serverram = input('How much GB/MB of RAM would you like to use (Example 256MB, 1GB, 4GB) (Leave empty for default)?: ')
                                    if os.path.exists(runbatpath):
                                        with open(os.path.join(os.path.dirname(__file__), userjvmargspath), 'w+') as userjvmargs:
                                            userjvmargsfull = '# Xmx and Xms set the maximum and minimum RAM usage, respectively.\n# They can take any number, followed by an M or a G.\n# M means Megabyte, G means Gigabyte.\n# For example, to set the maximum to 3GB: -Xmx3G\n# To set the minimum to 2.5GB: -Xms2500M\n\n# A good default for a modded server is 4GB.\n# Uncomment the next line to set it.\n# -Xmx4G'
                                            defaultmsg = 0
                                            if 'GB' in serverram:
                                                RAMgb = serverram[0:-2]
                                                RAM = int(RAMgb) * 1
                                                print('Running Server on ' + RAMgb + 'GB...')
                                                print()
                                                userjvmargsfull = '# Xmx and Xms set the maximum and minimum RAM usage, respectively.\n# They can take any number, followed by an M or a G.\n# M means Megabyte, G means Gigabyte.\n# For example, to set the maximum to 3GB: -Xmx3G\n# To set the minimum to 2.5GB: -Xms2500M\n\n# A good default for a modded server is 4GB.\n# Uncomment the next line to set it.\n# -Xmx'+str(RAM)+'G'
                                            else:
                                                defaultmsg += 1

                                            if 'MB' in serverram:
                                                RAMmb = serverram[0:-2]
                                                RAM = int(RAMmb)/1024
                                                print('Running Server on ' + RAMmb + 'MB...')
                                                print()
                                                userjvmargsfull = '# Xmx and Xms set the maximum and minimum RAM usage, respectively.\n# They can take any number, followed by an M or a G.\n# M means Megabyte, G means Gigabyte.\n# For example, to set the maximum to 3GB: -Xmx3G\n# To set the minimum to 2.5GB: -Xms2500M\n\n# A good default for a modded server is 4GB.\n# Uncomment the next line to set it.\n# -Xmx'+str(RAM)+'G'
                                            else:
                                                defaultmsg += 1
                                            if defaultmsg == 2:
                                                print('Running Server on Default Ram (4GB)...')
                                                print()
                                            for userjvmargsline in userjvmargsfull:
                                                userjvmargs.write(userjvmargsline)
                                            userjvmargs.close()
                                        print('Enter \"stop\" into Server Console to Stop the Server')
                                        os.system('cd ' + startserverpath + ' && run.bat')
                                        print()
                                    else:
                                        if 'GB' or 'MB' in serverram:
                                            if 'GB' in serverram:
                                                RAMgb = serverram[0:-2]
                                                RAM = int(RAMgb) * 1024
                                                print('Running Server on ' + RAMgb + 'GB...')
                                                print()
                                                print('Enter \"stop\" into Server Console to Stop the Server')
                                                os.system('cd ' + startserverpath + ' && java -Xmx'+str(RAM)+'M -Xms'+str(RAM)+'M -jar minecraft_server.'+startoptname+'.jar nogui')
                                                print()

                                            if 'MB' in serverram:
                                                RAMmb = serverram[0:-2]
                                                RAM = int(RAMmb) * 1
                                                print('Running Server on ' + RAMmb + 'MB...')
                                                print()
                                                print('Enter \"stop\" into Server Console to Stop the Server')
                                                os.system('cd ' + startserverpath + ' && java -Xmx'+str(RAM)+'M -Xms'+str(RAM)+'M -jar minecraft_server.'+startoptname+'.jar nogui')
                                                print()

                                            if serverram == '':
                                                print('Running Server on Default Ram (4GB)...')
                                                print()
                                                print('Enter \"stop\" into Server Console to Stop the Server')
                                                os.system('cd ' + startserverpath + ' && java -Xmx4096M -Xms4096M -jar minecraft_server.'+startoptname+'.jar nogui')
                                                print()
                                            else:
                                                print('Value was entered incorrectly, please try again')
                                                print()

                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "modify":
            listforgeversions()
            modifyoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('forgeservers\\'+modifyoptname):
                if modifyoptname != '':
                    modifyoptnamebytes = (len(modifyoptname.encode("utf8")))
                    modifynamedir = glob.glob("forgeservers/" + modifyoptname + "/*")
                    if modifynamedir != ([]):
                        for x in modifynamedir:
                            modifynamedirline = 0
                            for x in modifynamedir:
                                modifymversiondirline = modifynamedir[modifynamedirline] + ' '
                                modifymversiondirlinecut = modifyoptnamebytes + 14
                                print(modifymversiondirline[modifymversiondirlinecut:-1])
                                modifynamedirline += 1
                            modifyoptservername = input("Which server do you want to modify?: ")
                            print()
                            modifyserverpath = 'forgeservers\\' + modifyoptname + '\\' + modifyoptservername
                            modifyopt = input('Do you wish to modify \"properties\", \"mods\" or \"delete\" this server?: ')

                            if modifyopt == 'delete':
                                print()
                                removeservercheck = input('Type out \"delete '+modifyoptservername+'\" to confirm deletion of \"'+modifyoptservername+'\" running on \"'+modifyoptname+'\" version of minecraft: ')
                                if removeservercheck == 'delete '+modifyoptservername:
                                    print('Deleting Server...')
                                    os.system('rmdir /S '+modifyserverpath)
                                    if str(glob.glob("forgeservers/"+modifyoptname+"/*")) == '[]':
                                        deletionversionpath = 'forgeservers\\'+modifyoptname
                                        os.system('rmdir /S '+deletionversionpath)
                                    print('Deletion Completed!')
                                    print()

                            if modifyopt == 'mods':
                                modfolderpath = modifyserverpath + '\\mods'
                                if not os.path.exists(modfolderpath):
                                    os.mkdir(modfolderpath)
                                modsopt = input('Do you wish to \"download\" or \"remove\" mods?: ')
                                print()

                                if modsopt == 'remove':
                                    uncutmodlist = glob.glob(modfolderpath+'/*')
                                    if uncutmodlist == ([]):
                                        print('Mod Folder is Empty')
                                        print()
                                    else:
                                        modlist = []
                                        currentmod = 0
                                        for uncutsinglemod in uncutmodlist:
                                            currentmod += 1
                                            singlemod = (uncutsinglemod+' ')[len(modfolderpath)+1:-1]
                                            modlist.append(singlemod)
                                            print(str(currentmod)+' - '+singlemod)
                                        print()
                                        modsremoveopt = input('Which mods would you like to remove? (Select numbers of mods you want to remove or type out \"all\" to remove everything, foramt: 1, 3, 8): ')
                                        if modsremoveopt == 'all':
                                            print()
                                            print('Removing ALL Mods...')
                                            os.system('rmdir /S '+modfolderpath)
                                            print('Removal of ALL Mods Completed!')
                                            print()
                                        else:
                                            numbermodremovelist = []
                                            modremovecommabytesa = 0
                                            modremovecommabytesb = 0
                                            for modremovecommas in modsremoveopt:
                                                if modremovecommas == ',':
                                                    numbermodremovelist.append(modsremoveopt[modremovecommabytesa:modremovecommabytesb])
                                                    modremovecommabytesa -= modremovecommabytesa
                                                    modremovecommabytesa += modremovecommabytesb + 2
                                                modremovecommabytesb += 1
                                            numbermodremovelist.append(modsremoveopt[modremovecommabytesa:len(modsremoveopt)])

                                            modtoremovelist = []
                                            for numbermodtoremove in numbermodremovelist:
                                                try:
                                                    modtoremovelist.append(modlist[int(numbermodtoremove)-1])
                                                except:
                                                    print('Error: Bad Format or Out of Range, MOD NUMBER: '+numbermodtoremove)

                                            if str(modtoremovelist) != '[]':
                                                print()
                                                print('Removing Mods...')
                                                for modtoremove in modtoremovelist:
                                                    modremovepath = 'forgeservers/'+modifyoptname+'/'+modifyoptservername+'/mods/'+modtoremove
                                                    print('Removing '+modtoremove+'...')
                                                    os.remove(modremovepath)
                                                print('Removal of Mods Completed!')
                                            print()

                                if modsopt == 'download':
                                    print('(Currently supporting only 9minecraft.net, mc-mod.net, mod-minecraft.net file hosting and direct .jar files)')
                                    modurl = input('Please Enter Mod Download Urls (Format for more urls: url1, url2, url3): ')
                                    print()

                                    queuelist = []
                                    queuelistcheck = []
                                    queuelist.append(modfolderpath)
                                    queuelistcheck.append(modfolderpath)
                                    modurllist = []
                                    modurlcommabytesa = 0
                                    modurlcommabytesb = 0
                                    for modurlcommas in modurl:
                                        if modurlcommas == ',':
                                            modurllist.append(modurl[modurlcommabytesa:modurlcommabytesb])
                                            modurlcommabytesa -= modurlcommabytesa
                                            modurlcommabytesa += modurlcommabytesb+2
                                        modurlcommabytesb += 1
                                    modurllist.append(modurl[modurlcommabytesa:len(modurl)])

                                    maxmodurls = 0
                                    currentmodurl = 0
                                    for maxsinglemodurl in modurllist:
                                        maxmodurls += 1

                                    for singlemodurl in modurllist:
                                        currentmodurl += 1
                                        print('Mods: '+str(currentmodurl)+'/'+str(maxmodurls))
                                        if (singlemodurl+' ')[-5:-1] == '.jar':
                                            try:
                                                directjarnamesearchbyte = len(singlemodurl)-1
                                                for x in singlemodurl:
                                                    if (singlemodurl[directjarnamesearchbyte]) == '/':
                                                        directjarnamebytea = directjarnamesearchbyte
                                                        directjarname = singlemodurl[directjarnamebytea+1:len(singlemodurl)]
                                                        print('Found ' + directjarname + '!')
                                                        break
                                                    directjarnamesearchbyte -= 1
                                                directjarmoddownloadpath = modfolderpath + '\\' + directjarname
                                                print('Downloading Mod...')
                                                urllib.request.urlretrieve(singlemodurl, directjarmoddownloadpath)
                                                print('Downloading Completed!')
                                                print()
                                            except:
                                                try:
                                                    downloaddirectjar = requests.get(singlemodurl, allow_redirects=True)
                                                    open(directjarmoddownloadpath, 'wb').write(downloaddirectjar.content)
                                                    print('Downloading Completed!')
                                                    print()
                                                except:
                                                    if str(downloaddirectjar) == '<Response [403]>':
                                                        print('Error 403: This site won\'t work. URL Number: ' + str(currentmodurl))
                                                    else:
                                                        print('Error! Please make sure you entered download url correctly')
                                                        print()
                                        else:
                                            if 'mc-mod.net/' in singlemodurl:
                                                if 'index.php?act=download&id=' in singlemodurl:
                                                    nineminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[nineminecraftmodidsearch:nineminecraftmodidsearch+3] == 'id=':
                                                            nineminecraftmodidbytesa = nineminecraftmodidsearch+3
                                                        if singlemodurl[nineminecraftmodidsearch] == '&':
                                                            nineminecraftmodidbytesb = nineminecraftmodidsearch
                                                        nineminecraftmodidsearch += 1
                                                    nineminecraftmodid = singlemodurl[nineminecraftmodidbytesa:nineminecraftmodidbytesb]
                                                    if 'https://files.mc-mod.net' in singlemodurl:
                                                        singlemodurl = 'https://download.mc-mod.net/index.php?act=dl&id='+nineminecraftmodid #New URL
                                                    elif 'https://download.mc-mod.net' in singlemodurl:
                                                        singlemodurl = 'https://download.mc-mod.net/index.php?act=dl&id='+nineminecraftmodid #New URL
                                                try:
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(url='https://download.mc-mod.net/index.php?act=dl&id=')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'File name: ' in modhtmlline:
                                                                    modhtmllinecut = modhtmlline[1:-1]
                                                                    anchorpointposition = 0
                                                                    anchorpointlist = []
                                                                    for anchorpoint in modhtmllinecut:
                                                                        if anchorpoint == '\"':
                                                                            anchorpointlist.append(anchorpointposition)
                                                                        anchorpointposition += 1
                                                                    moddownloadurl = modhtmllinecut[anchorpointlist[0]+1:anchorpointlist[1]]
                                                                    modnamelinesearch = anchorpointlist[2]+31
                                                                    for nameanchorpoint in modhtmllinecut:
                                                                        if modhtmllinecut[modnamelinesearch:modnamelinesearch+4] == '.jar':
                                                                            modnameline = modnamelinesearch+4
                                                                        modnamelinesearch += 1
                                                                    modname = modhtmllinecut[anchorpointlist[2]+31:modnameline]
                                                                    print('Found '+modname+'!')
                                                                    break
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath+'\\'+modname
                                                        print('Downloading Mod...')
                                                        urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                        print('Downloading Completed!')
                                                        print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    print('Error! Please make sure you entered download url correctly')
                                                    print()

                                            if 'mod-minecraft.net' in singlemodurl:
                                                if 'download2.php?a=' in singlemodurl:
                                                    modminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[modminecraftmodidsearch:modminecraftmodidsearch+6] == 'php?a=':
                                                            modminecraftmodidbytesa = modminecraftmodidsearch+6
                                                        if singlemodurl[modminecraftmodidsearch] == '&':
                                                            modminecraftmodidbytesb = modminecraftmodidsearch
                                                        modminecraftmodidsearch += 1
                                                    modminecraftmodid = singlemodurl[modminecraftmodidbytesa:modminecraftmodidbytesb]
                                                    singlemodurl = 'http://dl3.mod-minecraft.net/download.php?file='+modminecraftmodid #New URL
                                                try:
                                                    queuecheck = 0
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(url='http://dl3.mod-minecraft.net/download.php?file=')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'You\'re trying to download again too soon!' in modhtmlline:
                                                                    print('mod-minecraft.net has download limit, url was added to the queue. URL Number: ' + str(currentmodurl))
                                                                    queuecheck = 1
                                                                    queuelist.append(singlemodurl)
                                                                    break
                                                                if '<td align=center class=middle><h1>' in modhtmlline:
                                                                    modnamesearchbytes = 0
                                                                    for x in modhtmlline:
                                                                        if modhtmlline[modnamesearchbytes:modnamesearchbytes+4] == '.jar':
                                                                            modnamebytesb = modnamesearchbytes+4
                                                                        modnamesearchbytes += 1
                                                                    modname = modhtmlline[35:modnamebytesb]
                                                                    print('Found '+modname+'!')
                                                                if 'document.getElementById(\"dl\").innerHTML = \'<a href=\"' in modhtmlline:
                                                                    moddownloadurlsearchbytes = 56
                                                                    for x in modhtmlline:
                                                                        if modhtmlline[moddownloadurlsearchbytes] == '\"':
                                                                            moddownloadurl = modhtmlline[56:moddownloadurlsearchbytes]
                                                                            break
                                                                        moddownloadurlsearchbytes += 1
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath+'\\'+modname
                                                        if queuecheck != 1:
                                                            print('Downloading Mod...')
                                                            urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                            print('Downloading Completed!')
                                                            print()
                                                        else:
                                                            print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    if queuecheck == 1:
                                                        print()
                                                    else:
                                                        print('Error! Please make sure you entered download url correctly')
                                                        print()

                                            if '9minecraft.net/' in singlemodurl:
                                                if 'index.php?act=download&id=' in singlemodurl:
                                                    nineminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[nineminecraftmodidsearch:nineminecraftmodidsearch+3] == 'id=':
                                                            nineminecraftmodidbytesa = nineminecraftmodidsearch+3
                                                        if singlemodurl[nineminecraftmodidsearch] == '&':
                                                            nineminecraftmodidbytesb = nineminecraftmodidsearch
                                                        nineminecraftmodidsearch += 1
                                                    nineminecraftmodid = singlemodurl[nineminecraftmodidbytesa:nineminecraftmodidbytesb]
                                                    if singlemodurl[0:28] != 'https://files.9minecraft.net':
                                                        singlemodurl = singlemodurl[0:29]+'/index.php?act=dl&id='+nineminecraftmodid #New URL
                                                    else:
                                                        singlemodurl = 'https://files.9minecraft.net/index.php?act=dl&id='+nineminecraftmodid #New URL
                                                try:
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(url='https://files.9minecraft.net/index.php?act=dl&id=0')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'File name: ' in modhtmlline:
                                                                    modhtmllinecut = modhtmlline[1:-1]
                                                                    anchorpointposition = 0
                                                                    anchorpointlist = []
                                                                    for anchorpoint in modhtmllinecut:
                                                                        if anchorpoint == '\"':
                                                                            anchorpointlist.append(anchorpointposition)
                                                                        anchorpointposition += 1
                                                                    moddownloadurl = modhtmllinecut[anchorpointlist[0]+1:anchorpointlist[1]]
                                                                    modnamelinesearch = anchorpointlist[2]+31
                                                                    for nameanchorpoint in modhtmllinecut:
                                                                        if modhtmllinecut[modnamelinesearch:modnamelinesearch+4] == '.jar':
                                                                            modnameline = modnamelinesearch+4
                                                                        modnamelinesearch += 1
                                                                    modname = modhtmllinecut[anchorpointlist[2]+31:modnameline]
                                                                    print('Found '+modname+'!')
                                                                    break
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath+'\\'+modname
                                                        print('Downloading Mod...')
                                                        urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                        print('Downloading Completed!')
                                                        print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    print('Error! Please make sure you entered download url correctly')
                                                    print()

                                    open(file='download-queue.txt', mode='w+', encoding='utf-8')
                                    wqueue = open(file='download-queue.txt', mode='w', encoding='utf-8')
                                    for singlequeuelink in queuelist:
                                        wqueue.write(singlequeuelink+'\n')
                                    wqueue.close()
                                    if str(queuelist) != str(queuelistcheck):
                                        writequeue()
                                        os.system('start cmd /k python mod-download-queue.py && exit')

                            if modifyopt == 'properties':
                                propertiespath = modifyserverpath + '\\server.properties'
                                if os.path.exists(modifyserverpath):
                                    if modifyoptservername != '':
                                        try:
                                            if not os.path.exists(propertiespath):
                                                with open(os.path.join(os.path.dirname(__file__), propertiespath),
                                                          'a+') as createserverproperties:
                                                    print('Creating Properties File...')
                                                    createserverproperties.close()
                                                    with open(os.path.join(os.path.dirname(__file__), propertiespath), 'w') as wserverproperties:
                                                        wserverproperties.write('enable-jmx-monitoring=false\nrcon.port=25575\nlevel-seed=\ngamemode=survival\nenable-command-block=false\nenable-query=false\ngenerator-settings=\nlevel-name=world\nmotd=A Minecraft Server\nquery.port=25565\npvp=true\ngenerate-structures=true\ndifficulty=easy\nnetwork-compression-threshold=256\nmax-tick-time=60000\nuse-native-transport=true\nmax-players=20\nonline-mode=true\nenable-status=true\nallow-flight=false\nbroadcast-rcon-to-ops=true\nview-distance=10\nmax-build-height=256\nserver-ip=\nallow-nether=true\nserver-port=25565\nenable-rcon=false\nsync-chunk-writes=true\nop-permission-level=4\nprevent-proxy-connections=false\nresource-pack=\nentity-broadcast-range-percentage=100\nrcon.password=\nplayer-idle-timeout=0\nforce-gamemode=false\nrate-limit=0\nhardcore=false\nwhite-list=false\nbroadcast-console-to-ops=true\nspawn-npcs=true\nspawn-animals=true\nsnooper-enabled=true\nfunction-permission-level=2\nlevel-type=default\ntext-filtering-config=\nspawn-monsters=true\nenforce-whitelist=false\nresource-pack-sha1=\nspawn-protection=16\nmax-world-size=29999984')
                                                        wserverproperties.close()
                                            with open(os.path.join(os.path.dirname(__file__), propertiespath), 'r+') as rserverproperties:
                                                rproperties = rserverproperties.readlines()
                                                rserverproperties.close()
                                        except:
                                            print()
                                            print('Error: No such file or directory')
                                            exit()
                                        propertiesline = -1
                                        maxpropertiesline = 0
                                        modifiedproperties = []
                                        print()
                                        for x in rproperties:
                                            maxpropertiesline += 1
                                        for x in rproperties:
                                            propertiesline += 1
                                            modifyline = rproperties[propertiesline][0:-1]
                                            if '#' not in modifyline:
                                                print('Line: '+str(propertiesline+1)+'/'+str(maxpropertiesline))
                                                print(modifyline)
                                                modifyinput = input('Do you wish to edit this line if not leave this field empty? (If you want to make field empty type \"empty\"): ')
                                                print()
                                                if modifyinput == '':
                                                    modifiedproperties.append(modifyline)
                                                else:
                                                    if modifyinput == 'empty':
                                                        modifyinput = ''
                                                    searchmodifyline = 0
                                                    for x in modifyline:
                                                        if modifyline[searchmodifyline] == '=':
                                                            bmodifyline = (modifyline[0:searchmodifyline + 1])
                                                            modifiedproperties.append(bmodifyline + modifyinput)
                                                        searchmodifyline += 1
                                        with open(os.path.join(os.path.dirname(__file__), propertiespath), 'w') as wproperty:
                                            for modifiedpropertiesline in modifiedproperties:
                                                wproperty.write(modifiedpropertiesline + "\n")
                                            wproperty.close()
                                        print('All settings were saved')
                                        print()
                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "create":
            imkversion = input("What version of server do you want to create? (example 1.17.1) (Oldest Supported Version is 1.5.2): ")
            mkversion = 'forgeservers\\' + imkversion
            forgeinstallerurl = 'https://files.minecraftforge.net/net/minecraftforge/forge/index_' + imkversion + '.html'
            forgeinstallerhtml = requests.get(forgeinstallerurl)
            if str(forgeinstallerhtml) == "<Response [200]>":
                print('Version Found!')
                forgeinstallersearcharea = forgeinstallerhtml.text[0:2000]
                latestforgeline = ''
                recommendedforgeline = ''
                forgesearcha = 0
                forgesearchb = 0
                for x in forgeinstallersearcharea:
                    if x == '\n':
                        forgesearchline = forgeinstallersearcharea[forgesearcha:forgesearchb] + ' '
                        forgesearchlinecut = forgesearchline[1:-1]
                        if 'Latest: ' in forgesearchlinecut:
                            latestforgeline = forgesearchlinecut
                            if '>' in latestforgeline:
                                latestforgeline = latestforgeline[0:len(latestforgeline) - 3]
                        if 'Recommended: ' in forgesearchlinecut:
                            recommendedforgeline = forgesearchlinecut
                            if '>' in recommendedforgeline:
                                recommendedforgeline = recommendedforgeline[0:len(recommendedforgeline) - 3]
                        forgesearcha -= forgesearcha
                        forgesearcha += forgesearchb
                    forgesearchb += 1
                if recommendedforgeline != '':
                     forgerelease = recommendedforgeline[13:len(recommendedforgeline)]
                else:
                    if latestforgeline != '':
                        forgerelease = latestforgeline[8:len(latestforgeline)]
                    else:
                        forgerelease = ''
                        print('Suitable Forge Release wasn\'t Found')
                if forgerelease != '':
                    forgedownloadurl = 'https://maven.minecraftforge.net/net/minecraftforge/forge/'+imkversion+'-'+forgerelease+'/forge-'+imkversion+'-'+forgerelease+'-installer.jar'
                    if not os.path.exists(mkversion):
                        os.mkdir(mkversion)
                    servername = input("Name your Server: ")
                    mkversionname = mkversion + '\\' + servername
                    if not os.path.exists(mkversionname):
                        os.mkdir(mkversionname)
                    forgeinstallername = 'forge-'+imkversion+'-'+forgerelease+'-installer.jar'
                    forgeinstallerloc = mkversionname + '\\' + forgeinstallername
                    print('Downloading Server...')
                    urllib.request.urlretrieve(forgedownloadurl, forgeinstallerloc)
                    print('Downloading Completed!')
                    print()
                    print('Installing Server...')
                    os.system('cd '+mkversionname+' && java -jar '+forgeinstallername+' --install')
                    print()
                    print('Server Installation Complete!')
                    print('Deleting Installer..')
                    os.system('cd '+mkversionname+' && del '+forgeinstallername)
                    runbatpath = mkversionname+'\\run.bat'
                    cpropertiespath = mkversionname+'\\server.properties'
                    if os.path.exists(runbatpath):
                        with open(os.path.join(os.path.dirname(__file__), runbatpath), 'w+') as runbatrewrite:
                            runbatrewrite.write('REM Forge requires a configured set of both JVM and program arguments.\nREM Add custom JVM arguments to the user_jvm_args.txt\nREM Add custom program arguments {such as nogui} to this file in the next line before the %* or\nREM  pass them to this script directly\njava @user_jvm_args.txt @libraries/net/minecraftforge/forge/'+imkversion+'-'+forgerelease+'/win_args.txt nogui %*')
                            runbatrewrite.close()
                    eulapath = mkversionname+'\\eula.txt'
                    with open(os.path.join(os.path.dirname(__file__), eulapath), 'w+') as eulainput_file:
                        weula = eulainput_file.write('eula=true')
                        eulainput_file.close()
                    with open(os.path.join(os.path.dirname(__file__), cpropertiespath), 'w+') as cwserverproperties:
                        cwserverproperties.write('enable-jmx-monitoring=false\nrcon.port=25575\nlevel-seed=\ngamemode=survival\nenable-command-block=false\nenable-query=false\ngenerator-settings=\nlevel-name=world\nmotd=A Minecraft Server\nquery.port=25565\npvp=true\ngenerate-structures=true\ndifficulty=easy\nnetwork-compression-threshold=256\nmax-tick-time=60000\nuse-native-transport=true\nmax-players=20\nonline-mode=true\nenable-status=true\nallow-flight=false\nbroadcast-rcon-to-ops=true\nview-distance=10\nmax-build-height=256\nserver-ip=\nallow-nether=true\nserver-port=25565\nenable-rcon=false\nsync-chunk-writes=true\nop-permission-level=4\nprevent-proxy-connections=false\nresource-pack=\nentity-broadcast-range-percentage=100\nrcon.password=\nplayer-idle-timeout=0\nforce-gamemode=false\nrate-limit=0\nhardcore=false\nwhite-list=false\nbroadcast-console-to-ops=true\nspawn-npcs=true\nspawn-animals=true\nsnooper-enabled=true\nfunction-permission-level=2\nlevel-type=default\ntext-filtering-config=\nspawn-monsters=true\nenforce-whitelist=false\nresource-pack-sha1=\nspawn-protection=16\nmax-world-size=29999984')
                        cwserverproperties.close()
                    print('DONE!')
                    print()
            else:
                if str(forgeinstallerhtml) == "<Response [404]>":
                    print('Error 404: Version Not Found')
                else:
                    print('Unknown Error: ' + str(forgeinstallerhtml))

    if minecrafttype == 'fabric':
        scoption = input(
            "Do you wish to \"modify\"/\"start\" an existing server or \"create\" a new one? (\"menu\" to go back to menu): ")
        print()

        if scoption == 'menu':
            minecrafttype = input("Do you wish to manage \"vanilla\", \"forge\" or \"fabric\"?: ")
            print()

        if scoption == "exit":
            exit()

        if scoption == "start":
            listfabricversions()
            startoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('fabricservers\\' + startoptname):
                if startoptname != '':
                    startoptnamebytes = (len(startoptname.encode("utf8")))
                    startnamedir = glob.glob("fabricservers/" + startoptname + "/*")
                    if startnamedir != ([]):
                        for x in startnamedir:
                            startnamedirline = 0
                            for x in startnamedir:
                                startmversiondirline = startnamedir[startnamedirline] + ' '
                                startmversiondirlinecut = startoptnamebytes + 15
                                print(startmversiondirline[startmversiondirlinecut:-1])
                                startnamedirline += 1
                            startoptservername = input("Which server do you want to start?: ")
                            print()
                            startserverpath = 'fabricservers\\' + startoptname + '\\' + startoptservername
                            if os.path.exists(startserverpath):
                                if startoptservername != '':
                                    serverram = input('How much GB/MB of RAM would you like to use (Example 256MB, 1GB, 4GB) (Leave empty for default)?: ')
                                    if 'GB' or 'MB' in serverram or serverram == '':
                                        if 'GB' in serverram:
                                            RAMgb = serverram[0:-2]
                                            RAM = int(RAMgb) * 1024
                                            print('Running Server on ' + RAMgb + 'GB...')
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx' + str(RAM) + 'M -Xms' + str(RAM) + 'M -jar fabric-server-launch.jar nogui')
                                        if 'MB' in serverram:
                                            RAMmb = serverram[0:-2]
                                            RAM = int(RAMmb) * 1
                                            print('Running Server on ' + RAMmb + 'MB...')
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx' + str(RAM) + 'M -Xms' + str(RAM) + 'M -jar fabric-server-launch.jar nogui')
                                        if serverram == '':
                                            print()
                                            print('Enter \"stop\" into Server Console to Stop the Server')
                                            os.system('cd ' + startserverpath + ' && java -Xmx4096M -Xms4096M -jar fabric-server-launch.jar nogui')
                                    else:
                                        print('Value was entered incorrectly, please try again')
                                    print()

                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "modify":
            listfabricversions()
            modifyoptname = input("Choose Version of Your Server (example 1.17.1): ")
            print()
            if os.path.exists('fabricservers\\' + modifyoptname):
                if modifyoptname != '':
                    modifyoptnamebytes = (len(modifyoptname.encode("utf8")))
                    modifynamedir = glob.glob("fabricservers/" + modifyoptname + "/*")
                    if modifynamedir != ([]):
                        for x in modifynamedir:
                            modifynamedirline = 0
                            for x in modifynamedir:
                                modifymversiondirline = modifynamedir[modifynamedirline] + ' '
                                modifymversiondirlinecut = modifyoptnamebytes + 15
                                print(modifymversiondirline[modifymversiondirlinecut:-1])
                                modifynamedirline += 1
                            modifyoptservername = input("Which server do you want to modify?: ")
                            print()
                            modifyserverpath = 'fabricservers\\' + modifyoptname + '\\' + modifyoptservername
                            modifyopt = input(
                                'Do you wish to modify \"properties\", \"mods\" or \"delete\" this server?: ')

                            if modifyopt == 'delete':
                                print()
                                removeservercheck = input(
                                    'Type out \"delete ' + modifyoptservername + '\" to confirm deletion of \"' + modifyoptservername + '\" running on \"' + modifyoptname + '\" version of minecraft: ')
                                if removeservercheck == 'delete ' + modifyoptservername:
                                    print('Deleting Server...')
                                    os.system('rmdir /S ' + modifyserverpath)
                                    if str(glob.glob("fabricservers/" + modifyoptname + "/*")) == '[]':
                                        deletionversionpath = 'fabricservers\\' + modifyoptname
                                        os.system('rmdir /S ' + deletionversionpath)
                                    print('Deletion Completed!')
                                    print()

                            if modifyopt == 'mods':
                                modfolderpath = modifyserverpath + '\\mods'
                                if not os.path.exists(modfolderpath):
                                    os.mkdir(modfolderpath)
                                modsopt = input('Do you wish to \"download\" or \"remove\" mods?: ')
                                print()

                                if modsopt == 'remove':
                                    uncutmodlist = glob.glob(modfolderpath + '/*')
                                    if uncutmodlist == ([]):
                                        print('Mod Folder is Empty')
                                        print()
                                    else:
                                        modlist = []
                                        currentmod = 0
                                        for uncutsinglemod in uncutmodlist:
                                            currentmod += 1
                                            singlemod = (uncutsinglemod + ' ')[len(modfolderpath) + 1:-1]
                                            modlist.append(singlemod)
                                            print(str(currentmod) + ' - ' + singlemod)
                                        print()
                                        modsremoveopt = input('Which mods would you like to remove? (Select numbers of mods you want to remove or type out \"all\" to remove everything, foramt: 1, 3, 8): ')
                                        if modsremoveopt == 'all':
                                            print()
                                            print('Removing ALL Mods...')
                                            os.system('rmdir /S ' + modfolderpath)
                                            print('Removal of ALL Mods Completed!')
                                            print()
                                        else:
                                            numbermodremovelist = []
                                            modremovecommabytesa = 0
                                            modremovecommabytesb = 0
                                            for modremovecommas in modsremoveopt:
                                                if modremovecommas == ',':
                                                    numbermodremovelist.append(
                                                        modsremoveopt[modremovecommabytesa:modremovecommabytesb])
                                                    modremovecommabytesa -= modremovecommabytesa
                                                    modremovecommabytesa += modremovecommabytesb + 2
                                                modremovecommabytesb += 1
                                            numbermodremovelist.append(
                                                modsremoveopt[modremovecommabytesa:len(modsremoveopt)])

                                            modtoremovelist = []
                                            for numbermodtoremove in numbermodremovelist:
                                                try:
                                                    modtoremovelist.append(modlist[int(numbermodtoremove) - 1])
                                                except:
                                                    print(
                                                        'Error: Bad Format or Out of Range, MOD NUMBER: ' + numbermodtoremove)

                                            if str(modtoremovelist) != '[]':
                                                print()
                                                print('Removing Mods...')
                                                for modtoremove in modtoremovelist:
                                                    modremovepath = 'fabricservers/' + modifyoptname + '/' + modifyoptservername + '/mods/' + modtoremove
                                                    print('Removing ' + modtoremove + '...')
                                                    os.remove(modremovepath)
                                                print('Removal of Mods Completed!')
                                            print()

                                if modsopt == 'download':
                                    print(
                                        '(Currently supporting only 9minecraft.net, mc-mod.net, mod-minecraft.net file hosting and direct .jar files)')
                                    modurl = input(
                                        'Please Enter Mod Download Urls (Format for more urls: url1, url2, url3): ')
                                    print()

                                    queuelist = []
                                    queuelistcheck = []
                                    queuelist.append(modfolderpath)
                                    queuelistcheck.append(modfolderpath)
                                    modurllist = []
                                    modurlcommabytesa = 0
                                    modurlcommabytesb = 0
                                    for modurlcommas in modurl:
                                        if modurlcommas == ',':
                                            modurllist.append(modurl[modurlcommabytesa:modurlcommabytesb])
                                            modurlcommabytesa -= modurlcommabytesa
                                            modurlcommabytesa += modurlcommabytesb + 2
                                        modurlcommabytesb += 1
                                    modurllist.append(modurl[modurlcommabytesa:len(modurl)])

                                    maxmodurls = 0
                                    currentmodurl = 0
                                    for maxsinglemodurl in modurllist:
                                        maxmodurls += 1

                                    for singlemodurl in modurllist:
                                        currentmodurl += 1
                                        print('Mods: ' + str(currentmodurl) + '/' + str(maxmodurls))
                                        if (singlemodurl + ' ')[-5:-1] == '.jar':
                                            try:
                                                directjarnamesearchbyte = len(singlemodurl) - 1
                                                for x in singlemodurl:
                                                    if (singlemodurl[directjarnamesearchbyte]) == '/':
                                                        directjarnamebytea = directjarnamesearchbyte
                                                        directjarname = singlemodurl[
                                                                        directjarnamebytea + 1:len(singlemodurl)]
                                                        print('Found ' + directjarname + '!')
                                                        break
                                                    directjarnamesearchbyte -= 1
                                                directjarmoddownloadpath = modfolderpath + '\\' + directjarname
                                                print('Downloading Mod...')
                                                urllib.request.urlretrieve(singlemodurl, directjarmoddownloadpath)
                                                print('Downloading Completed!')
                                                print()
                                            except:
                                                try:
                                                    downloaddirectjar = requests.get(singlemodurl, allow_redirects=True)
                                                    open(directjarmoddownloadpath, 'wb').write(
                                                        downloaddirectjar.content)
                                                    print('Downloading Completed!')
                                                    print()
                                                except:
                                                    if str(downloaddirectjar) == '<Response [403]>':
                                                        print('Error 403: This site won\'t work. URL Number: ' + str(
                                                            currentmodurl))
                                                    else:
                                                        print(
                                                            'Error! Please make sure you entered download url correctly')
                                                        print()
                                        else:
                                            if 'mc-mod.net/' in singlemodurl:
                                                if 'index.php?act=download&id=' in singlemodurl:
                                                    nineminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[
                                                           nineminecraftmodidsearch:nineminecraftmodidsearch + 3] == 'id=':
                                                            nineminecraftmodidbytesa = nineminecraftmodidsearch + 3
                                                        if singlemodurl[nineminecraftmodidsearch] == '&':
                                                            nineminecraftmodidbytesb = nineminecraftmodidsearch
                                                        nineminecraftmodidsearch += 1
                                                    nineminecraftmodid = singlemodurl[
                                                                         nineminecraftmodidbytesa:nineminecraftmodidbytesb]
                                                    if 'https://files.mc-mod.net' in singlemodurl:
                                                        singlemodurl = 'https://download.mc-mod.net/index.php?act=dl&id=' + nineminecraftmodid  # New URL
                                                    elif 'https://download.mc-mod.net' in singlemodurl:
                                                        singlemodurl = 'https://download.mc-mod.net/index.php?act=dl&id=' + nineminecraftmodid  # New URL
                                                try:
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(url='https://download.mc-mod.net/index.php?act=dl&id=')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'File name: ' in modhtmlline:
                                                                    modhtmllinecut = modhtmlline[1:-1]
                                                                    anchorpointposition = 0
                                                                    anchorpointlist = []
                                                                    for anchorpoint in modhtmllinecut:
                                                                        if anchorpoint == '\"':
                                                                            anchorpointlist.append(anchorpointposition)
                                                                        anchorpointposition += 1
                                                                    moddownloadurl = modhtmllinecut[
                                                                                     anchorpointlist[0] + 1:
                                                                                     anchorpointlist[1]]
                                                                    modnamelinesearch = anchorpointlist[2] + 31
                                                                    for nameanchorpoint in modhtmllinecut:
                                                                        if modhtmllinecut[
                                                                           modnamelinesearch:modnamelinesearch + 4] == '.jar':
                                                                            modnameline = modnamelinesearch + 4
                                                                        modnamelinesearch += 1
                                                                    modname = modhtmllinecut[
                                                                              anchorpointlist[2] + 31:modnameline]
                                                                    print('Found ' + modname + '!')
                                                                    break
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath + '\\' + modname
                                                        print('Downloading Mod...')
                                                        urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                        print('Downloading Completed!')
                                                        print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    print('Error! Please make sure you entered download url correctly')
                                                    print()

                                            if 'mod-minecraft.net' in singlemodurl:
                                                if 'download2.php?a=' in singlemodurl:
                                                    modminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[
                                                           modminecraftmodidsearch:modminecraftmodidsearch + 6] == 'php?a=':
                                                            modminecraftmodidbytesa = modminecraftmodidsearch + 6
                                                        if singlemodurl[modminecraftmodidsearch] == '&':
                                                            modminecraftmodidbytesb = modminecraftmodidsearch
                                                        modminecraftmodidsearch += 1
                                                    modminecraftmodid = singlemodurl[
                                                                        modminecraftmodidbytesa:modminecraftmodidbytesb]
                                                    singlemodurl = 'http://dl3.mod-minecraft.net/download.php?file=' + modminecraftmodid  # New URL
                                                try:
                                                    queuecheck = 0
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(url='http://dl3.mod-minecraft.net/download.php?file=')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'You\'re trying to download again too soon!' in modhtmlline:
                                                                    print(
                                                                        'mod-minecraft.net has download limit, url was added to the queue. URL Number: ' + str(
                                                                            currentmodurl))
                                                                    queuecheck = 1
                                                                    queuelist.append(singlemodurl)
                                                                    break
                                                                if '<td align=center class=middle><h1>' in modhtmlline:
                                                                    modnamesearchbytes = 0
                                                                    for x in modhtmlline:
                                                                        if modhtmlline[
                                                                           modnamesearchbytes:modnamesearchbytes + 4] == '.jar':
                                                                            modnamebytesb = modnamesearchbytes + 4
                                                                        modnamesearchbytes += 1
                                                                    modname = modhtmlline[35:modnamebytesb]
                                                                    print('Found ' + modname + '!')
                                                                if 'document.getElementById(\"dl\").innerHTML = \'<a href=\"' in modhtmlline:
                                                                    moddownloadurlsearchbytes = 56
                                                                    for x in modhtmlline:
                                                                        if modhtmlline[moddownloadurlsearchbytes] == '\"':
                                                                            moddownloadurl = modhtmlline[56:moddownloadurlsearchbytes]
                                                                            break
                                                                        moddownloadurlsearchbytes += 1
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath + '\\' + modname
                                                        if queuecheck != 1:
                                                            print('Downloading Mod...')
                                                            urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                            print('Downloading Completed!')
                                                            print()
                                                        else:
                                                            print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    if queuecheck == 1:
                                                        print()
                                                    else:
                                                        print(
                                                            'Error! Please make sure you entered download url correctly')
                                                        print()

                                            if '9minecraft.net/' in singlemodurl:
                                                if 'index.php?act=download&id=' in singlemodurl:
                                                    nineminecraftmodidsearch = 0
                                                    for x in singlemodurl:
                                                        if singlemodurl[
                                                           nineminecraftmodidsearch:nineminecraftmodidsearch + 3] == 'id=':
                                                            nineminecraftmodidbytesa = nineminecraftmodidsearch + 3
                                                        if singlemodurl[nineminecraftmodidsearch] == '&':
                                                            nineminecraftmodidbytesb = nineminecraftmodidsearch
                                                        nineminecraftmodidsearch += 1
                                                    nineminecraftmodid = singlemodurl[
                                                                         nineminecraftmodidbytesa:nineminecraftmodidbytesb]
                                                    if singlemodurl[0:28] != 'https://files.9minecraft.net':
                                                        singlemodurl = singlemodurl[
                                                                       0:29] + '/index.php?act=dl&id=' + nineminecraftmodid  # New URL
                                                    else:
                                                        singlemodurl = 'https://files.9minecraft.net/index.php?act=dl&id=' + nineminecraftmodid  # New URL
                                                try:
                                                    modhtml = requests.get(singlemodurl)
                                                    badmodhtml = requests.get(
                                                        url='https://files.9minecraft.net/index.php?act=dl&id=0')
                                                    if modhtml.text != badmodhtml.text:
                                                        modhtmlbytesa = 0
                                                        modhtmlbytesb = 0
                                                        for x in modhtml.text:
                                                            if x == '\n':
                                                                modhtmlline = modhtml.text[modhtmlbytesa:modhtmlbytesb]
                                                                if 'File name: ' in modhtmlline:
                                                                    modhtmllinecut = modhtmlline[1:-1]
                                                                    anchorpointposition = 0
                                                                    anchorpointlist = []
                                                                    for anchorpoint in modhtmllinecut:
                                                                        if anchorpoint == '\"':
                                                                            anchorpointlist.append(anchorpointposition)
                                                                        anchorpointposition += 1
                                                                    moddownloadurl = modhtmllinecut[
                                                                                     anchorpointlist[0] + 1:
                                                                                     anchorpointlist[1]]
                                                                    modnamelinesearch = anchorpointlist[2] + 31
                                                                    for nameanchorpoint in modhtmllinecut:
                                                                        if modhtmllinecut[
                                                                           modnamelinesearch:modnamelinesearch + 4] == '.jar':
                                                                            modnameline = modnamelinesearch + 4
                                                                        modnamelinesearch += 1
                                                                    modname = modhtmllinecut[
                                                                              anchorpointlist[2] + 31:modnameline]
                                                                    print('Found ' + modname + '!')
                                                                    break
                                                                modhtmlbytesa -= modhtmlbytesa
                                                                modhtmlbytesa += modhtmlbytesb
                                                            modhtmlbytesb += 1
                                                        moddownloadpath = modfolderpath + '\\' + modname
                                                        print('Downloading Mod...')
                                                        urllib.request.urlretrieve(moddownloadurl, moddownloadpath)
                                                        print('Downloading Completed!')
                                                        print()
                                                    else:
                                                        print('Error! Download Page Empty')
                                                        print()
                                                except:
                                                    print('Error! Please make sure you entered download url correctly')
                                                    print()

                                    open(file='download-queue.txt', mode='w+', encoding='utf-8')
                                    wqueue = open(file='download-queue.txt', mode='w', encoding='utf-8')
                                    for singlequeuelink in queuelist:
                                        wqueue.write(singlequeuelink + '\n')
                                    wqueue.close()
                                    if str(queuelist) != str(queuelistcheck):
                                        writequeue()
                                        os.system('start cmd /k python mod-download-queue.py && exit')

                            if modifyopt == 'properties':
                                propertiespath = modifyserverpath + '\\server.properties'
                                if os.path.exists(modifyserverpath):
                                    if modifyoptservername != '':
                                        try:
                                            if not os.path.exists(propertiespath):
                                                with open(os.path.join(os.path.dirname(__file__), propertiespath),
                                                          'a+') as createserverproperties:
                                                    print('Creating Properties File...')
                                                    createserverproperties.close()
                                                    with open(os.path.join(os.path.dirname(__file__), propertiespath), 'w') as wserverproperties:
                                                        wserverproperties.write('enable-jmx-monitoring=false\nlevel-seed=\nrcon.port=25575\ngamemode=survival\nenable-command-block=false\nenable-query=false\ngenerator-settings=\nlevel-name=world\nmotd=A Minecraft Server\nquery.port=25565\npvp=true\ngenerate-structures=true\ndifficulty=easy\nnetwork-compression-threshold=256\nmax-tick-time=60000\nrequire-resource-pack=false\nuse-native-transport=true\nmax-players=20\nonline-mode=true\nenable-status=true\nallow-flight=false\nbroadcast-rcon-to-ops=true\nview-distance=10\nmax-build-height=256\nserver-ip=\nresource-pack-prompt=\nallow-nether=true\nserver-port=25565\nenable-rcon=false\nsync-chunk-writes=true\nop-permission-level=4\nprevent-proxy-connections=false\nresource-pack=\nentity-broadcast-range-percentage=100\nrcon.password=\nplayer-idle-timeout=0\nforce-gamemode=false\nrate-limit=0\nhardcore=false\nwhite-list=false\nbroadcast-console-to-ops=true\nspawn-npcs=true\nspawn-animals=true\nsnooper-enabled=true\nfunction-permission-level=2\nlevel-type=default\ntext-filtering-config=\nspawn-monsters=true\nenforce-whitelist=false\nresource-pack-sha1=\nspawn-protection=16\nmax-world-size=29999984')
                                                        wserverproperties.close()
                                            with open(os.path.join(os.path.dirname(__file__), propertiespath), 'r+') as rserverproperties:
                                                rproperties = rserverproperties.readlines()
                                                rserverproperties.close()
                                        except:
                                            print()
                                            print('Error: No such file or directory')
                                            exit()
                                        propertiesline = -1
                                        maxpropertiesline = 0
                                        modifiedproperties = []
                                        print()
                                        for x in rproperties:
                                            maxpropertiesline += 1
                                        for x in rproperties:
                                            propertiesline += 1
                                            modifyline = rproperties[propertiesline][0:-1]
                                            if '#' not in modifyline:
                                                print('Line: ' + str(propertiesline + 1) + '/' + str(maxpropertiesline))
                                                print(modifyline)
                                                modifyinput = input(
                                                    'Do you wish to edit this line if not leave this field empty? (If you want to make field empty type \"empty\"): ')
                                                print()
                                                if modifyinput == '':
                                                    modifiedproperties.append(modifyline)
                                                else:
                                                    if modifyinput == 'empty':
                                                        modifyinput = ''
                                                    searchmodifyline = 0
                                                    for x in modifyline:
                                                        if modifyline[searchmodifyline] == '=':
                                                            bmodifyline = (modifyline[0:searchmodifyline + 1])
                                                            modifiedproperties.append(bmodifyline + modifyinput)
                                                        searchmodifyline += 1
                                        with open(os.path.join(os.path.dirname(__file__), propertiespath),
                                                  'w') as wproperty:
                                            for modifiedpropertiesline in modifiedproperties:
                                                wproperty.write(modifiedpropertiesline + "\n")
                                            wproperty.close()
                                        print('All settings were saved')
                                        print()
                    else:
                        print('Version Doesn\'t Exist or is empty')

        if scoption == "create":
            imkversion = input("What version of server do you want to create? (example 1.17.1) (Oldest Supported Version is 1.14): ")
            fabricinstallerurl = 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.8.3/fabric-installer-0.8.3.jar'
            mkversion = 'fabricservers\\' + imkversion
            if not os.path.exists(mkversion):
                os.mkdir(mkversion)
            servername = input("Name your Server: ")
            mkversionname = mkversion + '\\' + servername
            if not os.path.exists(mkversionname):
                os.mkdir(mkversionname)
                fabricinstallerloc = mkversionname + '\\fabric-installer-0.8.3.jar'
                print('Downloading Server...')
                urllib.request.urlretrieve(fabricinstallerurl, fabricinstallerloc)
                print('Downloading Completed!')
                print()
                print('Installing Server...')
                os.system('cd '+mkversionname+' && java -jar fabric-installer-0.8.3.jar server -mcversion '+imkversion+' -downloadMinecraft')
                print()
                print('Server Installation Complete!')
                print('Deleting Installer and Waste..')
                os.system('cd '+mkversionname+' && del fabric-installer-0.8.3.jar && rmdir /S .fabric-installer')
                cpropertiespath = mkversionname + '\\server.properties'
                eulapath = mkversionname + '\\eula.txt'
                with open(os.path.join(os.path.dirname(__file__), eulapath), 'w+') as eulainput_file:
                    weula = eulainput_file.write('eula=true')
                    eulainput_file.close()
                with open(os.path.join(os.path.dirname(__file__), cpropertiespath), 'w+') as cwserverproperties:
                    cwserverproperties.write('enable-jmx-monitoring=false\nlevel-seed=\nrcon.port=25575\ngamemode=survival\nenable-command-block=false\nenable-query=false\ngenerator-settings=\nlevel-name=world\nmotd=A Minecraft Server\nquery.port=25565\npvp=true\ngenerate-structures=true\ndifficulty=easy\nnetwork-compression-threshold=256\nmax-tick-time=60000\nrequire-resource-pack=false\nuse-native-transport=true\nmax-players=20\nonline-mode=true\nenable-status=true\nallow-flight=false\nbroadcast-rcon-to-ops=true\nview-distance=10\nmax-build-height=256\nserver-ip=\nresource-pack-prompt=\nallow-nether=true\nserver-port=25565\nenable-rcon=false\nsync-chunk-writes=true\nop-permission-level=4\nprevent-proxy-connections=false\nresource-pack=\nentity-broadcast-range-percentage=100\nrcon.password=\nplayer-idle-timeout=0\nforce-gamemode=false\nrate-limit=0\nhardcore=false\nwhite-list=false\nbroadcast-console-to-ops=true\nspawn-npcs=true\nspawn-animals=true\nsnooper-enabled=true\nfunction-permission-level=2\nlevel-type=default\ntext-filtering-config=\nspawn-monsters=true\nenforce-whitelist=false\nresource-pack-sha1=\nspawn-protection=16\nmax-world-size=29999984')
                    cwserverproperties.close()
                print('DONE!')
                print()
            else:
                print('Error: Name Already Exists')
