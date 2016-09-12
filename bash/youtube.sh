#!/bin/bash

# dependency: youtube-dl. (google it, install it.)
# download videos from youtube and convert into audio files.
# replace url with the url link, it's passed in as a string.

declare -a arr playlist=("url1" "url2" "url3")

for i in "${playlist[@]}"
do
    youtube-dl -F "$i"
    youtube-dl -f 140 "$i"
    echo "COMPLETE"
done

exit 0
