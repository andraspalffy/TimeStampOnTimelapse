from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
 
font = ImageFont.truetype("arial.ttf", 100) #select your font ans size for the clock
fontsmall = ImageFont.truetype("arial.ttf", 50) #select your font ans size for the date
fontcolor = (255,255,255) #color of the timestamp
counter = 0

x_start = 130
y_start = 0
dx = 3870
dy = 2177

text_y_date = 120
text_y_hour = 160

# Go through each file in current directory
for i in os.listdir(os.getcwd()):
    if i.endswith(".JPG"): #modify extension here
        counter += 1
        # For debugging: limit how many images are processed:
        if counter>10:
             break
        print("Image {0}: {1}".format(counter, i))

        img = Image.open(i) #open image
        exif = img._getexif() #extract exif
        creation_time = exif.get(36867) #get date-time from exif
        splitup = creation_time.split(":") #split fetched date 
        day_hour = splitup[2].split(" ") #day and hour are splitted here
        date = splitup[0]+'-'+splitup[1]+'-'+day_hour[0] #create date string in yyyy-mm-dd form
        hour = int(day_hour[1])%24 #fetch hours
        tformatted = str(hour).zfill(2) +':'+splitup[3] #create time string in hh:mm form
        img = img.crop((x_start, y_start, x_start + dx, y_start + dy)) #crop image if needed
 
        # get a drawing context
        draw = ImageDraw.Draw(img)
        draw.text((img.width-320, text_y_date), date, fontcolor, font=fontsmall)
        draw.text((img.width-315, text_y_hour), tformatted, fontcolor, font=font)
        filename = "resized/" + "img" + str(counter).zfill(5)+".jpg" #create filename
        img.save(filename) #save image