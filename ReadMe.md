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
  
### Note
- Index content will be overwrite  
  
---
  
## Todo List
- [x] Read episode from given folder.
- [x] Generate playlist and player page for the show.
- [ ] Generate RSS Feed for the show. (Pending)
- [ ] Run in background as simple web server.
- [ ] Auto update playing list.
  
---
  
## Release Note
  
### 2022-02-07
- First Release

<details>
<summary>Show More</summary>
<p>

None

</p>
</details> 