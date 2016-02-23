#!/usr/bin/env python
# -*- coding: utf-8 -*-         
import sys
import os
print """
 ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓ ▒█████  ▒███████▒ █    ██  ███▄    █  ▄▄▄      
▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒▒ ▒ ▒ ▄▀░ ██  ▓██▒ ██ ▀█   █ ▒████▄    
▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒░ ▒ ▄▀▒░ ▓██  ▒██░▓██  ▀█ ██▒▒██  ▀█▄  
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░  ▄▀▒   ░▓▓█  ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░▒███████▒▒▒█████▓ ▒██░   ▓██░ ▓█   ▓██▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░      ░ ▒ ▒░ ░░▒ ▒ ░ ▒░░▒░ ░ ░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
░          ░░   ░  ▒ ░░░         ░      ░ ░ ░ ▒  ░ ░ ░ ░ ░ ░░░ ░ ░    ░   ░ ░   ░   ▒   
░ ░         ░      ░                        ░ ░    ░ ░       ░              ░       ░  ░
░                                                ░                                      
"""
print """
                   #\   /##/      #
                    #   #/       #/
     ####\    /##\  #\__\#\     #/         /#
       \##\  /#  #\  ######|    #     /####/
         |#\_|___##| |#####|__ #/ _/######/
         \#########|_|##################/
           \###########/     \########/
            \#########|        \###|
        \##\ \########/   @@   |###| ___/#####
           #\ \######|    @@   |#########
            #\ //   \|         ||
            \##|     \\____ ####| /########
      _____  \#|_@@__|#####/....\##/ \#/  \#
     #######\ /######MMM#/ ......|#        \#
          /###/......\M/ ...... .\#######
         |#| .........|...........|###\
      ___|#|..........|......  .../| \##
     ########.. ......\........./##|   \#
         |#|.........../\.._____|##|     \##
         |##\  ...__.--|---#########
        /####\___/##/--|--|#######/ #
       /#    \######|-----|#/ \#    \##
     ##/     /|######\---/#/          \#             criptozuna v1.0
            ##/ |#########/            \#            author: oppaozuna@gmail.com
               /########|               \##______________________________________
              /#########|
             ## |#######|
                |#########\
                 |########|
                 |#########\
 VK              |##########\
                 |############\
"""
#\xc3\xb1
diccionario = {
'a':'yrfvYTFVTYBGNuhjhfvhtdTGBHBGh5445646756$%$%$&%65456676875765879807987856455233123254679878756647656456545645453453445ertdgfdcffdcfCFDDCDTD',
'b':'tdcrtdvFBYNFYTFDCRecsvfbtfcrCRCVDTBYNGYVDXESEXscrdvfbybnuhugnimjijnhBYUFREe6556453423124335676564542432568768744532546764%$#$"%65454434333',
'c':'tdthvdYTBFHGHRTDtrhvfbygnuihyfttrdrdcrvftbygntyfcrdtrvfbyngbyvfctdvtyfbgyugYFTFCTRDCRSXSEDRFVTYBGUNHUhyfctdvtbgyhbgtdcrxesxwexecrdrvtdvrtt',
'd':'esxefsECDTVTYFVYFBYgynut645343"#$"#$"$#$%&%/&(/&(/&%&%$%$%/&/&%&%$&%$%/&%$%/&%/&$&%$&%&$%$&%&%$&%/54654654&$/&$&%$#&%$/&$&%$#&%$&%#6545645',
'e':'nvftgdhftdVHTFVGHFBVUHNIUHM;IJUGTRDXWAQWZAwsercdrdvftygbuhni654534257&%&$%$#%$#%$$/&())/)(/(&/%$$#W$#eeertdfgdfgw4334567657564656779879095',
'f':'tvfhtyfUYTFUYTBFYUNGUIHMIJugbvtfdcrtxsexwESECCDRVFBYGNHUIHUI656443243#%$&/%/&)(/(/%&%#$"#"$%$%/&(/TgfdgfdcrgdtrVDRRECDRVTfy564654654564555',
'g':'rhdcrtvftyFJTYFtvhyfvfTHFytFHtde$354$&5755645342456576786986745342324356676879869878967556453424323213242544tyvdtredscgfdvgfbghfgcdcrsxsds',
'h':'jyftfvthyDTRDCRTCDVftbytfvtdrcdvtbgnuhuhungvtdcexdxsesdrtfbgunhntdxescrvfbynhuhyfdxdwaserdfvtybgunhufdsRVFYBFTVSXEAXESCDRVFTBGYGTSXWXAXWEE',
'i':'jyfgftyfvytFVTYFBYUGYdresewawexsERVFYHNIJMO;KPOKOMJNIUbyugfvtyfbyhnjO;KOjminuguyHIgtseasrefgbyunhyUDRESXEDFYBUGtyexedsrecdfvytbgtdrcsrdrdr',
'j':'tdcrtvdfBYUHNGYftfgy543678978674535656878tytGNHFTDCVFBYFTVDTTVFBGNgtdctrvfbygyunuijmikmjnudxeazwAWXSDFDVTGFrdrVFTBGYHBGTFTFTtfgbduhnufdcdd',
'k':'ytedcrDVTFbuyfTrDCRTFgbuyHGtr$%#5646543542564764543245765876986987897079867656534324545786986876454334243235476565343234245365764654675877',
'l':'catrecyrTDVTFBgiuynMIyufRCTDrtvfbgyunhmioufctrfdrcfdRTVFBGYNUHMrcdcrSEXSESCERDVRTBYHNHGYBGDEXewsrfgujjikgvfsr656757667%$%#$$%#Wrdvtrgdxesx',
'm':'trscGRDVYTBGNUkuijmojiuhbyuftvfgyufrewswawSCRTFVGYUNJMJYDXDFYNHFWCTTUIGVTFYUYHNUITTTUIYHUYFDABYBGVTDGVFBYUDGXBBFGygbxhtegUITGEvybtGUIBGt32',
'n':'cctdcrrdvTYBGNUYHFTRDrtfgbhbvfgdcrff354467%&/%$%"#$$$%&(&&%##$"#$345567687543567t87979079798(=)ttdfsxeaxscfdvtgfbrszwqzwAERDVFTBFTSEWdsrtf',
'ñ':'cxrscdtvfbgnujhgfdrFDVTYBGHUMJIGtr543465568754325448797987544523446776$$%#&/65332544576&%#$#"$##$&7tvfdxescfvbgdcdsxxcvgfgvdssstdvttrdwqwa',
'\xc3\xb1':'cxrscdtvfbgnujhgfdrFDVTYBGHUMJIGtr543465568754325448797987544523446776$$%#&/65332544576&%#$#"$##$&7tvfdxescfvbgdcdsxxcvgfgvdssstdvttrdwqwa',
'o':'frfrfdVTYFtftrerdfgbyunjhnR%$&/&/%$##$"$##&%/&5653542342432345456768776542343456785453465564565876r654345643423453423234231232345687tr543e',
'p':'rtcdvthfbgnkuJHUYFXRDScrvfgbunhuhfrtcdvtyuhjiok,ok,jygdcreswexascedvftbygnhunygdxdVFYFRTdcrtvGFBynUBbtyfbuynhmuigvcdexswxaxecdvtbgnyhyhgtv',
'q':'dvdvtygbuyhGYTDCTRFVYHBHUJKHIUKHYR%$&%/&&/$##"#!#$&//(/&%%$#%#$%$$%#%$"#"#$"$#"#$#$""#"WERCDVTGFCFGSXEDCDTVGBGHNHGDXEDXSXCFVDFBFVFGDFCFVFV',
'r':'rcdgrdesewazwawesdrtfgyuhnimjk,oppkmojnubgvytvdrctcdxresrfsew3$#"$2434657678898787554w332qwxescfdvbghnfdewzweewszwazWXSRCFDVGRFSREXSCRTVFt',
's':'hfhfvgfdhvgvfTE$%3446567465456487&(%%$3567656535465687665787986989867654343234ETYVDGCDVTGFytvfvbftrresxwescdfvbgytdewsrefcdtvfvydxesrecrrd',
't':'jtdvhtrfdTYFTYBGGJYT6545435465456437564%ECRTDYTRVDUTFBUYTFUYVTVYTRDytrdvtyt56354354578687687656536558765653435666534325tvftrdescrcrcresexr',
'u':'TYDTRDhvbjhnhjnut6545465788768786/%&%#$%W$%Rfbggcrsxesrerdeazqwqawewscrdvfbyhinjl.{k,okpok,ojihniugbuyfvtdrsxxewazwawesedvtfyhgnujhmjkkhby',
'v':'ioungyfTYBFGYUHGYffgyubhgnujhUGTDEWAWESRTFGUHMIJOINUGYTVdrceddrvttfbgynhmuhugtvydrccdcrcdvrftbgygnynygbyfrswawawzxdfctbgbynuhmijijimjimjij',
'w':'e4354365$&%/&%76687687698708987987987756443312121234567768778u6ttyDCRFDVGFBGDDDSEcsrSXedscdvtbfytfSXWAQaawaserdftbynhhYFRDRDTDCRrdvtfdrfdr',
'x':'4536745867465$/%$&$%#453435657876897908098980998798678556564523446565456$&$%454657868765tfbghbfdcvdbygnujhmhgvtdxeazawaxwcsrvfbygnuuhuhunh',
'y':'ehtvfhgdcrRTVFBYUGFR324334675654543467563564356890785433699868T/&/%&/rtyutvdfcdvybhnhfrwsxeCDTVBGNHFCXRXWSCRVTFBGBDWEXWSCRVBYBHGVTCDRDRFDr',
'z':'eeh5436546576785&%#$"45457878654322456789098765432456756546VTDCGFDVBHffcdvfFVVFVFFbhgnhfcfv54565432143657657656543234576544532425434534444',
' ':'fahRCDVHTFBJYUGnukgYUFBFYnUINbyFVTFbyugNYUbgvTYFTBYUGNUHIHJMI,OKOijhbyfr342$%%&/8766465354223134565876968678563424323425434545354335424323',
'1':'hgvff435647657/&%/&%/&tubgjhvfvTHTYFBJHGjgvftfgfgfv$&%$vfytfvjgfbjYffujytFRVUTFRV576576VJGFvjhgfvJHGfjbgbfvdfDCFGDChgdfCGFDchgfdcgfdcgfdff',
'2':'htgjhgbjhgvfjhfgfjvgfjhfggvfhgfvhbfvhgfhcgfdhgfvjhGFHYgfvhEXesFdcjHVGFvhfdg#$#%$&%$6654&%$&%$765764654%EcfdxGFDXgdSXGFDSXgdSGXDSXGFDSxXFDS',
'3':'htgvvdvhfgdhgfdhgtHYTDCYTDTRdctDVtydYTvdTYdTrdTd5465465$&%$&%$/6765/&%/&%/&$/&$65ytcfdcGFD!#$)====jbhfvDddXcgfdxAZZwzaxfgcCDTRvtvvtTTt555%',
'4':'hfvtfV%$#%$&4654654&%$&%$fvyhtchVTFujytfvJYTR546VhytfhtyVTYFJUY46pokplñkmouwqwxescfvBHNmiokjhvyyfbUNINH bgyvf56465bJHGFCSXCrdvfbygfJYTTdcd',
'5':'crdetrDTVRHDhtfhytgFV321243&%/&)(/)()(/=)(=)(TYVhythCTDtrdhTRD213243%$#546%$56354356465453542432309879798687CGDGFdcgfdxcfdgfDCGDxcfdsXGFcd',
'6':'tvdhTDCHTDTHVDhgtvT23424%465$/&%&5765765675/&%/&%67565656565780897354132&/&9875%$&"#%786875765/&$%&$%$%$%$#RecgdcgfdGCdgfDCGfdGCdCGfdXFDsd',
'7':'ghdcrswzwEWEXSFXDSXFDSFDSERSXFDSEXSXFESFESX34535435435435434243546546$&%$&%$&%6545$#%#%$#$%rdecDEWXDSR34354)/(/(76876786876766576666666666',
'8':'fgsxsdEXSGCRdsgD32654786589)(&%&&#"54758769()=867453452#"$56vFDCdvhgbgdcffsxcdvGHDCfdddvhbhgbdxedscfddaxwcsdvgffdcfdvfdfgvcdfcfvfbhnghcrfv',
'9':'sxfexesERSCRDGDrgdcgfdvfdcfDdcffvg34244564$%#$%#%$%cerecrdctfbhh()/()/&87thgdcfdcfdvFFXXRCVFYVFXSXXDZWQXdvgvfbhbgbhghvgdfvygdtvdrfdfbgnupo',
'0':'htcdtrxeRCDVfybfhrtdvfbyFRdvtybgnhimhYFDRTTVFGBHNIUHYD$Wvfyfvtdctvfdrdtre$#&%/&&/&(/=)()&/&%/&$WCVTFcfcrdvGVcdcdtvGBfvcrxeqqDVYfteRXcdtvtt',
'.':'gdcgfdCRDVbtNUygTVdfvtbgnut7678967866576tBFCRTXECDVTGFBgnhunhyufvt4345&%/&/%%$%#%$#&(/)()00==98tvgdbfdcVFgdCRDRsxQ""#"#%$&%vfdVfcdvbgvvdfv',
'-':'tfvvhthgdcrcdc%$%%$%TrvftgfyhbgNUKJHKfcvfbgnhluGDCRSCTVBGNHUFVFTg6786/%tfghbgknGHGCDVBFGNHfvfcdvgbgbjnhNHU(//&&/$$%#$%#&TGVGFDXDScfdcdsfdd',
'_':'trhdcRVFbggnuhFtvgfgrsEWASrvfbgnMKJhfdFVnuhbvdfbynhUFTRuloipoiuiouṕo{kbnhmlkol{lkjugbtdfvbuNHHFvbhnkhhjfvCDCVHbgvdTghT&578676&&bhjhfrcredy',
',':'gchrcdgredsxESCDRfdxeDSDTvfbGNuimjIYGDFVBUJUFRFGUIHNUGBGNKJGYffbyftyfbygnuijmokpl.pl.pl,k.op,o.ko,kokiohnugtewsx3wxecdrtfgbungtvvftgfvtbtf',
'!':'trd4t#%$#%$&$56467886457564756$%$76546754%6475$765876587(%&$564343$36544685876545#$%#$%45645$#$#%&()))==))=)(&%##$"#"#%$#%$#%$#32111#$"34#',
'#':'%&$%#%#$DCGSRCdvtfbyhGUFTFV56%/%/&%/&%$%#$#"#"$%%/()UITFDSXCFVFBHGNUNGBVFDCVBGNHHNBGDXAWEXSDTYHGBUHGYGFCDVYBNHMUKHNBYDCVFBYHGRSCRGVFVTDTTT',
'$':'grwxwAEWCTEytrDVTfbngnhmuiji;O;JKPOKMNHyf%#&%(/&$%64(&)66%&76#$"4334%76/%78587654%#$"$#"%$/&%/&$&%$%(%&%)()/)(/&%$%$"#"#$%&//&%E$TVGFDCCCc',
'%':'fezewxaESCDvtfbygnugbthDFTVFGUNHMIGTDXWAZWAWXEDFTYGBHNIKMJKVSR655634565(/(/&&%&%%$#$"#$%&/(/TFGUJHGHFGDFGHJKFDRTYYUIJHGFDRTYUIRTYUJplollll',
'&':'tyeytry2t542543654765$&$%$$&/%/)(/=)/()/=/)/)(&76575654532341435646576665765786348518324762513765vhfvghdcfTDCHVFBGFBhggvggfhgfvhgfbghvfvfg',
'/':'qzdwsaxeesddcfvGBGHBHNJNHG334354657679879====)9iunujhvfDCRSESRTFygOIHPIJKJhgftrr"$#&%/&%&$$%$/(6765534425432434535443243234435435435434344',
'(':'sxectrDVUTYFBYUNGKUIHuhufrerexstrdytfgyuhuijhiuyyr$#%$%/&&()/)()I=())(=))(()?=???==(=)()/(%&%$%"543465456342544656535434654654654653423wrt',
')':'edcesxEXERTFBYNUNHNTdtftvgfe32432354658768787097987676542431323#W$%RTCCFDCVGFGFVDCGDVGHazexscfdvgfTDCRFDVFBEDRTCDTVYFTFXESCRVDTBYGIUJPOKHK',
'=':'fxeawaxeAWEWXESECRDTVYFTR5646557876878709ytdvbhgfffsewawxsdtghgbujhJHMKJBUYFTVFTDSDFYUHIKJHGR"!#"%/&565465345354#%$/&%(/&/&%/%&$%#$"$#"$##',
'?':'GFDCFDvgfdfgdcxescerDTFBGUHGDXEXWEAXERDFTVGTCDRTGFBGHGTDETTHGFtbtdrserdvfyhgvdcrfyunjmiokkhfdcrswaeeT$&%$/&&)(&7445342454658768765675/&%66',
'¡':'ewxweaecdvrtfbuyugniuhnunGTYDFVTYBGNHUIHMYDEAXSECDVFTBYGNHUNHNNNFTVGBUgvvftfgyuhgvte557868756545653423423343r676875564576564564564654e4454',
'¿':'eraarzweaxwESECRTdft4655786876$&%#$"$%%/(&/)(U/)=(?))(/&&%$"43547654343123235487785345456531233145789880986t654565876876442313243543564565',
'@':'xwqZWAXECDRTVFBYHNHIKJMOP,KPḰIOYGTWW13564798//&&%$%#$"455T78UTGEFEDFVYBGNUIMHGESWEASRTFGBUNIJKO,PL.Ñ{+{++-.+L.ṔLPKIHNUFCRsecrdvfybuGHNIOMK'}

