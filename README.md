## Mail Watcher For XFCE Desktop Environment

### config mailbox

```shell
cp config.json.example config.json
```

### setup crontab

```shell
*/5 * * * * /usr/bin/python /opt/mail-watcher/mail-watcher.py
```
