# Overview

Electro AI provides a documentation site and a local-model chat API. The documentation is hosted separately from the API so the website and AI requests use the correct domains.

## The two domains

- **Documentation:** [https://electro.us.ci/](https://electro.us.ci/) — the docs interface only.

- **AI API:** [https://ai.electro.us.ci/](https://ai.electro.us.ci/) — the API host. Send prompts to [https://ai.electro.us.ci/ask](https://ai.electro.us.ci/ask).

Do not send AI requests to `electro.us.ci`; use `ai.electro.us.ci` for all API calls.

## Ask the model

Send a  `POST` request to `/ask` with a non-empty `prompt`:

```python
import requests

API_URL = "https://ai.electro.us.ci/ask"

prompt = (
    "Lundi 8h a 10h, cour informatique, enseignant Mohamed, group 1, salle 1"
)

response = requests.post(API_URL, json={"prompt": prompt})

if response.status_code == 200:
    print(response.json()["response"])
else:
    print("Error:", response.status_code, response.text)
```

A successful response looks like this:

<table style="border: solid black 2px; border-collapse: collapse;">
    <tr>
        <th style="border: solid black 2px;">Jour</th>
        <th style="border: solid black 2px;">Heure</th>
        <th style="border: solid black 2px;">Cours</th>
        <th style="border: solid black 2px;">Enseignant</th>
        <th style="border: solid black 2px;">Groupe</th>
        <th style="border: solid black 2px;">Salle</th>
    </tr>
    <tr>
        <td style="border: solid black 2px;">Lundi</td>
        <td style="border: solid black 2px;">8h a 10h</td>
        <td style="border: solid black 2px;">informatique</td>
        <td style="border: solid black 2px;">Mohamed</td>
        <td style="border: solid black 2px;">Groupe 1</td>
        <td style="border: solid black 2px;">Salle 1</td>
    </tr>
</table>


There is no request-level output-token cap. The model ends its response when it reaches its end-of-turn token or the available context limit. Prompts must be no longer than 20,000 characters.

## Local inference

The API runs the model on its own host using `llama-cpp-python` and a local GGUF model file. It does not call Groq and does not need a provider API key. The model file is not included in the app bundle; the operator supplies it on the API host.

## Useful endpoints

| Method | URL | Purpose |
| --- | --- | --- |
| `GET` | `https://ai.electro.us.ci/` | API endpoint metadata as JSON |
| `POST` | `https://ai.electro.us.ci/ask` | Generate a response from a prompt |
| `GET` | `https://ai.electro.us.ci/health` | Basic service liveness check |

The health endpoint confirms that the web app responds; it does not load or verify the model.
