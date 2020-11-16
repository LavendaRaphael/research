#!/bin/bash
set -eo pipefail

grep 'pseudo' Templates/*
grep 'SHTU' script/*
grep 'SHTU' ~/tianff/environment.sh

