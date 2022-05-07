@echo off
setlocal
echo This script runs the website locally.
echo While this script is running, any changes you make will be automatically detected.
echo Open the following link in your browser to view the website (CTRL + click the link to open it):
echo http://localhost:4000
echo =======================

echo Running and serving...
echo Press CTRL + C to stop (or just close the window)

bundle exec jekyll serve

echo Done! Press any key to exit...
pause >nul
