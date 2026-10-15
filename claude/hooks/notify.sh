#!/usr/bin/env bash
# Notification/Stop hook: desktop ping via notify-send. Silent no-op on headless servers.
command -v notify-send >/dev/null || exit 0
[ -n "$DISPLAY$WAYLAND_DISPLAY$DBUS_SESSION_BUS_ADDRESS" ] || exit 0

input=$(cat)
event=$(jq -r '.hook_event_name // empty' <<<"$input" 2>/dev/null)
project=$(basename "$(jq -r '.cwd // empty' <<<"$input" 2>/dev/null)")

case "$event" in
  Notification) msg=$(jq -r '.message // "braucht dich"' <<<"$input"); urgency=critical ;;
  Stop)         msg="fertig ✅"; urgency=normal ;;
  *)            exit 0 ;;
esac

notify-send -a "Claude" -u "$urgency" -i dialog-information "Claude · ${project:-?}" "$msg" 2>/dev/null
exit 0
