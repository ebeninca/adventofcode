import os
import re

with open(os.path.dirname(__file__) + '/day04input.txt') as f:
    passports = [line for line in f]


def validatePassports(requiredFields, validateValues):
    validFields = 0
    validPassports = 0
    passport = {}
    for idx, line in enumerate(passports):

        if line in ('\n', '\r\n'):
            if validFields == len(requiredFields):
                if not validateValues:
                    validPassports += 1
                elif isFieldsValid(requiredFields, passport):
                    validPassports += 1
            passport = {}
            print(idx, validFields, validPassports)
            validFields = 0
            continue

        for keyValue in line.split('\x20'):
            key, value = keyValue.split('\x3A')
            if key in requiredFields.keys():
                passport.update({key: value})
                validFields += 1

        if idx == len(passports)-1:
            if validFields == len(requiredFields):
                if not validateValues:
                    validPassports += 1
                elif isFieldsValid(requiredFields, passport):
                    validPassports += 1
            passport = {}
            print(idx, validFields, validPassports)

    return validPassports


def isFieldsValid(requiredFields, passport):
    validFieldsCount = 0
    for reqKey, reqValue in requiredFields.items():

        if reqKey in ['byr', 'iyr', 'eyr']:
            minv, maxv = [int(i) for i in reqValue.split('\x2D')]
            value = int(passport[reqKey].strip())
            if value >= minv and value <= maxv:
                validFieldsCount += 1

        elif reqKey == 'hgt':
            cm, inch = reqValue.split('\x2C')
            intVal = int(re.findall(r'\d+', passport[reqKey].strip())[0])
            if 'cm' in passport[reqKey].strip():
                minv, maxv, mesu = [i for i in cm.split('\x2D')]
                if intVal >= int(minv) and intVal <= int(maxv):
                    validFieldsCount += 1
            elif 'in' in passport[reqKey].strip():
                minv, maxv, mesu = [i for i in inch.split('\x2D')]
                if intVal >= int(minv) and intVal <= int(maxv):
                    validFieldsCount += 1

        elif reqKey == 'hcl':
            match = re.findall(
                r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport[reqKey].strip())
            if len(match) == 1:
                validFieldsCount += 1

        elif reqKey == 'ecl':
            listValid = reqValue.split('\x2C')
            value = passport[reqKey].strip()
            if value in listValid:
                validFieldsCount += 1

        elif reqKey == 'pid':
            if len(passport[reqKey].strip()) == 9:
                try:
                    int(passport[reqKey].strip())
                    validFieldsCount += 1
                except:
                    continue

    return validFieldsCount == len(requiredFields)


requiredFields = {'byr': '1920-2002', 'iyr': '2010-2020', 'eyr': '2020-2030',
                  'hgt': '150-193-cm,59-76-in', 'hcl': '#000000', 'ecl': 'amb,blu,brn,gry,grn,hzl,oth', 'pid': '123456789'}

print(validatePassports(requiredFields, False))

print(validatePassports(requiredFields, True))
