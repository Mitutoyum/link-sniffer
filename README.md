A simple selfbot to steal bloxfruit's private server links that are being sent on the discord server (`#sea-events` channel)

### Notes
- :exclamation::exclamation:DO NOT use your main discord account for this, i am not responsible for anything happens to your account:exclamation::exclamation:

- records are saved in `records.txt`

- to get your account token, you can paste this code into the console
```
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

### Installation
- run these commands
```
git clone https://github.com/Mitutoyum/bloxfruits-link-stealer.git

cd ./bloxfruits-link-stealer

pip install -r requirements.txt

echo "TOKEN=<your token goes here>" > .env
```
