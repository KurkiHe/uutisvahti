# Uutisvahti

Kahdeksan suomalaisen urheilusivuston RSS-uutisvirrat yhdessä mobiilinäkymässä.

## Käyttöönotto
1. Lataa tämän paketin tiedostot julkiseen GitHub-repositorioon säilyttäen `.github/workflows/update.yml` -polun.
2. Repository → Settings → Actions → General → Workflow permissions → Read and write permissions (jos valittavissa), tallenna.
3. Actions → Päivitä uutiset → Run workflow. Odota, että `news.json` ilmestyy.
4. Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.
5. Avaa Pagesin näyttämä URL puhelimella ja lisää Safarin Jaa-valikosta kotinäytölle.

GitHubin ajastetut työt voivat viivästyä, eivätkä kaikki sivustot välttämättä tarjoa toimivaa RSS-syötettä. Sivun alussa näkyvät lähteet, joiden syötteitä ei saatu luettua. Artikkelien säilyminen alkaa ensimmäisestä onnistuneesta hausta.
