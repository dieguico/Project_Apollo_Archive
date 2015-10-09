# Project Apollo Archive
Script written in python 2.7 to download the entire NASA's Project Apollo Archive hosted in flickr, with the original resolution. 

The script creates _number_of_threads_ asynchronous threads and each one downloads one picture. The pictures are stored in _destination_folder_. By default are used 4 threads and the pictures are stored in the ~/Desktop/NASA_Apollo_Project/ folder, with ~ being expanded by the os module.

The script takes pictures' urls and names from the file _photo_links_. Before initiates the download it checks the destination folder for pictures and only get the remainig.

Usage: 
```python
  python huston_we_want_pictures.py destination_folder number_of_threads
```

It's a massive download, by October 9th there are 13029 pictures. **So click, relax, and get ready to enjoy the views.** 
