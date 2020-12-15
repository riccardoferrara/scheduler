def str2bool(str_var):
    if str_var.lower() == 'false':
        return False
    elif str_var.lower() == 'true':
        return True
    else:
        print('%s cannot be converter to boolean variable' % str_var)
        return None

def hours2seconds(hours):
    seconds = hours*60*60
    return seconds