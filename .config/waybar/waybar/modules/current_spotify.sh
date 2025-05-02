#!/bin/bash

# Config
scroll_speed=0.5   # Time between scrolls
padding=" "    # Space between end and start of the scroll

while true; do
    # Get metadata
    metadata=$(playerctl --player=spotify metadata --format "{{ artist }} - {{ title }}")

    # If no song is playing, sleep and continue
    if [[ -z "$metadata" ]]; then
        echo '{"text": ""}'
        sleep 1
        continue
    fi

    # Add padding and prepare scrollable text
    scroll_text="$metadata$padding"
    len=${#scroll_text}
    offset=0

    # Scroll the text
    for (( i=0; i<len; i++ )); do
        part="${scroll_text:offset}${scroll_text:0:offset}"
        echo "{\"text\": \"${part:0:40}\"}"  # Adjust width as needed
        sleep $scroll_speed
        offset=$(( (offset + 1) % len ))
    done
done

