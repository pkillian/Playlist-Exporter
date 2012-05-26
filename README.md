Playlist-Exporter
=================

Python Script: Copies all necessary files and information and aggregates it in order to make playlist sharing simple.

Playlist Exporter v1.0; Patrick Killian -- pkillian@berkeley.edu
        
        Takes a '.m3u' playlist file as input, and exports all songs 
        to a folder on user's desktop by default (a different output
        location can be specified with the '-o' flag described here).
        
        Makes sharing iTunes playlists simple -- just send the 
        folder/compressed file to a friend, and they can open the 
        newly created '.m3u' file to import directly to iTunes or 
        other music programs.
        
        USAGE: python playlist_export.py [FLAGS: -vhzoD] /path/to/file.m3u "output filename"
        
        FLAGS: 
        
            Combine all flags into one term: -vzD for Verbose, Zip and Delete
        
        -v -- Verbose Mode: Prints progress during execution.
        -h -- Print help and exit. Will not complete script if -h is used at all.
        -z -- Zips playlist folder after completion.
        -o -- Allows the user to specify a different output folder. 
        -D -- Deletes playlist file used in execution, as well as all temporary files.