#!/bin/bash

secs=60
endTime=$(( $(date +%s) + secs ))
while [ $(date +%s) -lt $endTime ]; do
  already_running=$(docker compose ps | grep -c "running")
  already_running=$((already_running+1))
  containers_count=$(docker compose ps | wc -l)
  echo -en "\rWaiting for services... $already_running/$containers_count"
  if [[ $already_running -eq $containers_count ]]; then
    echo ""
    exit 0
  fi
  sleep 1
done

exit 1