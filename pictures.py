import exifread
import piexif
import sys


exif_dict = piexif.load("test_image.JPG")

list_of_keys = exif_dict["0th"].keys()

print list_of_keys
sys.exit()

#print piexif.TAGS["0th"]
for tag in exif_dict["0th"].keys():
    print "Key: %s, value %s" % (tag, exif_dict[tag])

#    print(piexif.TAGS[tag]["name"], exif_dict[tag])



#print tags

#for ifd in ("0th", "Exif", "GPS", "1st"):
#    for tag in exif_dict[ifd]:
#        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])


print "^^^^^^\n\n"
# Open image file for reading (binary mode)
f = open("test_image.JPG", 'rb')

# Return Exif tags
tags = exifread.process_file(f)
#print tags
#print type(tags)
print tags["Image Model"]
#print tags
#for tag in tags.keys():

 #   Image Model

 #   print tag
    #if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        #print "Key: %s, value %s" % (tag, tags[tag])

