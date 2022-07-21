#! /usr/bin/env python3
"""Philippine phone service provider identifier"""

import re


def main():

    # Service provider prefixes
    DITO = [
        '0895', '0896', '0897', '0898', '0991', '0992', '0993', '0994'
    ]

    GLOBE = [
        '0817', '0905', '0906', '0915', '0916', '0917', '0926', '0927',
        '0935', '0936', '0937', '0945', '0953', '0954', '0955', '0956',
        '0965', '0966', '0967', '0975', '0976', '0977', '0978', '0979',
        '0995', '0996', '0997',
    ]

    GLOBE_EXTRA = [
        '09253', '09255', '09256', '09257', '09258'
    ]

    SMART = [
        '0908', '0918', '0919', '0920', '0921', '0928', '0929', '0939',
        '0946', '0947', '0949', '0951', '0961', '0998', '0999'
    ]

    SUN = [
        '0922', '0923', '0924', '0925', '0931', '0932', '0933', '0934',
        '0940', '0941', '0942', '0943', '0973', '0974'
    ]

    TNT = [
        '0907', '0909', '0910', '0912', '0930', '0938', '0946', '0948',
        '0950'
    ]

    number = input('Enter phone number: ')

    # Substitutes country calling code with 0 if number begins with one
    country_code = re.compile(r'^\+63')
    number = country_code.sub(r'0', number)

    # Strip digit separators
    separator = re.compile(r'\s|-|\.')
    number = separator.sub(r'', number)

    if len(number) != 11:
        print('Invalid number')
        return

    prefix = number[0:4]

    # Special prefix case
    if prefix == '0925':
        prefix = number[0:5]
        if prefix in GLOBE_EXTRA:
            print('Provider: GLOBE')
            return
        else:
            print('Provider: SUN')
            return

    if prefix in DITO:
        print('Provider: DITO')
        return

    if prefix in GLOBE:
        print('Provider: GLOBE')
        return

    if prefix in SMART:
        print('Provider: SMART')
        return

    if prefix in SUN:
        print('Provider: SUN')
        return

    if prefix in TNT:
        print('Provider: TNT')
        return

    print('Invalid number')


if __name__ == '__main__':
    main()