import zlib

s = b'Tres tristes tigres comian trigo en un trigal muy muy muy grande'
print(len(s))

t = zlib.compress(s)
print(len(t))

