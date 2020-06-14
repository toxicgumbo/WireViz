COLOR_CODES = {
               'DIN': ['WH','BN','GN','YE','GY','PK','BU','RD','BK','VT'], # ,'GYPK','RDBU','WHGN','BNGN','WHYE','YEBN','WHGY','GYBN','WHPK','PKBN'],
               'IEC': ['BN','RD','OG','YE','GN','BU','VT','GY','WH','BK'],
               'BW':  ['BK','WH']
              }

color_hex = {
             'BK': '#000000',
             'WH': '#ffffff',
             'GY': '#999999',
             'PK': '#ff66cc',
             'RD': '#ff0000',
             'OG': '#ff8000',
             'YE': '#ffff00',
             'GN': '#00ff00',
             'TQ': '#00ffff',
             'BU': '#0066ff',
             'VT': '#8000ff',
             'BN': '#666600',
              }

color_full = {
             'BK': 'black',
             'WH': 'white',
             'GY': 'grey',
             'PK': 'pink',
             'RD': 'red',
             'OG': 'orange',
             'YE': 'yellow',
             'GN': 'green',
             'TQ': 'turquoise',
             'BU': 'blue',
             'VT': 'violet',
             'BN': 'brown',
}

color_ger = {
             'BK': 'sw',
             'WH': 'ws',
             'GY': 'gr',
             'PK': 'rs',
             'RD': 'rt',
             'OG': 'or',
             'YE': 'ge',
             'GN': 'gn',
             'TQ': 'tk',
             'BU': 'bl',
             'VT': 'vi',
             'BN': 'br',
}

def translate_color(input, color_mode):
    if input == '':
        output = ''
    else:
        if color_mode == 'full':
            output = color_full[input].lower()
        elif color_mode == 'FULL':
            output = color_full[input].upper()
        elif color_mode == 'hex':
            output = color_hex[input].lower()
        elif color_mode == 'HEX':
            output = color_hex[input].upper()
        elif color_mode == 'ger':
            output = color_ger[input].lower()
        elif color_mode == 'GER':
            output = color_ger[input].upper()
        elif color_mode == 'short':
            output = input.lower()
        elif color_mode == 'SHORT':
            output = input.upper()
        else:
            raise Exception('Unknown color mode')
    return output
