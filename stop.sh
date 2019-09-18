#!/usr/bin/env bash

pg_ctl -D data stop
pkill redis-server
