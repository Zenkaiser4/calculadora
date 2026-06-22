[app]

# (str) Title of your application
title = Calculadora

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow

# (str) Presplash and Icon of the application
presplash.filename = %(source.dir)s/calcu.png
icon.filename = %(source.dir)s/calcu.png

# (list) Supported orientations
orientation = portrait

# Opciones específicas de Android
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 26b
android.ndk_api = 21

# TRUCO DEFINITIVO: Forzamos a Buildozer a usar herramientas versión 33 en vez de la 37
android.build_tools_version = 33.0.1

android.private_storage = True
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Opciones específicas de Python for Android (p4a)
p4a.branch = develop
p4a.bootstrap = sdl2

# Opciones específicas de iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1
