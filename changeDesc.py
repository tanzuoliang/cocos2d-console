#!/usr/bin/python

"""
/Users/tanzuoliang/Documents/tools/cocos2d-x-3.12/tools/cocos2d-console/plugins/plugin_compile/build_android.py
	[line:500]             add by tzl old is 'compile_obj.compile_js_scripts(assets_dir, assets_dir)' new is 'if not no_apk:compile_obj.compile_js_scripts(assets_dir, assets_dir)'

/Users/tanzuoliang/Documents/tools/cocos2d-x-3.12/tools/cocos2d-console/plugins/plugin_compile/project_compile.py
	[line:141]           add by tzl  self._just_apk = args.just_apk or "0"

	[line:479]         add by tzl old is 'if (not self._project._is_script_project() or self._project._is_native_support()):' now is 'if self._just_apk == "0" and (not self._project._is_script_project() or self._project._is_native_support()):'

"""