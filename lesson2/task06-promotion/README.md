# Задание 6. Promotion: staging → release

**Что делаем:** заводим в Artifactory два локальных docker-репозитория
и проводим образ через контроль качества: сначала staging, после
проверки — release. Деплой в прод должен ходить только в release.

## Что сделать

1. Создайте локальные репозитории `docker-staging-local` и
   `docker-release-local`. Назначьте им порты 8091 и 8092
   (HTTP Settings → Port, как в занятии 1 — порты уже проброшены
   в compose-файле стенда).
2. Доставьте образ в staging:

   ```bash
   docker login localhost:8091     # креды Artifactory
   docker pull localhost:8090/<логин>/pipeline-lab:latest
   docker tag localhost:8090/<логин>/pipeline-lab:latest \
              localhost:8091/pipeline-lab:____   # впишите версию релиза
   docker push localhost:8091/pipeline-lab:____
   ```

3. Проведите promotion через jfrog CLI — найдите команду
   `jf rt docker-promote` и выполните её: источник
   `docker-staging-local`, цель `docker-release-local`.
4. Убедитесь, что образ появился в release-репозитории
   (UI или `jf rt s "docker-release-local/"`).
5. Переключите деплой: в `docker-compose.deploy.yml` замените
   репозиторий на release (порт 8092, имя `pipeline-lab`,
   тег — версия), поднимите и проверьте `curl`.

## Вопрос на подумать (письменно)

Чем promotion отличается от простого `docker push` сразу в release?
Что мы выигрываем?

## В отчёт

- вывод `jf rt docker-promote` и список файлов release-репозитория;
- обновлённый `docker-compose.deploy.yml`;
- ответ на вопрос.
