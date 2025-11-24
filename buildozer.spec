[app]
title = Quiz Game
package.name = quizgame
package.domain = com.quiz.app
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,xml
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
# (un)comment android.permissions as needed
android.permissions = 
# the entry point
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
icon.filename = icons/icon_192.png
