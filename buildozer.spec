[app]

title = Kozel
package.name = kozel
package.domain = org.far

source.dir = .
source.include_exts = py,png,jpg,wav,ttf,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

p4a.bootstrap = sdl2


[buildozer]

log_level = 2
warn_on_root = 1
