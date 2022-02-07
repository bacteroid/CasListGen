# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:24:41 2022
@author: Hsi-Chun, Kung (@mercteria)

## CasListGen
A quick podcast playlist site (with player) generator.

## Source Structure
Source
└─Episode1 (Folder)
│ └─episode.m4a
│ └─info.txt
└─Episode2 (Folder)
│ └─episode.m4a
│ └─info.txt
...

## Naming Rule
 - Your folder name will be the name for each episode.
 - Media file should be named "episode".
 - Text file "info.txt" is not necessary, but will become the content note for your episode if existed.

"""

import os
import sys
import urllib
import urllib.parse
import configparser
import shutil
import base64

## Basic information
baset = {
    "title":"",
    "source":"",
    "cover":"",
    "logo":"",
    "ext":"",
    "icon" : '''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'''
}

## Set Configuration File
config = configparser.ConfigParser()
configpat = "CastConfig.ini"

## Check Configuration File
if os.path.isfile(configpat):
    config.read(configpat)
else:
    config['SET'] = {
        "title" : "Your Cast Title",
        "cover" : "Cast Cover",
        "logo" : "Cast Logo",
        "source" : "Cast Source Path",
        "ext" : "Extension of Media File"
    }
    with open(configpat, 'w') as configfile:
        config.write(configfile)
    print("Config Generated !")
    sys.exit()

## Set Variables
baset["title"] = config['SET']['title']
baset["source"] = config['SET']['source']
baset["cover"] = config['SET']['cover']
baset["logo"] = config['SET']['logo']
baset["ext"] = config['SET']['ext']
listdir = os.listdir(baset["source"])

## Default Icon / Cover Generator for Your Cast.
def genicon(fnam,baset=baset):
    imgdata = base64.b64decode(baset["icon"])
    filename = fnam
    with open(filename, 'wb') as f:
        f.write(imgdata)

## Check Resource Folder
if not os.path.exists("resource"):
    os.makedirs("resource")

## Check Logo
logpat = os.path.join("resource",baset["logo"])
if not os.path.isfile(logpat):
    try:
        shutil.move(baset["logo"],logpat)
    except:
        baset["logo"] = "logo.png"
        genicon(baset["logo"])
        shutil.move(baset["logo"],logpat)
        print("Cannot read Logo file.")

## Check Cover
covpat = os.path.join("resource",baset["cover"])
if not os.path.isfile(covpat):
    try:
        shutil.move(baset["cover"],covpat)
    except:
        baset["cover"] = "cover.png"
        genicon(baset["cover"])
        shutil.move(baset["cover"],covpat)
        print("Cannot read Cover file.")

## Page Template
head = '''
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<link rel="apple-touch-icon" href="./resource/'''+baset["logo"]+'''">
	<link rel="Shortcut Icon" type="image/x-icon" href="./resource/'''+baset["logo"]+'''">
	<title>CastList</title>
	<link rel="stylesheet" type="text/css" href="./resource/style.css">
    <script>
    // Open Modal 
    function opnmoda(modid){
        document.getElementById(modid).style.display = "block";
        document.getElementById(modid+"_opnctn").value = "X";
        document.getElementById(modid+"_opnctn").setAttribute('onclick', "javascript:clomoda(\'"+modid+"\');");
    }
    // Close Modal
    function clomoda(modid) {
        document.getElementById(modid).style.display = "none";
        document.getElementById(modid+"_opnctn").value = "☰";
        document.getElementById(modid+"_opnctn").setAttribute('onclick', "javascript:opnmoda(\'"+modid+"\');");
    }
    </SCRIPT>
</head>
<body>
<table class="midtable">
<tr><td>
<center>
<br><br>
<span class="bigtitle">'''+baset["title"]+'''</span>
<br><br>
'''

foot = '''
<div class="pill">
<table width="100%" style="text-align:left; vertical-align:middle;">
<tr><td width="20%">
<img src="./resource/'''+baset["logo"]+'''" class="qrcod" style="height:8vmin; border-radius:10px;">
</td><td width="5%">
</td><td width="75%">
<strong>'''+baset["title"]+'''</strong>
</td></tr>
</table>
</div>
<br><br>
<strong><span class="tag">Generated with CasListGen<br>by<br></span><a class="tag" href="https://twitter.com/mercteria">@mercteria</a></strong>
<br><br>
</td></tr>
</table>
</body>
'''

## Generate card for each episode
def gencrd(title,idn,baset=baset):
    urltit = urllib.parse.quote(title,safe=";/?:@&=+$,",encoding="utf-8")
    try:
        info = ""
        with open(os.path.join(baset['source'],title,"info.txt"),"r",encoding="utf8") as file:
            lines = file.readlines()
            for line in lines:
                info+=line+"<br>"
        file.close()
    except:
        info = "No Content"
    
    url = '''./player.html?ep='''+urltit
    idcnt = idn+"_cnt"
    res = '''
    <div id="'''+idn+'''" style="display:None;max-width:250px;">
    <div class="neumorphismcrd boxfdin" style="height:calc(90px + 1vmin);">
    <div class="incrd">
    <table class="intable" style="vertical-align:middle;width:95%;">
    <tr><td width="5%" style="text-align:center;">
    <img src="./resource/'''+baset["cover"]+'''" class="qrcod" style="height:calc(90px + 1vmin); border-radius:10px;">
    </td><td width="10%">
    </td><td width="85%" style="text-align:left;">
    <span class="castitle">'''+title+'''</span>
    <br>
    <input id="'''+idcnt+'''_opnctn" type="button" style="width:'30%';" class="pill" onclick="javascript:opnmoda(\''''+idcnt+'''\');" value = "☰">
    <input type="button" style="width:'70%';" class="pill" onclick="window.location.href=\''''+url+'''\'" value = "➤">
    </td></tr>
    </table>
    </div>
    </div>
    <br>
    
    <div id="'''+idcnt+'''" class="neumorphismcrd boxfdin" style="display:None;height:250px;">
    <br><hr><br>
    <div class="modal-content"><span class="castinfo">'''+info+'''</span></div>
    <br><hr><br>
    </div>
    <br>
    </div>
    '''
    return res

## Player template
playerpag = '''
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<link rel="apple-touch-icon" href="./resource/'''+baset["logo"]+'''">
	<link rel="Shortcut Icon" type="image/x-icon" href="./resource/'''+baset["logo"]+'''">
	<title>CastList</title>
	<link rel="stylesheet" type="text/css" href="./resource/style.css">
	<script type="text/javascript">
		function no(){
			var urlinput = location.search;
			var params = new URLSearchParams(urlinput);
			var epnm = params.get("ep");
			if(epnm !== null){
				epnm = decodeURIComponent(epnm)
				sourl = './episode/'+epnm+'/episode.m4a'
				document.getElementById("epnm").innerHTML = epnm;
				document.getElementById("player").setAttribute('src', sourl);
				document.getElementById("sourf").setAttribute('href', sourl);
			}else{
				document.getElementById("epnm").innerHTML = "Untitled";
			};
		}
	</script>
</head>
<body onload="no();">
<table class="midtable"><tr><td>

<center>
<br><br>
<span class="bigtitle">CastPlayer</span>
<br><br>

<div class="neumorphismcrd boxfdin" style="max-width:85%;">
<div class="incrd">
<br>
<table class="intable" style="vertical-align:middle;width:90%;">
<tr><td width="4%" style="text-align:center;">
<img src="./resource/'''+baset["cover"]+'''" class="qrcod" style="height:calc(100px + 1vmin); border-radius:10px;">
</td><td width="6%">
</td><td width="90%" style="text-align:left;">
<span class="castitle" id="epnm">Untitled</span><br><br>
<audio controls preload="none" id="player" style="width:100%;border-radius:10px;">
<source src="path-to-m4a.m4a" type="audio/mp4"/>
<p>Your browser does not support HTML5 audio.</p>
</audio>
<br><br>
<p><a href="path-to-m4a.m4a" class="pill" id="sourf" download>Source</a></p>
</td>
</td></tr>
</table>
<br>
</div>
</div>
<br>

<a style="display:block" href="javascript:history.back()">
<div class="pill">
<table width="100%" style="text-align:left; vertical-align:middle;">
<tr><td width="20%">
<img src="./resource/'''+baset["logo"]+'''" class="qrcod" style="height:8vmin; border-radius:10px;">
</td><td width="5%">
</td><td width="75%">
<strong>'''+baset["title"]+'''&nbsp;↩</strong>
</td>
</td></tr>
</table>
</div>
</a>
<br>
<strong><span class="tag">Generated with CasListGen<br>by<br></span><a class="tag" href="https://twitter.com/mercteria">@mercteria</a></strong>
<br><br>
</center>
</td></tr></table>
</body>
'''

## CSS Template
style = '''
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: calc(12px + 1vmin);
}

body {
  font-family: sans-serif;
  background-size:cover;
  margin:0;
  padding:0;
  -moz-background-size:cover;
  background:cover;
}

.bigtitle{
	font-family: "Cursive", "Lucida Handwriting";
	font-size:calc(15px + 5vmin);
	font-weight: bold;
}

.castitle{
	font-weight: bold;
    font-size:calc(12px + 1vmin);
	text-decoration:none;
}

.castinfo{
    font-size:calc(10px + 2vmin);  
}

.tag{
    font-size:calc(5px + 1vmin);
    text-decoration:none;
}

.midtable{
    height:100%;
    width:100%;
    position: absolute;
    top: 0; 
    bottom: 0; 
    left: 0; 
    right: 0;
}

.midtable td{
    text-align: center; 
    vertical-align: middle;
}

.pill {
  background-color: #ddd;
  border: none;
  color: black;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 2px 1px;
  cursor: pointer;
  border-radius: 16px;
}

.qrcod {
	border-radius: 20px;
	box-shadow:  7px 7px 16px #d0d0d0,
             -7px -7px 16px #f0f0f0;
}

.incrd{
    width:100%;
    height:100%;
    overflow-x:hidden;
    display: table;
    display: table-cell;
    vertical-align: middle;
    text-align:center;
    font-size: 5vmin;
}

.neumorphismcrd{
    overflow:hidden;
    vertical-align: middle;
    text-align:center;
    display: table;
    width:80%;
    max-width:30%;
    min-width:260px;
    height:auto;
    font-size: 5vmin;
    border-radius: 20px;
    opacity:0.8;
    box-shadow:  7px 7px 16px #d0d0d0,
             -7px -7px 16px #f0f0f0;
}

.intable{
	width:85%;
	margin-left:auto; 
  margin-right:auto;
}

hr {
width: 50%;
margin-left: auto;
margin-right: auto;
}

.neumbtn{
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border:0;
    border-radius:8px;
    text-align:center;
    font-size:calc(12px + 1vmin);
    height:4vmin;
    min-height:30px;
    box-shadow: 5px 5px 10px #d9d9d9, 
             -5px -5px 10px #ffffff;
    vertical-align: middle;
    
    color: #000080;
    background: #ffffff;
    font-weight: bold;
}

.cust-select{
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    text-align: center;
    text-align-last: center;
    border:1;
    border-radius:8px;
    font-size:calc(12px + 1vmin);
    height:4vmin;
    min-height:30px;
    width:90%;
    vertical-align: middle;
    color: #000080;
    background: #ffffff;
    font-weight: bold;
}

.boxfdin{
  animation: fdinFrames linear 1s;
  animation-iteration-count: 1;
  transform-origin: 50% 50%;
  -webkit-animation: fdinFrames linear 1s;
  -webkit-animation-iteration-count: 1;
  -webkit-transform-origin: 50% 50%;
  -moz-animation: fdinFrames linear 1s;
  -moz-animation-iteration-count: 1;
  -moz-transform-origin: 50% 50%;
  -o-animation: fdinFrames linear 1s;
  -o-animation-iteration-count: 1;
  -o-transform-origin: 50% 50%;
  -ms-animation: fdinFrames linear 1s;
  -ms-animation-iteration-count: 1;
  -ms-transform-origin: 50% 50%;
}

@keyframes fdinFrames{
  0% {
    opacity:0.17;
    transform:  translate(-50px,0px)  ;
  }
  100% {
    opacity:1;
    transform:  translate(0px,0px)  ;
  }
}

@-moz-keyframes fdinFrames{
  0% {
    opacity:0.17;
    -moz-transform:  translate(-50px,0px)  ;
  }
  100% {
    opacity:1;
    -moz-transform:  translate(0px,0px)  ;
  }
}

@-webkit-keyframes fdinFrames {
  0% {
    opacity:0.17;
    -webkit-transform:  translate(-50px,0px)  ;
  }
  100% {
    opacity:1;
    -webkit-transform:  translate(0px,0px)  ;
  }
}

@-o-keyframes fdinFrames {
  0% {
    opacity:0.17;
    -o-transform:  translate(-50px,0px)  ;
  }
  100% {
    opacity:1;
    -o-transform:  translate(0px,0px)  ;
  }
}

@-ms-keyframes fdinFrames {
  0% {
    opacity:0.17;
    -ms-transform:  translate(-50px,0px)  ;
  }
  100% {
    opacity:1;
    -ms-transform:  translate(0px,0px)  ;
  }
}

.modal-content {
  border-radius: 8px; 
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  overflow-x:hidden;
  overflow-y:scroll;
  word-break:break-all；
  max-width:80%;
  height:150px;
  width: 80%;
}

'''

## Generate episode menu
genlst = ''''''
seleopt = '''<option selected="selected" value="">☰ 🎤 ☰</option>'''
listdir = sorted(listdir)
eplst = []
for ep in listdir:
    catep = [f for f in os.listdir(os.path.join(baset["source"],ep)) if f.endswith(baset["ext"]) and "episode" in os.path.basename(f)]
    if len(catep) > 0:
        print("Catch episode :",ep)
        idn = "ep_"+str(listdir.index(ep))
        eplst.append(idn)
        seleopt+='''<option value="'''+idn+'''">☊ '''+ep+'''</option>'''
        genlst+=gencrd(ep,idn)

## Menu Controller
seljs = '''
<script>
function check(e){
    var itmlst = [\"'''+"\",\"".join(eplst)+'''\"];
    var i;
    for (i = 0; i < itmlst.length; i++) {
            var itm = document.getElementById(itmlst[i])
            if (itm.style.display != 'none') {
                        itm.style.display = 'none';
            }
    }
    document.getElementById(e).style.display = "";
 }
</script>
'''

menu = '''
<div class='neumorphismcrd' style="min-width:260px;">
<select class="cust-select" onchange="check(this.value)">'''+seleopt+'''</select>
</div>
<br>
'''

## Generating Page
page = head+seljs+menu+genlst+foot

with open("index.html","w+",encoding="utf8") as cstlst:
    cstlst.write(page)
cstlst.close()

playr = "player.html"
if not os.path.isfile(playr):
    with open(playr,"w+",encoding="utf8") as playr:
        playr.write(playerpag)
    playr.close()

cstyl = os.path.join("resource","style.css")
if not os.path.isfile(cstyl):
    with open(cstyl,"w+",encoding="utf8") as styl:
        styl.write(style)
    styl.close()

print("Done!")
