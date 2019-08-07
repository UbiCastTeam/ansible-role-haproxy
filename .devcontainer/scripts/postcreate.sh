#!/usr/bin/env bash

# copy local ssh config
mkdir -p ~/.ssh
cp -r ~/.ssh-localhost/* ~/.ssh
find ~/.ssh -type d -exec chmod 700 {} +
find ~/.ssh -type f -exec chmod 600 {} +
