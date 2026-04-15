@echo off
call git submodule update --init --recursive
call git submodule foreach git pull origin master
call npm install -D --save autoprefixer postcss-cli
call hugo server --configDir config/sites/groupdocs/home --disableFastRender
