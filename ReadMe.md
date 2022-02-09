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
- Blog Post (Mandarin) : [Click Here](https://mercuryagar.wordpress.com/2022/01/28/%e7%ad%86%e8%a8%98-%e9%83%bd%e5%81%9a%e4%ba%86%e9%82%84%e5%9c%a8%e6%87%b6-%e8%a9%a6%e5%af%ab-podcast-%e5%b1%95%e7%a4%ba%e7%b6%b2%e9%a0%81%e7%94%9f%e6%88%90%e5%99%a8/)
  
---
  
## Todo List
- [x] Read episode from given folder.
- [x] Generate playlist and player page for the show.
- [ ] Generate RSS Feed for the show. (Pending)
- [x] Run in background as simple web server.
- [x] Auto update playing list.
  
---
  
## Release Note
  
### 2022-02-08
- Add web server.
- Fix some bugs.

<details>
<summary>Show More</summary>
<p>

#### 2022-02-07
- First Release

</p>
</details> 