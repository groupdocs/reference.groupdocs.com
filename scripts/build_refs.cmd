@echo off
rem Run from the repo root regardless of where this script is invoked (it now lives in scripts/).
cd /d "%~dp0.."
call git submodule update --init --recursive
call git submodule foreach git pull origin master
call npm install -D --save autoprefixer postcss-cli
call hugo server --configDir config/sites/groupdocs/home --disableFastRender
