## Code
```python
import requests
import markdown

API_URL = "https://ai.electro.us.ci/ask"

prompt = """
Lundi 8h a 10h, cour informatique, enseignant Mohamed, group 1, salle 1
Mardi 10h a 12h, cour mathématiques, enseignant Ali, group 2, salle 3
Mercredi 14h a 16h, cour physique, enseignant Sara, group 1, salle 5
Jeudi 8h a 10h, cour anglais, enseignant Nour, group 3, salle 2
Vendredi 13h a 15h, cour chimie, enseignant Karim, group 4, salle 7
Samedi 9h a 11h, cour biologie, enseignant Leila, group 2, salle 4
Dimanche 11h a 13h, cour histoire, enseignant Youssef, group 5, salle 6
Lundi 15h a 17h, cour sport, enseignant Amine, group 1, salle Gymnase
Mardi 8h a 10h, cour programmation, enseignant Hana, group 6, salle 8
Mercredi 10h a 12h, cour réseaux, enseignant Omar, group 3, salle 9
Jeudi 14h a 16h, cour bases de données, enseignant Rania, group 2, salle 10
Vendredi 8h a 10h, cour algorithmes, enseignant Sami, group 1, salle 11
"""

response = requests.post(API_URL, json={"prompt": prompt})

if response.status_code == 200:
    md_table = response.json()["response"]
    html_table = markdown.markdown(md_table, extensions=['tables'])
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emploi du Temps</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Emploi du Temps</h1>
    {html_table}
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_document)

    print("Table saved to index.html")
else:
    print("Error:", response.status_code, response.text)
```
## Output **index.html**

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emploi du Temps</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Emploi du Temps</h1>
    <table>
<thead>
<tr>
<th>Jour</th>
<th>Heure</th>
<th>Cours</th>
<th>Enseignant</th>
<th>Groupe</th>
<th>Salle</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lundi</td>
<td>8h a 10h</td>
<td>informatique</td>
<td>Mohamed</td>
<td>group 1</td>
<td>salle 1</td>
</tr>
<tr>
<td>Mardi</td>
<td>10h a 12h</td>
<td>mathématiques</td>
<td>Ali</td>
<td>group 2</td>
<td>salle 3</td>
</tr>
<tr>
<td>Mercredi</td>
<td>14h a 16h</td>
<td>physique</td>
<td>Sara</td>
<td>group 1</td>
<td>salle 5</td>
</tr>
<tr>
<td>Jeudi</td>
<td>8h a 10h</td>
<td>anglais</td>
<td>Nour</td>
<td>group 3</td>
<td>salle 2</td>
</tr>
<tr>
<td>Vendredi</td>
<td>13h a 15h</td>
<td>chimie</td>
<td>Karim</td>
<td>group 4</td>
<td>salle 7</td>
</tr>
<tr>
<td>Samedi</td>
<td>9h a 11h</td>
<td>biologie</td>
<td>Leila</td>
<td>group 2</td>
<td>salle 4</td>
</tr>
<tr>
<td>Dimanche</td>
<td>11h a 13h</td>
<td>histoire</td>
<td>Youssef</td>
<td>group 5</td>
<td>salle 6</td>
</tr>
<tr>
<td>Mardi</td>
<td>8h a 10h</td>
<td>programmation</td>
<td>Hana</td>
<td>group 6</td>
<td>salle 8</td>
</tr>
<tr>
<td>Mercredi</td>
<td>10h a 12h</td>
<td>réseaux</td>
<td>Omar</td>
<td>group 3</td>
<td>salle 9</td>
</tr>
<tr>
<td>Jeudi</td>
<td>14h a 16h</td>
<td>bases de données</td>
<td>Rania</td>
<td>group 2</td>
<td>salle 10</td>
</tr>
<tr>
<td>Vendredi</td>
<td>8h a 10h</td>
<td>algorithmes</td>
<td>Sami</td>
<td>group 1</td>
<td>salle 11</td>
</tr>
</tbody>
</table>
</body>
</html>
