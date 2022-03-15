<img width="544" alt="image" src="https://user-images.githubusercontent.com/31820707/108661418-60d4b500-74fe-11eb-81ed-c164df9ef4a5.png">

# Frida Android hook
📍 A tool that helps you can easy using frida. It support script for trace classes, functions, and modify the return values of methods on iOS platform.

👉 For iOS platform: [frida-ios-hook](https://github.com/noobpk/frida-ios-hook)

## Env OS Support
| OS      | Supported          | Noted   |
| ------- | ------------------ | ------- |
| MacOS   | :white_check_mark: | main	 |
| Linux   | :white_check_mark: | sub  	 |
| Windows | :white_check_mark: | sub	 |

## Compatible with
| Android Api   |  Frida   | Supported         |
| ------------- | ---------| ----------------- |
|  8.0 - Api 26 | 14.2.13  | :white_check_mark:|
|  8.0 - Api 26 | 15.0.18  | :white_check_mark:|

## Feature

Running with python3.x

Support both spawn & attach script to process.

```
[+] Options:

	-p(--package)		Identifier of application ex: com.android.calendar
	-n(--name) 		Name of application ex: Calendar
	-s(--script) 		Using script format script.js
	-c(--check-version) 	Check for the newest version
	-u(--update) 		Update to the newest version
	
	[*] Dump memory aplication:
	
    	--dump-memory         Dump memory of application

	[*] Information:

	--fs-install	    Install frida server
	--fs-start          Start frida server
	--fs-stop           Stop frida server
	--list-devices      List All Devices
	--list-apps         List the installed apps
	--list-scripts      List All Scripts
	--logcat            Show system log of device
	--shell             Get the shell of connect device

	[*] Quick method:

	-m(--method)    Support commonly used methods
				app-static(-n)
				bypass-jb(-p)
				bypass-ssl(-p)
				i-url-req(-p)
				i-crypto(-n)
```

## ChangeLog

[See Full ChangeLog](https://github.com/noobpk/frida-android-hook/blob/master/CHANGELOG.md)

## Install & Usage

```
1. Git clone https://github.com/noobpk/frida-android-hook
2. cd frida-android-hook/
3. chmod +x androidhook
4. Start Frida-server: `./androidhook --fs-start`
5. ./androidhook --help(-h)
6. rebellion :))

```

If you run the script but it doesn't work, you can try the following:
```frida -U -f package -l script.js```

## 📺 Demo Feature

|N|Title|Link|
|:---|:---|:---|
|1||
|2||
|3||

## Frida Scripts

|N|Spawn/Attach|Script Name| Script Description|Script Version|
|:---|:---|:---|:---|:---|
|1|S+A|android-intercepts-crypto.js|Android Intercepts Crypto Operations|1.0|
|2|S+A|android-logcat.js|Android logcat capture|1.0|
|3|S+A|call-method-of-class.js|Call method of class|1.0|
|4|S+A|dupDex.js|dupDex|1.0|
|5|S+A|fingerprint-bypass-via-exception-handling.js|Fingerprint bypass via Exception Handling.|1.0|
|6|S+A|fingerprint-bypass.js|Fingerprint bypass|1.0|
|7|S+A|hook-method-of-class.js|Hook method of class|1.0|
|8|S|raptor_frida_android_bypass.js|Raptor frida android bypass|1.0|
|9|S|raptor_frida_android_debug.js|Raptor frida android debug|1.0|
|10|S|raptor_frida_android_enum.js|Raptor frida android enum|1.0|
|11|S|raptor_frida_android_findClass1.js|Raptor frida android findclass 1|1.0|
|12|S|raptor_frida_android_findClass2.js|Raptor frida android findclass 2|1.0|
|13|S|raptor_frida_android_lowlevel.js|Raptor frida android low level |1.0|
|14|S|raptor_frida_android_trace.js|Raptor frida android trace|1.0|
|15|S+A|show-all-classes-methods.js|Show all class name and method|1.0|
|16|S+A|show-all-classes.js|Show all class name|1.0|
|17|S+A|show-module-exported-functions.js|Show module exported function|1.0|
|18|S+A|show-modules-exports.js|Show modules exports|1.0|
|19|S+A|show-specific-class-methods.js|Show specific class and method|1.0|

## Disclaimer
Because I am not a developer, so my coding skills might not be the best. Therefore, if this tool have any issue or not working for you, create an issue and i will try to fix it.
Any suggestions for new feature and discussions are welcome!


