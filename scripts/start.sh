#!/bin/bash
# shellcheck disable=SC2046
# shellcheck disable=SC2164

cd `dirname $0`/..
docker-compose up --build --force-recreate
