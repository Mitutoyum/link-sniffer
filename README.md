# Link Sniffer

Discord selfbot to sniff for links with 3 variants

| Variant   | Description                  |
| :-------- | :-------                     |
| `global`  | Sniffs on all servers        |
| `server`  | Sniffs on a specific server  |
| `channel` | Sniffs on a specific channel |

You can set sniff type on `config.json`

## Notes
Dont use your main account to sniff

Records are saved in `records.txt`

Your token is saved in `.env`

To get your account token, paste this code into the console
```
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

## Installation
```
git clone https://github.com/Mitutoyum/link-sniffer.git
cd ./link-sniffer

pip install -r requirements.txt

echo "TOKEN=<your token goes here>" > .env
```
