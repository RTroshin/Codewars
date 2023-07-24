def year_days(year):
    return f"{year} has {'365' if year % 4 or year % 400 and not year % 100 else '366'} days"
