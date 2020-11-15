#!/bin/bash
set -eo pipefail

find  ./  -maxdepth 1 -type d -exec chmod 750 {} \;
find  ./  -maxdepth 1 -type f -exec chmod 640 {} \;
find  ./  -maxdepth 1 -name "*.sh"  -exec chmod 750 {} \;
