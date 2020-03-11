## Mail Watcher For XFCE Desktop Environment

### config mailbox

```shell
cp config.json.example config.json
```

### setup crontab

```shell
*/5 * * * * /usr/bin/python /opt/matcher/mail-watcher.py
```