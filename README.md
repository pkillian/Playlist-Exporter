Playlist-Exporter
=================

Playlist Exporter v1.3; Patrick Killian -- pkillian@berkeley.edu


Creative Commons Copyright: http://creativecommons.org/licenses/

Attribution-NonCommercial-ShareAlike -- CC BY-NC-SA
This license lets others remix, tweak, and build upon your work non-commercially, as long as they credit you and license their new creations under the identical terms.


Playlist Exporter: Copies all necessary files and information and aggregates it in order to make playlist sharing simple.
        
        YOU MUST USE PYTHON3 WITH THIS SCRIPT!! The file input will fail with python2 or below.

        Takes a '.m3u' playlist file as input, and exports all songs 
        to a folder on user's desktop by default (a different output
        location can be specified with the '-o' flag described here).
        
        Makes sharing iTunes playlists simple -- just send the 
        folder/compressed file to a friend, and they can open the 
        newly created '.m3u' file to import directly to iTunes or 
        other music programs.
        
        USAGES: 
                python playlist_export.py [FLAGS: -vhzoD] /path/to/file.m3u "output filename"
                ./playlist_export.py [FLAGS: -vhzoD] /path/to/file.m3u "output filename"
        FLAGS: 
        
            Combine all flags into one term: -vzD for Verbose, Zip and Delete
        
        -v -- Verbose Mode: Prints progress during execution.
        -h -- Print help and exit. Will not complete script if -h is used at all.
        -z -- Zips playlist folder after completion.
        -o -- Allows the user to specify a different output folder. 
        -D -- Deletes playlist file used in execution, as well as all temporary files.
