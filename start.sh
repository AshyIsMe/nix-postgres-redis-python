#!/usr/bin/env bash

pg_ctl -D data -l postgres.log start
redis-server &
