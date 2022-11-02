#!/bin/bash
pwd > $PWD
cd /app/archive
coverage run -m pytest
coverage report
coverage html
echo "file:///home/"$(whoami)"/personal/stage-archive/stage-archive-backend/archive/htmlcov/index.html"
cd $PWD