#argumento=sys.argv[1]
textoleet=''
if len(sys.argv)==3:
	if sys.argv[1]=='--cifra':
		cifrado=open(sys.argv[2]+'.cifra','w')
		arch=open(sys.argv[2],"r")
		while True:
			line=arch.readline()
			if not line:break
			for v in line:
				if v in diccionario.keys():
					textoleet += diccionario[v]
				else:
					textoleet += v
			print textoleet
			cifrado.write(textoleet)
		arch.close()
		os.remove(sys.argv[2])
			#print line



		print "cifrado %s" %(sys.argv[2])
	elif sys.argv[1]=='--descifra':
		descifrado=open(sys.argv[2].strip(".cifra"),'w')
		print "descifrando %s" %(sys.argv[2])
		arch=open(sys.argv[2],"r")
		while True:
			line=arch.readline()
			if not line:break
			inicio= 0
			final = 138
			while inicio < len(line) :
				v=line[inicio:final]
				inicio+=2
				final+=2
				for g,w in diccionario.items():
					if w == v:
						textoleet+= g
					#descifrado.write(g)
		print(textoleet)
		descifrado.write(textoleet)
		
		arch.close()
		descifrado.close()
		os.remove(sys.argv[2])
else:
	print "Sintaxis:\ncriptozuna <options> <file>\noptions:\n     --cifra\n     --descifra"
#print argumento
