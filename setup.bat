@echo off
setlocal
:PROMPT
echo Setting up a development environment...
echo This script assumes Jekyll and Bundler are installed.
echo You only need to run this ONCE.

bundle install || PAUSE
