def isValid(yesNo_welcome):
    if yesNo_welcome in ['yes','Yes', 'YES', 'y', 'Y', 'No', 'NO', 'n', 'N', 'no']:
        return True
    else:
        return False

def launchChoice(userLaunch):
    if userLaunch in ['l', 'L', 'Launch', 'launch']:
        return True
    else:
        return False
