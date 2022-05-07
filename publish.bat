@echo off
setlocal
echo Publishing your site...

git switch master
git merge staging
git push
git switch staging

echo Done! Press any key to exit...
pause >nul
