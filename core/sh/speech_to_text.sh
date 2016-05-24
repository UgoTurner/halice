#!/bin/bash

DIR_PATH=$PWD

# Listening :
printf "\n\r1) => Listening"
rec -q $DIR_PATH/core/sh/recording.flac rate 32k silence 1 0.1 10% 1 3.0 10% &
sleep 1
p=$!
until [ "$var1" != "$var2" ]; do
	var1=`du "$DIR_PATH/core/sh/recording.flac"`
	sleep 1
	var2=`du "$DIR_PATH/core/sh/recording.flac"`
done
kill $p
printf "\n\r2) => Sound detected"
mpg321 -q $DIR_PATH/core/sounds/listening.mp3

# Record when sound detected :
printf "\n\r3) => Start recording"
rec -q -r 16000 -c 1 $DIR_PATH/core/sh/speech.flac &
p=$!
sleep 3
kill $p
printf "\n\r4) => End of recording"

# Convert sound to text :
wget -q --post-file $DIR_PATH/core/sh/speech.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v2/recognize?client=chromium&lang=en-EN&key=YOUR_KEY" > $DIR_PATH/core/sh/result.json
#wget -qO- --post-file "$1" --header 'Content-type: audio/x-flac; rate=16000' "$url" 
speech="$(cat $DIR_PATH/core/sh/result.json | sed 's/^[^[]*\[{\"utterance\":\"\([^\"]*\)\".*/\1/' | tr ‘[A-Z]‘ ‘[a-z]‘)"
printf "$speech" >> $DIR_PATH/core/logs/logs.txt