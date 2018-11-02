import os
import datetime
import re
import logging
import platform
import sys

logger = logging.getLogger('filerenamer')
logger.setLevel(logging.DEBUG)
hdlr = logging.FileHandler('filerenamer.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
hdlr.setLevel(logging.INFO)
logger.addHandler(hdlr)
logging.getLogger().addHandler(logging.StreamHandler())

ext = (".mov", ".mp4", ".mpg", ".mpeg", \
       ".jpg", ".jpeg", ".png", "3gp", "avi")
tagged_format = re.compile("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]")

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def rename(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            fullfilename = root + "/" + filename
            logger.info("processing %s", fullfilename)
            if filename.lower().endswith((tuple(ext))):
                # it's a media file...
                logger.debug("%s is a media file", fullfilename)
                if re.match(tagged_format, filename):
                    logger.debug("file has already been processed: %s", fullfilename)
                    # this file was already renamed.. so we don't want to do anything
                else:
                    if " " in filename:
                        logger.debug("File name has spaces, skipping processing %s", fullfilename)
                    else:
                        """ let's skip anything that has a space in the name - that way, anything that's been 
                        custom named will also be skipped so long as we chose a name with a space in it """

                        logger.debug("we're going to rename %s based on the creation date", fullfilename)
                        #stamp1 = datetime.datetime.fromtimestamp(os.path.getctime(fullfilename)).strftime("%Y%m%d_%H%M%S")  # get file modification timestamp
                        #stamp2 = datetime.datetime.fromtimestamp(os.path.getmtime(fullfilename)).strftime("%Y%m%d_%H%M%S")  # get file modification timestamp
                        #print fullfilename
                        #print "stamp1: "+stamp1
                        #print "stamp2: "+stamp2
                        #sys.exit()

                        created_time = os.path.getmtime(fullfilename)  # get file modification timestamp
                        created_date = datetime.datetime.fromtimestamp(created_time)  # convert timestamp to a date
                        date_as_name = created_date.strftime("%Y%m%d_%H%M%S")
                        fileext = os.path.splitext(filename)[1]
                        target_name = os.path.join(root, '{}{}'.format(date_as_name, fileext))

                        matched = True
                        count = 0
                        while matched:
                            # let's do the check at least once to make sure it
                            if os.path.isfile(target_name):
                                logger.debug("File already exists... this would overwrite")
                                count = count + 1
                                target_name = os.path.join(root, '{}{}'.format(date_as_name + "_" + str(count), fileext))
                            else:
                                # file doesn't exist.
                                matched = False
                                if count < 1:
                                    # basically, do nothing, no name change needed
                                    pass
                                else:
                                    target_name = os.path.join(root, '{}{}'.format(date_as_name+ "_" +  str(count), fileext))
                        logger.info("Renaming %s to %s", fullfilename, target_name)
                        os.rename(fullfilename, target_name)
            else:
                logger.debug("%s is NOT a media file", filename)
#                print "it's a match %s", filename
#            else:
#                print "no match %s", filename
#

#rename("c:\\tmp\\")
#rename("Z:\\Library\\Home\\Pets\\Dogs")
#rename("Z:\\Library\\Vacation")