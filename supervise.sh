#!/usr/bin/env bash

export NODE_PATH=./config:./controllers
export PORT=3030

supervisor -e 'html|js' app rest-api.js
