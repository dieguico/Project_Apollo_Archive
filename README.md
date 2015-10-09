# Project Apollo Archive
Script written in python 2.7 to download the entire NASA's Project Apollo Archive hosted in flickr, with the original resolution. 

The script creates four asynchronous threads and each one downloads one picture. The pictures are stored in ~/Desktop/NASA_Apollo_Project/ folder, with ~ being expanded by the os module.

The script takes pictures' urls and names from the file _photo_links_. Before initiates the download it checks the destination folder for pictures and only get the remainig.

It's a massive download, by October 9th there are 13029 pictures. **So click, relax, and get ready to enjoy the views.** 
