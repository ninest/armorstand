from armorstand.date import get_date, DateCode

d = get_date([DateCode.MONTH_NUMBER, DateCode.SLASH, DateCode.DAY,DateCode.SLASH, DateCode.SHORT_YEAR], return_strf=True)

print(d)