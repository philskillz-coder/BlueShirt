import json

done = False
supported_locales = ["en-US", "de"]
locales: dict[str, dict[str, str]] = {}

for locale in supported_locales:
    with open(f"Translations/{locale}.json", "rb") as f:
        data: dict[str, str] = json.loads(f.read().decode())
        locales[locale] = data


class _AdvancedFormat(dict):
    def __missing__(self, _key: str):
        return '{' + _key + '}'


def save():
    for i, e in locales.items():
        with open(f"Translations/{i}.json", "w") as _f:
            json.dump(e, _f, indent=4)


while not done:
    command = input("Enter command >>> ")
    if command == "d":
        done = True
        break

    if command == "n":
        key = input("Enter key >>> ")
        for _l in supported_locales:
            _lT = input(f"Enter translation for locale: {_l} >>> ").format_map(_AdvancedFormat(n="\n"))
            locales[_l][key] = _lT
        print("Saved.\n")
        save()

    if command == "e":
        pass

    if command == "ek":
        pass
