#!/usr/bin/env python3

#############################################
#                                           #
#  Patrick Killian - pkillian@berkeley.edu  #
#                                           #
#          playlist_export.py               #
#   -------------------------------------   #
#  A tool for exporting and sharing '.m3u'  #
#  formatted playlists. The script will     #
#  copy files described in an '.m3u' file   #
#  and export them in an organized manner.  #
#                                           #
#      Creative Commons Copyright           #
#   Attribution-NonCommercial-ShareAlike    #
#                                           #
#  This license lets others remix, tweak,   #
#  and build upon works non-commercially,   #
#  as long as they credit [Patrick Killian] #
#  and license their new creations under    #
#  the identical terms.                     #
#                                           #
#   http://creativecommons.org/licenses/    #
#                                           #
#############################################

### BEGIN IMPORTS ###

from shutil import *
import sys, os, re

### BEGIN IMPLEMENTATION ###

class FormatError(Exception):
    def __init__(self, message):
        self.message = message

def print_help():
    """ Prints help information for script. """
    print("""
        Playlist Exporter v1.4.2 Patrick Killian -- pkillian@berkeley.edu
        
	MUST USE PYTHON3 WITH THIS SCRIPT. Python2 or below will NOT
	load the playlist file correctly.

        Takes a '.m3u' playlist file as input, and exports all songs 
        to a folder on user's desktop by default (a different output
        location can be specified with the '-o' flag described here).
        
        Makes sharing iTunes playlists simple -- just send the 
        folder/compressed file to a friend, and they can open the 
        newly created '.m3u' file to import directly to iTunes or 
        other music programs.
        
        USAGES: 
        	playlist_export [FLAGS: -vhzoD] /path/to/file.m3u "output filename"
		python3 playlist_export.py [FLAGS: -vhzoD] /path/to/file.m3u "output filename"
		./playlist_export.py [FLAGS: -vhzoD] /path/to/file.m3u "output filename"	
        
        FLAGS: 
        
            Combine all flags into one term: -vzD for Verbose, Zip and Delete
        
        -v -- Verbose Mode: Prints progress during execution.
        -h -- Print help and exit. Will not complete script if -h is used at all.
        -z -- Zips playlist folder after completion.
        -o -- Allows the user to specify a different output folder. 
        -D -- Deletes playlist file used in execution, as well as all temporary files. \n""")

def check_format():
    """ Raises a FormatError iff the last input item is not a '.m3u' file. """
    if len(sys.argv) < 3:
        print_help()
        sys.exit(0)
    if sys.argv[-2][-4:] != '.m3u':
        raise FormatError("Wrong format. Use 'python playlist_export.py -h' for usage.")

def check_flags(flags):
    global zip, output_path, delete, verbose
    for flag in flags:
        if flag == 'h':
            ### Print help menu and exit if '-h' used.
            print_help()
            sys.exit(0)
        elif flag == 'z':
            ### Determine if zipping is to be completed.
            zip = True
        elif flag == 'o':
            output_path = sys.argv[-3]
            if output_path[-1] == '/':
                output_path = output_path[:-1]
        elif flag == 'D':
            delete = True
        elif flag == 'v':
            verbose = True
        elif '-'+flag in sys.argv:
            raise FormatError("Wrong format. Use 'python playlist_export.py -h' for usage.")
        else:
            raise FormatError("{0} is not a valid option.".format(flag))

### INIT VARIABLES AND FLAGS ###

try:
    ### Check input format.
    check_format()
    
    ### Init variables.
    verbose = False
    zip = False
    delete = False
    filename = sys.argv[-1]
    m3u = open(sys.argv[-2]).read().split('\n')[:-1]
    m3u_name = re.sub(r'.*/', "", sys.argv[-2])
    output_path = os.getenv("HOME") + "/Desktop"
    
    ### Examine flag input.
    if re.match(r"^-", sys.argv[1]):
        check_flags(sys.argv[1][1:]) 
    
    output_path_file = output_path + '/' + filename
    songs_folder = output_path_file + '/Songs'
        
### ACCOUNT FOR ERRORS 

except FormatError as error:
    print(error.message)
    sys.exit("EXITING: Export failed!")

except IOError as error:
    print(error)
    sys.exit("EXITING: Export failed!")

### BEGIN EXECUTION ###

print("Creating playlist from {0}...".format(sys.argv[-1])) 

if verbose: 
    print("Making folders at {0}...".format(output_path_file))

### CREATE FOLDERS

if not os.path.exists(output_path_file):
    os.makedirs(output_path_file)
if not os.path.exists(songs_folder):
    os.makedirs(songs_folder)

### COPY ALL FILES INTO NEWLY MADE SONGS FOLDER

if verbose:
    print("Copying files from iTunes to {0}...".format(songs_folder))

files = [x for x in m3u if '#EXT' not in x]

for x in files:
    if verbose:
        print("Copying file {0}...".format(x))
    copy2(x, songs_folder)

if verbose:
    print("Done!")
    print("Making new playlist file...")

### GATHER DATA TO WRITE PLAYLIST FILE

song_names = []
contents = []

for x in files:
    song_names.append(x.split('/').pop(-1))

for x in m3u:
    if '#EXT' in x:
        contents.append(x + '\n')
    else:
        contents.append('./Songs/' + song_names.pop(0) + '\n')

if verbose:
    print("Done!")
    print("Writing playlist to file: {0}".format(output_path_file))

### OPEN FILEHANDLE; WRITE CONTENTS TO DISK

new_file = open(output_path_file + '/' + m3u_name, "w")
new_file.writelines(contents)

if verbose:
    print("Done!")
    print("Cleaning up...")

### CLOSE FILEHANDLE, ZIP AND DELETE TEMPORARY FILES USED

new_file.close()

if zip:
    print("Zipping {0}...".format(output_path_file))
    make_archive(output_path_file, 'zip', output_path_file + '/')
    if verbose:
        print("Done!")

if delete:
    if verbose:
        print("Deleting {0}...".format(sys.argv[-2]))
    os.remove(sys.argv[-2])

if zip:
    if verbose:
        print("Deleting {0}...".format(output_path_file))
    rmtree(output_path_file)

print("Done!")
print("Enjoy!")
