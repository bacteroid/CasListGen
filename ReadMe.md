## CasListGen

A simple web page generator for podcast playlist display (with player).
  
---
  
## Description
  
### Usage
Put this script under root folder alone with the folder contains your episode records, the file structure should be like below.
  
### File Structure
```
Root Folder
└─ CasListGen.py <- Place here !
└─ Source (Folder)
	└─ Episode1 (Folder)
	│ └─ episode.m4a <- Main file
	│ └─ info.txt <- Ep content
	└─ Episode2 (Folder)
	│ └─ episode.m4a
	│ └─ info.txt
	...
```
  
### Naming Rule
- Your folder name will be the title for each episode.
- Media file should be named as "episode" for the program to recgonize as the main sound source.
- Text file "info.txt" is not necessary, but will become the content note for your episode if existed.
  
### Configuration File
```
[CAST]
title = Your Cast Title
cover = Cast Cover
logo = Cast Logo
source = Cast Source Path
ext = Extension of Media File

[SERVER]
port = Port for your web server
cycle = Time peroid for checking episode list
mode = Web server mode [True / False]
```
  
### Note
- Index content will be overwrite  
  
---
  
## Todo List
- [x] Read episode from given folder.
- [x] Generate playlist and player page for the show.
- [ ] Generate RSS Feed for the show. (Pending)
- [x] Run in background as simple web server.
- [x] Auto update playing list.
  
---
  
## Release Note
  
### 2022-02-07
- Add web server.
- Fix some bugs.

<details>
<summary>Show More</summary>
<p>

#### 2022-02-07
- First Release

</p>
</details> 