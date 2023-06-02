import json as js
with open('keys.json') as f:
    keys = js.load(f)

data = {
    "title": "ADNW layout",
    "rules": [
        {
            "description": "Personalized ADNW layout to bypass Ukelele ",
            "manipulators": [
            ]
        }
    ]
}

for key in keys:
    for i in range(len(key["to_keys"])):
        data["rules"][0]["manipulators"].append(
            {
             "type": "basic",
             "from": {
                 "key_code": key["from_key"],
                 "modifiers": key["from_mods"][i]
             },
             "to": [
                 {
                 "key_code": key["to_keys"][i],
                 "modifiers": key["to_mods"][i]
                 }
             ]
            }
        )
with open ("/Users/ich/.config/karabiner/assets/complex_modifications/adnw.json", "w") as f:
    js.dump(data, f, indent=3)
