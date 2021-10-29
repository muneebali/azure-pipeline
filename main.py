from git import Repo
import pr
import sys

repo = Repo()
git = repo.git

path = 'refs/heads/main'
if (len(sys.argv) > 1):
    path = sys.argv[1]

branch = 'origin/main'
index = path.find('refs/heads/')
if (index != -1):
    index = index + len('refs/heads/')
    branch = 'origin/' + path[index:]
else:
    print ("using default main branch")

comment = """
## Markdown

```
{}
```

""".format(git.diff(branch))

msg = pr.Message()
result = msg.add(comment=comment)
if result is False:
    print("Sending failed")
