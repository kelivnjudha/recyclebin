def format_likes_count(n):
    if n < 1000:
        return str(n)
    elif n < 1000000:
        return "{:.1f}k".format(n/1000).rstrip('0').rstrip('.')
    elif n < 1000000000:
        return "{:.1f}M".format(n/1000000).rstrip('0').rstrip('.')
    else:
        return "{:.1f}B".format(n/1000000000).rstrip('0').rstrip('.')
