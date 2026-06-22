[app]

# (str) Title of your application
title = Calculadora

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,hostpython3,kivy=2.3.0,pillow

# (str) Presplash of the application
presplash.filename = %(source.dir)s/calcu.png

# (str) Icon of the application
icon.filename = %(source.dir)s/calcu.png

# (list) Supported orientations
orientation = portrait


# =============================================================================
# Opciones específicas de Android (Modificadas para GitHub Actions)
# =============================================================================

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API (API 34 es el estándar requerido actualmente)
android.api = 34

# (int) Minimum API your APK / AAB will support
android.minapi = 24

# (str) Android NDK version to use (La versión 27c evita fallos de glibc en Ubuntu 24.04)
android.ndk = 27c

# (int) Android NDK API to use. Generalmente debe coincidir con android.minapi
android.ndk_api = 24

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True


# =============================================================================
# Opciones específicas de Python for Android (p4a)
# =============================================================================

# (str) python-for-android branch to use (Desarrollo obligatorio para NDKs modernos)
p4a.branch = develop

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2


# =============================================================================
# Opciones específicas de iOS
# =============================================================================
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false


# =============================================================================
# Configuración del motor Buildozer
# =============================================================================
[buildozer]

# (int) Log level (2 = debug detallado con salida de comandos)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
