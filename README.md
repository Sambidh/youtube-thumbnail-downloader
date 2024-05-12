
# Youtube thumbnail downloader

I created a simple Youtube video thumbnail downloader using Python. 
## Deployment

Please go through the following instructions.

These are some the packages required to run this programs.

### Step 1: Find Channel ID

First, we open 'channel id finder.py' file. In this file, we need to install pytube python package. Install it using the prompt bellow.
```bash
  pip install pytube
```
Run the program after installing the required package.
We will be asked the URL of any youtube video of the youtuber whose channel id we want. 
We will be provided an output where we can find the channel id of the youtuber. Let's copy it.

### Step 2: Video Link Scrapping

Secondly, we will open 'video link scrapper.py' file. We need to install few new python packages. 

```bash
  pip install scrapetube
```
```bash
  pip install pandas
```
```bash
  pip install openpyxl
```
```bash
  pip install workbook
```

After installing all these packages, we run the program. Here, we will be asked the channel id of the youtuber. Copy & paste the channel id and then all the URLs will be written in an excel file.

### Step 3: Download Youtube Video Thumbnails

Finally in this step, we need to install urllib3 python package. 

```bash
  pip install urllib3
```

After installing the package, we need to edit the code and change the path of the excel file. Change it according to your file path location. And then run the program. 

Downloading the thumbnails could sometime so be patient. 


## Acknowledgements

 - [Took help from here for thumbnail downloading code](https://medium.com/@omogidavis/mastering-python-how-to-download-youtube-video-thumbnails-with-python-c5e93fc49321#:~:text=Use%20urllib.,jpg.)
 - [Took help from here for retrieving youtube video URLS of a youtube channel](https://youtu.be/LUOm0QqL3q8?si=wTuljsnbNhJN3vdH)
 - [Took help from here for finding the channel id](https://youtu.be/p2IKvHnzyS8?si=tmPJq37c-I1z4r0X)


## Contributing

Contributions are always welcome! I am new to this. Trying raising an issue. But I honestly do not know what to do if I get it. 

