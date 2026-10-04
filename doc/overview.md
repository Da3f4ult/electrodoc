# Overview

Electro AI provides a documentation site and a local-model chat API. The documentation is hosted separately from the API so the website and AI requests use the correct domains.

## The two domains

- **Documentation:** [https://electro.us.ci/](https://electro.us.ci/) — the docs interface only.

- **AI API:** [https://ai.electro.us.ci/](https://ai.electro.us.ci/) — the API host. Send prompts to [https://ai.electro.us.ci/ask](https://ai.electro.us.ci/ask).

Do not send AI requests to `electro.us.ci`; use `ai.electro.us.ci` for all API calls.

## Ask the model

Send a JSON `POST` request to `/ask` with a non-empty `prompt`:

```bash
curl -X POST https://ai.electro.us.ci/ask \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Explain an API in one sentence."}'
```

A successful response looks like this:

```json
{
  "response": "An API lets software communicate through defined requests and responses."
}
```

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
