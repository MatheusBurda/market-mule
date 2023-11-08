{"payload":{"allShortcutsEnabled":false,"fileTree":{"src":{"items":[{"name":"__init__.py","path":"src/__init__.py","contentType":"file"},{"name":"bindings.cpp","path":"src/bindings.cpp","contentType":"file"},{"name":"calibrate.py","path":"src/calibrate.py","contentType":"file"},{"name":"gh-actions-rpi-cmd.sh","path":"src/gh-actions-rpi-cmd.sh","contentType":"file"},{"name":"install-deps.sh","path":"src/install-deps.sh","contentType":"file"},{"name":"test.py","path":"src/test.py","contentType":"file"}],"totalCount":6},"":{"items":[{"name":".github","path":".github","contentType":"directory"},{"name":".vscode","path":".vscode","contentType":"directory"},{"name":"src","path":"src","contentType":"directory"},{"name":".bumpversion.cfg","path":".bumpversion.cfg","contentType":"file"},{"name":".gitattributes","path":".gitattributes","contentType":"file"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"hx711.gif","path":"hx711.gif","contentType":"file"},{"name":"pyproject.toml","path":"pyproject.toml","contentType":"file"},{"name":"setup.py","path":"setup.py","contentType":"file"}],"totalCount":11}},"fileTreeProcessingTime":12.061626,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":396795607,"defaultBranch":"master","name":"hx711-rpi-py","ownerLogin":"endail","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2021-08-16T12:58:17.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/52652357?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1674023666.25399","canEdit":false,"refType":"branch","currentOid":"d30b682b8814217144a3d7dc09bd183f0a55e68d"},"path":"src/calibrate.py","currentUser":null,"blob":{"rawLines":["import os","import sys","from datetime import timedelta","","from HX711 import *","","if len(sys.argv) != 3:","    print(\"Usage: calibrate.py [data pin] [clock pin]\", file=sys.stderr)","    sys.exit(os.EX_USAGE)","","try:","    hx = SimpleHX711(int(sys.argv[1]), int(sys.argv[2]), 1, 0)","except GpioException:","    print(\"Failed to connect to HX711 chip\", file=sys.stderr)","    sys.exit(os.EX_UNAVAILABLE)","except TimeoutException:","    print(\"Failed to connect to HX711 chip\", file=sys.stderr)","    sys.exit(os.EX_UNAVAILABLE)","","","print(\"\"\"","\\x1B[2J\\x1B[H","========================================","HX711 Calibration","========================================","","Find an object you know the weight of. If you can't find anything,","try searching Google for your phone's specifications to find its weight.","You can then use your phone to calibrate your scale.","\"\"\")","","unit = input(\"1. Enter the unit you want to measure the object in (eg. g, kg, lb, oz): \")","","knownWeight = float(input(\"2. Enter the weight of the object in the unit you chose (eg. \" +","                    \"if you chose 'g', enter the weight of the object in grams): \"))","","samples = int(input(\"3. Enter the number of samples to take from the HX711 chip (eg. 15): \"))","","input(\"4. Remove all objects from the scale and then press enter.\")","print(\"Working...\")","","zeroValue = hx.read(Options(int(samples)))","","input(\"5. Place object on the scale and then press enter.\")","print(\"Working...\")","","raw = hx.read(Options(int(samples)))","refUnitFloat = (raw - zeroValue) / knownWeight","refUnit = round(refUnitFloat, 0)","","if refUnit == 0:","    refUnit = 1","","print(","    \"\\n\\n\" +","    \"Known weight (your object) \" + str(knownWeight) + \" \" + unit + \"\\n\" +","    \"Raw value over \" + str(samples) + \" samples: \" + str(raw) + \"\\n\" +","    \"\\n\" +","    \"-> REFERENCE UNIT: \" + str(round(refUnit)) + \"\\n\" +","    \"-> ZERO VALUE: \" + str(round(zeroValue)) + \"\\n\" +","    \"\\n\" +","    \"You can provide these values to the constructor when you create the \"","    \"HX711 objects or later on. For example: \\n\" +","    \"\\n\" +","    \"hx = SimpleHX711(\" + sys.argv[1] + \", \" + sys.argv[2] + \", \" + ","    str(round(refUnit)) + \", \" + str(round(zeroValue)) + \")\\n\" +","    \"OR\\n\" +","    \"hx.setReferenceUnit(\" + str(round(refUnit)) + \") and \" +","    \"hx.setOffset(\" + str(round(zeroValue)) + \")\\n\"",")","","sys.exit(os.EX_OK)"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":9,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":20,"cssClass":"pl-k"},{"start":21,"end":30,"cssClass":"pl-s1"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":10,"cssClass":"pl-v"},{"start":11,"end":17,"cssClass":"pl-k"},{"start":18,"end":19,"cssClass":"pl-c1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":6,"cssClass":"pl-en"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":54,"cssClass":"pl-s"},{"start":56,"end":60,"cssClass":"pl-s1"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":61,"end":64,"cssClass":"pl-s1"},{"start":65,"end":71,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":24,"cssClass":"pl-v"}],[],[{"start":0,"end":3,"cssClass":"pl-k"}],[{"start":4,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-v"},{"start":21,"end":24,"cssClass":"pl-en"},{"start":25,"end":28,"cssClass":"pl-s1"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":39,"end":42,"cssClass":"pl-en"},{"start":43,"end":46,"cssClass":"pl-s1"},{"start":47,"end":51,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":57,"end":58,"cssClass":"pl-c1"},{"start":60,"end":61,"cssClass":"pl-c1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":20,"cssClass":"pl-v"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":43,"cssClass":"pl-s"},{"start":45,"end":49,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-c1"},{"start":50,"end":53,"cssClass":"pl-s1"},{"start":54,"end":60,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":30,"cssClass":"pl-v"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":23,"cssClass":"pl-v"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":43,"cssClass":"pl-s"},{"start":45,"end":49,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-c1"},{"start":50,"end":53,"cssClass":"pl-s1"},{"start":54,"end":60,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":30,"cssClass":"pl-v"}],[],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":9,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"},{"start":0,"end":4,"cssClass":"pl-cce"},{"start":7,"end":11,"cssClass":"pl-cce"}],[{"start":0,"end":40,"cssClass":"pl-s"}],[{"start":0,"end":17,"cssClass":"pl-s"}],[{"start":0,"end":40,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":66,"cssClass":"pl-s"}],[{"start":0,"end":72,"cssClass":"pl-s"}],[{"start":0,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":12,"cssClass":"pl-en"},{"start":13,"end":88,"cssClass":"pl-s"}],[],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-en"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":89,"cssClass":"pl-s"},{"start":90,"end":91,"cssClass":"pl-c1"}],[{"start":20,"end":82,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-en"},{"start":14,"end":19,"cssClass":"pl-en"},{"start":20,"end":91,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":66,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":18,"cssClass":"pl-s"}],[],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":14,"cssClass":"pl-s1"},{"start":15,"end":19,"cssClass":"pl-en"},{"start":20,"end":27,"cssClass":"pl-v"},{"start":28,"end":31,"cssClass":"pl-en"},{"start":32,"end":39,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":58,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":18,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":8,"cssClass":"pl-s1"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":21,"cssClass":"pl-v"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":33,"cssClass":"pl-s1"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":31,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":46,"cssClass":"pl-s1"}],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":15,"cssClass":"pl-en"},{"start":16,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":10,"cssClass":"pl-s1"},{"start":11,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":10,"cssClass":"pl-s"},{"start":5,"end":7,"cssClass":"pl-cce"},{"start":7,"end":9,"cssClass":"pl-cce"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":4,"end":33,"cssClass":"pl-s"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":39,"cssClass":"pl-en"},{"start":40,"end":51,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":55,"end":58,"cssClass":"pl-s"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":61,"end":65,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":68,"end":72,"cssClass":"pl-s"},{"start":69,"end":71,"cssClass":"pl-cce"},{"start":73,"end":74,"cssClass":"pl-c1"}],[{"start":4,"end":21,"cssClass":"pl-s"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-en"},{"start":28,"end":35,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":51,"cssClass":"pl-s"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":54,"end":57,"cssClass":"pl-en"},{"start":58,"end":61,"cssClass":"pl-s1"},{"start":63,"end":64,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-s"},{"start":66,"end":68,"cssClass":"pl-cce"},{"start":70,"end":71,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-s"},{"start":5,"end":7,"cssClass":"pl-cce"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":25,"cssClass":"pl-s"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":31,"cssClass":"pl-en"},{"start":32,"end":37,"cssClass":"pl-en"},{"start":38,"end":45,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s"},{"start":51,"end":53,"cssClass":"pl-cce"},{"start":55,"end":56,"cssClass":"pl-c1"}],[{"start":4,"end":21,"cssClass":"pl-s"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-en"},{"start":28,"end":33,"cssClass":"pl-en"},{"start":34,"end":43,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":52,"cssClass":"pl-s"},{"start":49,"end":51,"cssClass":"pl-cce"},{"start":53,"end":54,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-s"},{"start":5,"end":7,"cssClass":"pl-cce"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":74,"cssClass":"pl-s"}],[{"start":4,"end":48,"cssClass":"pl-s"},{"start":45,"end":47,"cssClass":"pl-cce"},{"start":49,"end":50,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-s"},{"start":5,"end":7,"cssClass":"pl-cce"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":23,"cssClass":"pl-s"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":40,"end":44,"cssClass":"pl-s"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-s1"},{"start":51,"end":55,"cssClass":"pl-s1"},{"start":56,"end":57,"cssClass":"pl-c1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":61,"end":65,"cssClass":"pl-s"},{"start":66,"end":67,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-en"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":21,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-en"},{"start":37,"end":42,"cssClass":"pl-en"},{"start":43,"end":52,"cssClass":"pl-s1"},{"start":55,"end":56,"cssClass":"pl-c1"},{"start":57,"end":62,"cssClass":"pl-s"},{"start":59,"end":61,"cssClass":"pl-cce"},{"start":63,"end":64,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-s"},{"start":7,"end":9,"cssClass":"pl-cce"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":4,"end":26,"cssClass":"pl-s"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-en"},{"start":33,"end":38,"cssClass":"pl-en"},{"start":39,"end":46,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-c1"},{"start":51,"end":59,"cssClass":"pl-s"},{"start":60,"end":61,"cssClass":"pl-c1"}],[{"start":4,"end":19,"cssClass":"pl-s"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":31,"cssClass":"pl-en"},{"start":32,"end":41,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":46,"end":51,"cssClass":"pl-s"},{"start":48,"end":50,"cssClass":"pl-cce"}],[],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":8,"cssClass":"pl-en"},{"start":9,"end":11,"cssClass":"pl-s1"},{"start":12,"end":17,"cssClass":"pl-v"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/endail/hx711-rpi-py/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/endail/hx711-rpi-py/security/dependabot","repoSecurityAndAnalysisPath":"/endail/hx711-rpi-py/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"calibrate.py","displayUrl":"https://github.com/endail/hx711-rpi-py/blob/master/src/calibrate.py?raw=true","headerInfo":{"blobSize":"2.22 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"9faf8a5","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fendail%2Fhx711-rpi-py%2Fblob%2Fmaster%2Fsrc%2Fcalibrate.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"72","truncatedSloc":"56"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/endail/hx711-rpi-py/discussions/new","newIssuePath":"/endail/hx711-rpi-py/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/endail/hx711-rpi-py/blob/master/src/calibrate.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/endail/hx711-rpi-py/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"endail","repoName":"hx711-rpi-py","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"unit","kind":"constant","identStart":826,"identEnd":830,"extentStart":826,"extentEnd":915,"fullyQualifiedName":"unit","identUtf16":{"start":{"lineNumber":31,"utf16Col":0},"end":{"lineNumber":31,"utf16Col":4}},"extentUtf16":{"start":{"lineNumber":31,"utf16Col":0},"end":{"lineNumber":31,"utf16Col":89}}},{"name":"knownWeight","kind":"constant","identStart":917,"identEnd":928,"extentStart":917,"extentEnd":1093,"fullyQualifiedName":"knownWeight","identUtf16":{"start":{"lineNumber":33,"utf16Col":0},"end":{"lineNumber":33,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":33,"utf16Col":0},"end":{"lineNumber":34,"utf16Col":84}}},{"name":"samples","kind":"constant","identStart":1095,"identEnd":1102,"extentStart":1095,"extentEnd":1188,"fullyQualifiedName":"samples","identUtf16":{"start":{"lineNumber":36,"utf16Col":0},"end":{"lineNumber":36,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":36,"utf16Col":0},"end":{"lineNumber":36,"utf16Col":93}}},{"name":"zeroValue","kind":"constant","identStart":1279,"identEnd":1288,"extentStart":1279,"extentEnd":1321,"fullyQualifiedName":"zeroValue","identUtf16":{"start":{"lineNumber":41,"utf16Col":0},"end":{"lineNumber":41,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":41,"utf16Col":0},"end":{"lineNumber":41,"utf16Col":42}}},{"name":"raw","kind":"constant","identStart":1404,"identEnd":1407,"extentStart":1404,"extentEnd":1440,"fullyQualifiedName":"raw","identUtf16":{"start":{"lineNumber":46,"utf16Col":0},"end":{"lineNumber":46,"utf16Col":3}},"extentUtf16":{"start":{"lineNumber":46,"utf16Col":0},"end":{"lineNumber":46,"utf16Col":36}}},{"name":"refUnitFloat","kind":"constant","identStart":1441,"identEnd":1453,"extentStart":1441,"extentEnd":1487,"fullyQualifiedName":"refUnitFloat","identUtf16":{"start":{"lineNumber":47,"utf16Col":0},"end":{"lineNumber":47,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":47,"utf16Col":0},"end":{"lineNumber":47,"utf16Col":46}}},{"name":"refUnit","kind":"constant","identStart":1488,"identEnd":1495,"extentStart":1488,"extentEnd":1520,"fullyQualifiedName":"refUnit","identUtf16":{"start":{"lineNumber":48,"utf16Col":0},"end":{"lineNumber":48,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":48,"utf16Col":0},"end":{"lineNumber":48,"utf16Col":32}}}]}},"copilotInfo":null,"csrf_tokens":{"/endail/hx711-rpi-py/branches":{"post":"0PssFxOEyFzqOIVkxICsj3D1YwTk8GIbLS8U5NH39SE9A7kMk7ramu8lGl1sNXlUkrh4M6keWWtko4A-PHR_uA"},"/repos/preferences":{"post":"Yx7uFih4--jAtsr4m4tNAQa8QLbXJyS8YzJdd_sVVPxtARfKn4LO3AImFJXoVybopOtI2-rToAiBOyTLB3DB5A"}}},"title":"hx711-rpi-py/src/calibrate.py at master · endail/hx711-rpi-py"}