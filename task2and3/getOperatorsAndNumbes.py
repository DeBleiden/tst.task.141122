
# Country code combined with operator's code for replacement and strip.
# 050 / 093 / 096 in this variant, could be removed from the end a number.
defaultCountryCode = ["+38050", "+38093", "+38096"]


# Show numbers that has predefined country code and area code combination with its operator.
def getOperatorByCode(fileData):
    for i in fileData:
        for y in fileData[i]:
            for x in range(len(defaultCountryCode)):
                if defaultCountryCode[x] in y.get("number"):
                    print(defaultCountryCode[x], "|", y.get("name"), "|", y.get("number"))
    return


# Show numbers without country code and without operator's code
def getUserNumber(fileData):
    for i in fileData:
        for y in fileData[i]:
            string = y.get("number")
            for x in range(len(defaultCountryCode)):
                if defaultCountryCode[x] in string:
                    string = string.replace(defaultCountryCode[x], " ")
                    string = string.strip()
                    print("Number without country code and operator's code:", string)
    return
