#!/bin/bash

# dependency: youtube-dl. (google it, install it, update if necessary.)
# download videos from youtube and convert into audio files.

# Usage:
# At the commandline, change directory to desktop or to the location
# where you want to download the audio files.
# For example,
# me@mycomputer $ cd ~/desktop
# me@mycomputer desktop $ chmod +x youtube_v2.sh
# me@mycomputer desktop $ ./youtube_v2.sh paste_your_youtube_video_url_here add_another_url_here_separated_by_a_space add_as_many_urls_as_you_want

for arg in "$@";
do
    youtube-dl -F "$arg";
    youtube-dl -f 140 "$arg";
    echo "COMPLETE";
done

exit 0
