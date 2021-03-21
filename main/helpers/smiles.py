def create_smile(smile_code):
    return (smile_code.encode("latin_1").decode("raw_unicode_escape").encode('utf-16', 'surrogatepass').decode('utf-16'))
