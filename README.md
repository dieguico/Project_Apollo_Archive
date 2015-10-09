# Project Apollo Archive
Script to download the entire NASA's Project Apollo Archive hosted in flickr, with the original resolution. 

The script creates four threads and each thread downloads one picture. The pictures are stored in ~/Desktop/NASAs/ folder, with ~ being expanded by the os module.

The script takes pictures' urls and names from the file _photo_links_. Before start the download checks the folder ~/Desktop/NASAs/ and only download the pictures left.

It's a massive download, by October 9th there are 13000+ pictures. **So click, relax, and get ready to enjoy the views** 
