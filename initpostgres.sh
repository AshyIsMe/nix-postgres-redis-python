#!/usr/bin/env bash

mkdir data

export LOCALE_ARCHIVE="/usr/lib/locale/locale-archive"

pg_ctl -D data init

