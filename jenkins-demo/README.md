# Jenkins-демо (краткий показ)

Здесь лежит `Jenkinsfile` — тот же пайплайн, что мы собрали на
GitHub Actions, но в синтаксисе Jenkins (declarative pipeline).

**На занятии** преподаватель покажет его вживую за 10–15 минут:
поднимет Jenkins в Docker, создаст джобу из этого Jenkinsfile и
прогонит пайплайн. Вам повторять не нужно — просто сравните
структуру со своим `ci.yml`:

| GitHub Actions | Jenkins |
|---|---|
| `on.push` | триггер из SCM / webhook |
| `jobs.<name>` | `stage('...')` |
| `runs-on: ubuntu-latest` | `agent` (контроллер или агент) |
| `steps` / `uses` | `steps` / `sh` / плагины |
| `secrets.GITHUB_TOKEN` | Credentials store + `withCredentials` |

**Подробно Jenkins — на семинаре наставника.** Там будет
своя практика: агенты, credentials, общие библиотеки, Blue Ocean.
