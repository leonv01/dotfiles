#!/bin/bash

APP_NAME="hyprsunset"

function toggle_nightlight()
{
	if pgrep -x "$APP_NAME" > /dev/null; then
		killall "$APP_NAME"
	else
		"$APP_NAME" &
	fi
}

function get_status()
{
	if pgrep -x "hyprsunset" > /dev/null; then
		echo '{"text": "🌙"}'
	else
		echo '{"text": "☀️"}'
	fi
}

if [[ "$1" == "toggle" ]]; then
	toggle_nightlight
fi
get_status
