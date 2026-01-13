#!/bin/bash

CTFD_URL="https://ctf.bluraven.io"
API="$CTFD_URL/api/v1"
SESSION_COOKIE="${SESSION_COOKIE:?Set SESSION_COOKIE environment variable}"

case "$1" in
  challenges)
    curl -s -b "session=$SESSION_COOKIE" "$API/challenges" | jq '.data[] | {id, name, category, value, solved_by_me}'
    ;;

  challenge)
    curl -s -b "session=$SESSION_COOKIE" "$API/challenges/$2" | jq '.data'
    ;;

  submit)
    if [ -z "$2" ] || [ -z "$3" ]; then
      echo "Usage: ./ctfd.sh submit <challenge_id> <flag>"
      exit 1
    fi
    # Get CSRF nonce
    NONCE=$(curl -s -b "session=$SESSION_COOKIE" "$CTFD_URL/challenges" | grep -oP "(?<='csrfNonce': \")[^\"]+")
    # Submit with CSRF token
    curl -s -b "session=$SESSION_COOKIE" \
      -H "Content-Type: application/json" \
      -H "CSRF-Token: $NONCE" \
      -X POST "$API/challenges/attempt" \
      --data-raw "{\"challenge_id\": $2, \"submission\": \"$3\"}" | jq '.'
    ;;

  scoreboard)
    curl -s -b "session=$SESSION_COOKIE" "$API/scoreboard" | jq '.data[:10]'
    ;;

  *)
    echo "Usage: ./ctfd.sh {challenges|challenge <id>|submit <id> <flag>|scoreboard}"
    ;;
esac
