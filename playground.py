from armorstand.date import DateCode
from armorstand.date import get_date

d = get_date(
    [
        DateCode.DAY_NAME,
        DateCode.COMMA,
        DateCode.DAY,
        DateCode.MONTH,
        DateCode.COMMA,
        DateCode.YEAR,
    ],
    # return_strf=True,
)

print(d)
