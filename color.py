def set_color(string, color=None, bold=None, italic=None, blinking=None, highlite_color=None, underline=None):
    bold_value,color_value,italic_value,blinking_value,highlite_color_value,underline_value = None,None,None,None,None,None
    if bold:
        bold_value = '1'
    else:
        bold_value = '0'
    if italic: 
        italic_value = '3'
    else:
        italic_value = '0'
    if blinking:
        blinking_value = '5'
    else:
        blinking_value = '0'
    if underline:
        if underline.lower() == "Normal":
            underline_value = '4'
        elif underline.lower() == "Taxt Cut":
            underline_value = '9'
        elif underline.lower() == "Double":
            underline_value = '21'
        elif underline.lower() == "Space":
            underline_value = '52'
    else:
        underline_value = '0'   
    if color:
        if color.lower() == "Gray":
            color_value = '30'
        elif color.lower() == "Bright Red":
            color_value = '31'
        elif color.lower() == "Bright Green":
            color_value = '32'
        elif color.lower() == "Bright Yellow":
            color_value = '33'
        elif color.lower() == "Bright Blue":
            color_value = '34'
        elif color.lower() == "Bright Magenta":
            color_value = '35'
        elif color.lower() == "Bright Cyan":
            color_value = '36'
        elif color.lower() == "Bright White":
            color_value = '37'
        elif color.lower() == "Olive":
            color_value = '90'
        elif color.lower() == "Red":
            color_value = '91'
        elif color.lower() == "Green":
            color_value = '92'
        elif color.lower() == "Yellow":
            color_value = '93'
        elif color.lower() == "Blue":
            color_value = '94'
        elif color.lower() == "Magenta":
            color_value = '95'
        elif color.lower() == "Cyan":
            color_value = '96'
        elif color.lower() == "White":
            color_value = '97'
    else:
        color_value = '0'
    if highlite_color:
        if highlite_color.lower() == "Bright Gray":
            highlite_color_value = '40'
        elif highlite_color.lower() == "Bright Red":
            highlite_color_value = '41'
        elif highlite_color.lower() == "Bright Green":
            highlite_color_value = '42'
        elif highlite_color.lower() == "Bright Yellow":
            highlite_color_value = '43'
        elif highlite_color.lower() == "Bright Blue":
            highlite_color_value = '44'
        elif highlite_color.lower() == "Bright Magenta":
            highlite_color_value = '45'
        elif highlite_color.lower() == "Bright Cyan":
            highlite_color_value = '46'
        elif highlite_color.lower() == "Bright White":
            highlite_color_value = '47'
        if highlite_color.lower() == "Olive":
            highlite_color_value = '100'
        elif highlite_color.lower() == "Red":
            highlite_color_value = '101'
        elif highlite_color.lower() == "Green":
            highlite_color_value = '102'
        elif highlite_color.lower() == "Yellow":
            highlite_color_value = '103'
        elif highlite_color.lower() == "Blue":
            highlite_color_value = '104'
        elif highlite_color.lower() == "Magenta":
            highlite_color_value = '105'
        elif highlite_color.lower() == "Cyan":
            highlite_color_value = '106'
        elif highlite_color.lower() == "White":
            highlite_color_value = '107'
    else:
        highlite_color_value = '0'

    if color_value != '0':
        if highlite_color_value != '0':
            if bold_value != '0':
                if italic_value != '0':
                    if underline_value != '0':
                        if blinking_value != '0':
                            return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                        else:
                            return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                    elif blinking_value != '0':
                        return '\033['+bold_value+';'+italic_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                    else:
                        return '\033['+bold_value+';'+italic_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                elif underline_value != '0':
                    if blinking_value != '0':
                        return '\033['+bold_value+';'+underline_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                    else:
                        return '\033['+bold_value+';'+underline_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                elif blinking_value != '0':
                    return '\033['+bold_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif italic_value != '0':
                if underline_value != '0':
                    if blinking_value != '0':
                        return '\033['+italic_value+';'+underline_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                    else:
                        return '\033['+italic_value+';'+underline_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                elif blinking_value != '0':
                    return '\033['+italic_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+italic_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif underline_value != '0':
                if blinking_value != '0':
                    return '\033['+underline_value+';'+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+underline_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+blinking_value+';'+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
            else:
                return '\033['+color_value+';'+highlite_color_value+'m'+string+'\033[0m'
        elif bold_value != '0':
            if italic_value != '0':
                if underline_value != '0':
                    if blinking_value != '0':
                        return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
                    else:
                        return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+color_value+'m'+string+'\033[0m'
                elif blinking_value != '0':
                    return '\033['+bold_value+';'+italic_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+italic_value+';'+color_value+'m'+string+'\033[0m'
            elif underline_value != '0':
                if blinking_value != '0':
                    return '\033['+bold_value+';'+underline_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+underline_value+';'+color_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+bold_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
            else:
                return '\033['+bold_value+';'+color_value+'m'+string+'\033[0m'
        elif italic_value != '0':
            if underline_value != '0':
                if blinking_value != '0':
                    return '\033['+italic_value+';'+underline_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+italic_value+';'+underline_value+';'+color_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+italic_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
            else:
                return '\033['+italic_value+';'+color_value+'m'+string+'\033[0m'
        elif underline_value != '0':
            if blinking_value != '0':
                return '\033['+underline_value+';'+blinking_value+';'+color_value+'m'+string+'\033[0m'
            else:
                return '\033['+underline_value+';'+color_value+'m'+string+'\033[0m'
        elif blinking_value != '0':
            return '\033['+blinking_value+';'+color_value+'m'+string+'\033[0m'
        else:
            return '\033['+color_value+'m'+string+'\033[0m'
    elif highlite_color_value != '0':
        if bold_value != '0':
            if italic_value != '0':
                if underline_value != '0':
                    if blinking_value != '0':
                        return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
                    else:
                        return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+highlite_color_value+'m'+string+'\033[0m'
                elif blinking_value != '0':
                    return '\033['+bold_value+';'+italic_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+italic_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif underline_value != '0':
                if blinking_value != '0':
                    return '\033['+bold_value+';'+underline_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+underline_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+bold_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
            else:
                return '\033['+bold_value+';'+highlite_color_value+'m'+string+'\033[0m'
        if italic_value != '0':
            if underline_value != '0':
                if blinking_value != '0':
                    return '\033['+italic_value+';'+underline_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
                else:
                    return '\033['+italic_value+';'+underline_value+';'+highlite_color_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+italic_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
            else:
                return '\033['+italic_value+';'+highlite_color_value+'m'+string+'\033[0m'
        elif underline_value != '0':
            if blinking_value != '0':
                return '\033['+underline_value+';'+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
            else:
                return '\033['+underline_value+';'+highlite_color_value+'m'+string+'\033[0m'
        elif blinking_value != '0':
            return '\033['+blinking_value+';'+highlite_color_value+'m'+string+'\033[0m'
        else:
            return '\033['+highlite_color_value+'m'+string+'\033[0m'
    elif bold_value != '0':
        if italic_value != '0':
            if underline_value != '0':
                if blinking_value != '0':
                    return '\033['+bold_value+';'+italic_value+';'+underline_value+';'+blinking_value+'m'+string+'\033[0m'
                else:
                    return '\033['+bold_value+';'+italic_value+';'+underline_value+'m'+string+'\033[0m'
            elif blinking_value != '0':
                return '\033['+bold_value+';'+italic_value+';'+blinking_value+'m'+string+'\033[0m'
            else:
                return '\033['+bold_value+';'+italic_value+'m'+string+'\033[0m'
        elif underline_value != '0':
            if blinking_value != '0':
                return '\033['+bold_value+';'+underline_value+';'+blinking_value+'m'+string+'\033[0m'
            else:
                return '\033['+bold_value+';'+underline_value+'m'+string+'\033[0m'
        elif blinking_value != '0':
            return '\033['+bold_value+';'+blinking_value+'m'+string+'\033[0m'
        else:
            return '\033['+bold_value+'m'+string+'\033[0m'
    elif italic_value != '0':
        if underline_value != '0':
            if blinking_value != '0':
                return '\033['+italic_value+';'+underline_value+';'+blinking_value+'m'+string+'\033[0m'
            else:
                return '\033['+italic_value+';'+underline_value+'m'+string+'\033[0m'
        elif blinking_value != '0':
            return '\033['+italic_value+';'+blinking_value+'m'+string+'\033[0m'
        else:
            return '\033['+italic_value+'m'+string+'\033[0m'
    elif underline_value != '0':
        if blinking_value != '0':
            return '\033['+underline_value+';'+blinking_value+'m'+string+'\033[0m'
        else:
            return '\033['+underline_value+'m'+string+'\033[0m'
    elif blinking_value != '0':
        return '\033['+blinking_value+'m'+string+'\033[0m'

